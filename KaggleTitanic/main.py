import pandas as pd

# データの読み込み
train_data = pd.read_csv('./KaggleTitanic/titanic/train.csv')
test_data = pd.read_csv('./KaggleTitanic/titanic/test.csv')

# 欠損値の処理
train_data['Age'].fillna(train_data['Age'].median(), inplace=True)
test_data['Age'].fillna(test_data['Age'].median(), inplace=True)
train_data['Fare'].fillna(train_data['Fare'].median(), inplace=True)
test_data['Fare'].fillna(test_data['Fare'].median(), inplace=True)

# カテゴリカル変数の処理
train_data = pd.get_dummies(train_data, columns=['Sex', 'Embarked'])
test_data = pd.get_dummies(test_data, columns=['Sex', 'Embarked'])

# 特徴量の選択
features = ['Sex_female', 'Sex_male', 'Age', 'Pclass', 'SibSp', 'Parch']
X_train = train_data[features]
y_train = train_data['Survived']
X_test = test_data[features]

# モデルの作成
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 予測
predictions = model.predict(X_test)

# 予測結果をDataFrameに変換
output = pd.DataFrame({'PassengerId': test_data['PassengerId'], 'Survived': predictions})

# CSVファイルに書き込み
output.to_csv('./KaggleTitanic/submission.csv', index=False)
