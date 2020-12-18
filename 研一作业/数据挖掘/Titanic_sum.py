# coding=utf-8
## 导入数据分析包
import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None)  # 设置pandas读取的数据显示全部列
## 导入可视化包
import seaborn as sns
import matplotlib.pyplot as plt
## 导入机器学习包
from sklearn.svm import SVC
from sklearn import metrics
from sklearn.model_selection import GridSearchCV

## 读取训练和测试数据集
data_train = pd.read_csv('Titanic/train.csv')
data_test = pd.read_csv('Titanic/test.csv')
data_test_Y = pd.read_csv('Titanic/gender_submission.csv')
combine = [data_train, data_test]  # 组合数据，便于后续处理

## 补全age数据（缺一百多个），Fare数据，用中位数填充，补全Embarked数据（缺两个），用出现次数最多的值填充
for dataset in combine:
    dataset['Age'] = dataset['Age'].fillna(dataset['Age'].median())  # 填充age空值
    dataset['Fare'] = dataset['Fare'].fillna(dataset['Fare'].median())  # 填充Fare空值
    dataset['Embarked'] = dataset['Embarked'].fillna(dataset['Embarked'].value_counts().index[0])  # 填充Embarked空值


# print(data_test.describe())

## 定义函数：统计变量和生存率的关系,stacked的值设置为True,为False默认展示该变量下的生存率
def visualize_survival(feature, stacked=False):
    if stacked:
        survived_rate = data_train.groupby([feature, 'Survived'])['Survived'].count().unstack().plot(kind='bar',stacked='True')
    else:
        # survived_rate = data_train[[feature,'Survived']].groupby([feature],as_index=False).mean().sort_values(by='Survived',ascending=False)
        survived_rate = (data_train.groupby([feature]).sum() / data_train.groupby([feature]).count())['Survived']
        survived_rate.plot(kind='bar')
    plt.title(feature + ' V.S. Survival')
    plt.show()


## 统计各变量和生存率的关系
    # Sex
visualize_survival('Sex')
    # Pclass
# visualize_survival('Pclass')
    # Embarked
# visualize_survival('Embarked', True)
    # Age,,age_cut选取特征时要去掉
ages = np.arange(0,90,10) #年龄分段
data_train['age_cut'] = pd.cut(data_train.Age,ages)
# visualize_survival('age_cut')
    # Fare,,fare_cut选取特征时要去掉
# print(data_train['Fare'].describe(include='all'))
fares = np.arange(0,100,10) #年龄分段
fares = np.append(fares, 500)
data_train['fare_cut'] = pd.cut(data_train.Fare,fares)
# visualize_survival('fare_cut')
    # Parch
# visualize_survival('Parch', True)
    # SibSp
# visualize_survival('SibSp')

#
# ## 特征工程
# # 数值化性别(male->0,female->1),乘客登船港口（S->0,C->1,Q->2）
# # print(data_train['Sex'].unique())  #返回其参数数组中所有不同的值，并且按照从小到大的顺序排列
# for dataset in combine:
#     dataset['Sex'].replace(['male', 'female'], [0, 1], inplace=True)
#     dataset['Embarked'].replace(['S', 'C', 'Q'], [0, 1, 2], inplace=True)
# # 离散化年龄：Age为0~80岁，等间隔分成五组
# for dataset in combine:
#     dataset['Age_band'] = 0
#     dataset.loc[dataset['Age'] <= 16, 'Age_band'] = 0
#     dataset.loc[(dataset['Age'] > 16) & (dataset['Age'] <= 32), 'Age_band'] = 1
#     dataset.loc[(dataset['Age'] > 32) & (dataset['Age'] <= 48), 'Age_band'] = 2
#     dataset.loc[(dataset['Age'] > 48) & (dataset['Age'] <= 64), 'Age_band'] = 3
#     dataset.loc[dataset['Age'] > 64, 'Age_band'] = 4
# # 离散化船票价格：
# for dataset in combine:
#     dataset['Fare_cat'] = 0
#     dataset.loc[dataset['Fare'] <= 7.91, 'Fare_cat'] = 0
#     dataset.loc[(dataset['Fare'] > 7.91) & (dataset['Fare'] <= 14.454), 'Fare_cat'] = 1
#     dataset.loc[(dataset['Fare'] > 14.454) & (dataset['Fare'] <= 31), 'Fare_cat'] = 2
#     dataset.loc[(dataset['Fare'] > 31) & (dataset['Fare'] <= 513), 'Fare_cat'] = 3
#
# # 选择特征
# Y_train = data_train['Survived']
# Y_test = data_test_Y['Survived']
#
# data_train.drop(['Name','Age','age_cut','Ticket','Fare','fare_cut','Cabin','PassengerId', 'Survived'],axis=1,inplace=True)
# data_test.drop(['Name','Age','Ticket','Fare','Cabin','PassengerId'],axis=1,inplace=True)
#
# X_train = data_train
# X_test = data_test
# ## 绘制相关性热图
# # sns.heatmap(data_train.corr(),annot=True,square=True,linewidths=0.2,cmap='RdYlGn')
# # plt.show()
#
# ## 调用SVM模型
# svc = SVC(kernel='rbf', class_weight='balanced', probability=True)
#     # 网格交叉验证
# c_range = np.logspace(-1, 6, 20,base=2)   #构造等比数列：2的-5次方到2的15次方中均匀产生11个数
# gamma_range = np.logspace(-14, -6, 20,base=2)
# param_grid = [{'kernel': ['rbf'], 'C': c_range, 'gamma': gamma_range}]
# grid = GridSearchCV(svc, param_grid, cv=5, n_jobs=-1)
# grid.fit(X_train, Y_train)
# print(grid.best_params_)
#
# ## 使用模型预测
#     # 对训练数据进行预测
# Y_pred = grid.predict(X_train)
# score = metrics.accuracy_score(Y_train, Y_pred, normalize=True, sample_weight=None)
# pre = metrics.precision_score(Y_train, Y_pred)
# recall = metrics.recall_score(Y_train, Y_pred)
# print(score, pre, recall)
#     # 对测试数据进行预测
# Y_pred = grid.predict(X_test)
# score = metrics.accuracy_score(Y_test, Y_pred, normalize=True, sample_weight=None)
# pre = metrics.precision_score(Y_test, Y_pred)
# recall = metrics.recall_score(Y_test, Y_pred)
# print(score, pre, recall)