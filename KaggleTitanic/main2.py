import pandas as pd
import numpy as np

# データの読み込み
train_data = pd.read_csv('./KaggleTitanic/titanic/train.csv')
test_data = pd.read_csv('./KaggleTitanic/titanic/test.csv')

# 欠損値の処理

# Ageの欠損値を中央値で補完
train_data['Age'].fillna(train_data['Age'].median(), inplace=True)
test_data['Age'].fillna(test_data['Age'].median(), inplace=True)

# Fareの欠損値を中央値で補完
train_data['Fare'].fillna(train_data['Fare'].median(), inplace=True)
test_data['Fare'].fillna(test_data['Fare'].median(), inplace=True)

# Embarkedの欠損値を最頻値で補完
train_data['Embarked'].fillna(train_data['Embarked'].mode()[0], inplace=True)
test_data['Embarked'].fillna(test_data['Embarked'].mode()[0], inplace=True)

# Cabinの欠損値を「Unknown」で補完
train_data['Cabin'].fillna('Unknown', inplace=True)
test_data['Cabin'].fillna('Unknown', inplace=True)

# 新しい特徴量を作成
train_data['FamilySize'] = train_data['SibSp'] + train_data['Parch'] + 1
test_data['FamilySize'] = test_data['SibSp'] + test_data['Parch'] + 1

# 不要な列を削除
train_data.drop(['PassengerId', 'Name', 'Ticket'], axis=1, inplace=True)
test_data.drop(['Name', 'Ticket'], axis=1, inplace=True)

# カテゴリカル変数の処理
train_data = pd.get_dummies(train_data, columns=['Sex', 'Embarked'])
test_data = pd.get_dummies(test_data, columns=['Sex', 'Embarked'])

#　確認
columns = train_data.columns
print(columns)

# 特徴量の選択
features = ['Pclass', 'Sex_female', 'Sex_male', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked_C', 'Embarked_Q', 'Embarked_S','FamilySize', 'Cabin']
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
output.to_csv('./KaggleTitanic/submission2.csv', index=False)