#coding = utf-8
import numpy as np
import pandas as pd
import joblib
from sklearn.svm import SVC
from sklearn import metrics
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV, train_test_split

#加载数据集
def load_data(filename):
    data = pd.read_csv(filename)
    x = data.iloc[1:, 2:]    #数据特征
    y = data.iloc[1:, 1]     #标签：1-5
    scaler = StandardScaler()
    x_std = scaler.fit_transform(x)  # 标准化
    # 将数据划分为训练集和测试集，test_size=.3表示30%的测试集
    x_train, x_test, y_train, y_test = train_test_split(x_std, y, test_size=.2)
    return x_train, x_test, y_train, y_test


def svm_c(x_train, x_test, y_train, y_test):
    # 寻找最优参数
    # rbf核函数，设置数据权重
    svc = SVC(kernel='rbf', class_weight='balanced', decision_function_shape='ovo', probability=True)
    '''
    分类的时候，当不同类别的样本量差异很大时，很容易影响分类结果，因此要么每个类别的数据量大致相同，要么就要进行校正。sklearn的做法可以是加权，不设置class_weight参数时，默认值是所有类别的权值为1。
    '''
    c_range = np.logspace(-1, 6, 20,base=2)   #构造等比数列：2的-5次方到2的15次方中均匀产生11个数
    gamma_range = np.logspace(-14, -6, 20,base=2)
    # 网格搜索交叉验证的参数范围，cv=3,3折交叉,交叉验证：https://blog.csdn.net/weixin_40475450/article/details/80578943
    param_grid = [{'kernel': ['rbf'], 'C': c_range, 'gamma': gamma_range}]
    grid = GridSearchCV(svc, param_grid, cv=5, n_jobs=-1)
    # 训练模型 用过的参数：'C': 4.8, 'gamma': 0.00126，结果50多；'C': 3.856704, 'gamma': 0.003138,结果70多；'C': 1.244692, 'gamma': 0.00523，结果：
    # grid = SVC(kernel='rbf', class_weight='balanced', decision_function_shape='ovo', probability=True, C=1.244692, gamma=0.00523)
    grid.fit(x_train, y_train)
    print(grid.best_params_)    #输出最佳参数c和gamma
    # 保存模型到本地
    joblib.dump(grid, r'data\SVM模型\svm_model.pkl', compress=3)
    # 计算测试集准确率，精准率（precision），,召回率，f1值
    y_predict = grid.predict(x_test)  # 测试集预测分类结果
    score = metrics.accuracy_score(y_test, y_predict, normalize=True, sample_weight=None) #grid.score(x_test, y_test)  #准确率
    precision = metrics.precision_score(y_test, y_predict, average='weighted') #精准率
    recall = metrics.recall_score(y_test, y_predict, average='weighted')   #召回率
    f1 = metrics.f1_score(y_test, y_predict, average='weighted')   #f1值
    print('准确率为%s' % score)
    print('精准率（precision）:%s' % precision)
    print('召回率：%s' % recall)
    print('f1值：%s' % f1)

if __name__ == '__main__':

    '''
    这里可以先用小样本进行训练，得出最优参数，然后使用最优参数训练整体数据，不然网格加交叉验证应用于整体数据训练时间过长。
    '''
    svm_c(*load_data(r'data\特征向量\特征向量.csv'))