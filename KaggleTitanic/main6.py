import pandas as pd
import numpy as np

# データの読み込み
train_data = pd.read_csv('./KaggleTitanic/titanic/train.csv')
test_data = pd.read_csv('./KaggleTitanic/titanic/test.csv')

# 欠損値の処理
train_data['Age'].fillna(train_data['Age'].median(), inplace=True)
test_data['Age'].fillna(test_data['Age'].median(), inplace=True)
train_data['Fare'].fillna(train_data['Fare'].median(), inplace=True)
test_data['Fare'].fillna(test_data['Fare'].median(), inplace=True)
train_data['Embarked'].fillna(train_data['Embarked'].mode()[0], inplace=True)
test_data['Embarked'].fillna(test_data['Embarked'].mode()[0], inplace=True)
train_data['Cabin'].fillna('Unknown', inplace=True)
test_data['Cabin'].fillna('Unknown', inplace=True)

# 新しい特徴量を作成
train_data['FamilySize'] = train_data['SibSp'] + train_data['Parch'] + 1
test_data['FamilySize'] = test_data['SibSp'] + test_data['Parch'] + 1

# キャビンの頭文字を抽出して新しい列を作成
train_data['CabinInitial'] = train_data['Cabin'].str[0]
test_data['CabinInitial'] = test_data['Cabin'].str[0]

'''
# 不要な列を削除
train_data.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], axis=1, inplace=True)
test_data.drop(['Name', 'Ticket', 'Cabin'], axis=1, inplace=True)
'''

# カテゴリカル変数の処理
train_data = pd.get_dummies(train_data, columns=['Sex', 'Embarked', 'CabinInitial'])
test_data = pd.get_dummies(test_data, columns=['Sex', 'Embarked', 'CabinInitial'])

#　確認
columns = train_data.columns
print(columns)
print(train_data.head())

# 特徴量の選択
features = ['Pclass', 'Sex_female', 'Sex_male', 'Age', 'SibSp', 'Parch', 'Fare',
            'Embarked_C', 'Embarked_Q', 'Embarked_S', 'FamilySize',
            'CabinInitial_A', 'CabinInitial_B', 'CabinInitial_C', 'CabinInitial_D',
            'CabinInitial_E', 'CabinInitial_F', 'CabinInitial_G', 'CabinInitial_U']
X_train = train_data[features]
y_train = train_data['Survived']
X_test = test_data[features]

# モデルの作成
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier

random_forest = RandomForestClassifier(random_state=42)
gradient_boosting = GradientBoostingClassifier(random_state=42)

# RandomForestClassifierのハイパーパラメータの範囲を指定
param_grid_rf = {
    'n_estimators': [100, 200, 300],
    'max_depth': [None, 5, 10],
    'criterion': ['gini', 'entropy']
}

# GridSearchCVを使って最適なハイパーパラメータを探索
grid_rf = GridSearchCV(random_forest, param_grid_rf, cv=5)
grid_rf.fit(X_train, y_train)

# 最適なハイパーパラメータを表示
print("RandomForestClassifierの最適なハイパーパラメータ:", grid_rf.best_params_)

# GradientBoostingClassifierのハイパーパラメータの範囲を指定
param_grid_gb = {
    'n_estimators': [100, 200, 300],
    'learning_rate': [0.1, 0.05, 0.01],
    'max_depth': [3, 5, 10],
    'loss': ['deviance', 'exponential']
}

# GridSearchCVを使って最適なハイパーパラメータを探索
grid_gb = GridSearchCV(gradient_boosting, param_grid_gb, cv=5)
grid_gb.fit(X_train, y_train)

# 最適なハイパーパラメータを表示
print("GradientBoostingClassifierの最適なハイパーパラメータ:", grid_gb.best_params_)

# チューニング後のモデルの作成
random_forest_tuned = RandomForestClassifier(
    n_estimators=grid_rf.best_params_['n_estimators'],
    max_depth=grid_rf.best_params_['max_depth'],
    criterion=grid_rf.best_params_['criterion'],
    random_state=42
)

gradient_boosting_tuned = GradientBoostingClassifier(
    n_estimators=grid_gb.best_params_['n_estimators'],
    learning_rate=grid_gb.best_params_['learning_rate'],
    max_depth=grid_gb.best_params_['max_depth'],
    loss=grid_gb.best_params_['loss'],
    random_state=42
)

random_forest_tuned.fit(X_train, y_train)
gradient_boosting_tuned.fit(X_train, y_train)

rf_predictions_tuned = random_forest_tuned.predict(X_test)
gb_predictions_tuned = gradient_boosting_tuned.predict(X_test)

ensemble_predictions_tuned = (rf_predictions_tuned + gb_predictions_tuned) / 2
ensemble_predictions_rounded_tuned = np.where(ensemble_predictions_tuned >= 0.5, 1, ensemble_predictions_tuned)
ensemble_predictions_rounded_tuned = ensemble_predictions_rounded_tuned.astype(int)

# 予測結果をDataFrameに変換
output_tuned = pd.DataFrame({'PassengerId': test_data['PassengerId'], 'Survived': ensemble_predictions_rounded_tuned})

# CSVファイルに書き込み
output_tuned.to_csv('./KaggleTitanic/submission6.csv', index=False)

