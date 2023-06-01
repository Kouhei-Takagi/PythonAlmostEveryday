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

# 不要な列を削除
train_data.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], axis=1, inplace=True)
test_data.drop(['Name', 'Ticket', 'Cabin'], axis=1, inplace=True)

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
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier

random_forest = RandomForestClassifier(n_estimators=100, random_state=42)
gradient_boosting = GradientBoostingClassifier(n_estimators=100, random_state=42)

random_forest.fit(X_train, y_train)
gradient_boosting.fit(X_train, y_train)

rf_predictions = random_forest.predict(X_test)
gb_predictions = gradient_boosting.predict(X_test)

ensemble_predictions = (rf_predictions + gb_predictions) / 2
ensemble_predictions_rounded = np.where(ensemble_predictions >= 0.5, 1, ensemble_predictions)
ensemble_predictions_rounded = ensemble_predictions_rounded.astype(int)

# 予測結果をDataFrameに変換
output = pd.DataFrame({'PassengerId': test_data['PassengerId'], 'Survived': ensemble_predictions_rounded})

# CSVファイルに書き込み
output.to_csv('./KaggleTitanic/submission4.csv', index=False)
