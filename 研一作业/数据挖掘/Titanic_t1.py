#coding=utf-8
import pandas as pd
import numpy as np
from sklearn.svm import SVC
from sklearn import metrics
from sklearn.model_selection import GridSearchCV

pd.set_option('display.max_columns', None)  #设置pandas读取的数据显示全部列
## 读取训练和测试数据集
data_train = pd.read_csv('Titanic/train.csv')
data_test = pd.read_csv('Titanic/test.csv')
data_test_Y = pd.read_csv('Titanic/gender_submission.csv')
combine = [data_train, data_test]   #组合数据，便于后续处理
# print(data_train.describe(include='all'))    #输出测试集的相应信息，发现age列有空值，需补全数据
# print(data_train.isnull().sum())    #统计每个特征下的缺失值个数
## 补全age数据（缺一百多个），Fare数据，用中位数填充,补全Embarked数据（缺两个），用出现次数最多的值填充
for dataset in combine:
    dataset['Age'] = dataset['Age'].fillna(dataset['Age'].median())  #填充age空值
    dataset['Fare'] = dataset['Fare'].fillna(dataset['Fare'].median())  #填充Fare空值
    dataset['Embarked'] = dataset['Embarked'].fillna(dataset['Embarked'].value_counts().index[0]) #填充Embarked空值
# print(data_test.describe())

## 数值化性别(male->0,female->1),乘客登船港口（S->0,C->1,Q->2）
# print(data_train['Sex'].unique())  #返回其参数数组中所有不同的值，并且按照从小到大的顺序排列
for dataset in combine:
    dataset.loc[dataset['Sex'] == 'male', 'Sex'] = 0
    dataset.loc[dataset['Sex'] == 'female', 'Sex'] = 1
    dataset.loc[dataset['Embarked'] == 'S', 'Embarked'] = 0
    dataset.loc[dataset['Embarked'] == 'C', 'Embarked'] = 1
    dataset.loc[dataset['Embarked'] == 'Q', 'Embarked'] = 2


## 选取特征
predictors=['Pclass','Sex','Age','SibSp','Parch','Fare','Embarked']
X_train = data_train[predictors]
Y_train = data_train['Survived']
X_test = data_test[predictors]
Y_test = data_test_Y['Survived']

## 调用SVM模型
svc = SVC(kernel='rbf', class_weight='balanced', probability=True)
# 网格交叉验证
c_range = np.logspace(-1, 6, 20,base=2)   #构造等比数列：2的-5次方到2的15次方中均匀产生11个数
gamma_range = np.logspace(-14, -6, 20,base=2)
param_grid = [{'kernel': ['rbf'], 'C': c_range, 'gamma': gamma_range}]
grid = GridSearchCV(svc, param_grid, cv=5, n_jobs=-1)
grid.fit(X_train, Y_train)
print(grid.best_params_)

## 使用模型预测
# 对训练数据进行预测
Y_pred = grid.predict(X_train)
score = metrics.accuracy_score(Y_train, Y_pred, normalize=True, sample_weight=None)
pre = metrics.precision_score(Y_train, Y_pred)
recall = metrics.recall_score(Y_train, Y_pred)
print(score, pre, recall)
# 对测试数据进行预测
Y_pred = grid.predict(X_test)
score = metrics.accuracy_score(Y_test, Y_pred, normalize=True, sample_weight=None)
pre = metrics.precision_score(Y_test, Y_pred)
recall = metrics.recall_score(Y_test, Y_pred)
print(score, pre, recall)