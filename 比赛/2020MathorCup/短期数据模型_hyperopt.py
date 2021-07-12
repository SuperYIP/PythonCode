#coding=utf-8
import pandas as pd
import numpy as np
import lightgbm as lgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, mean_absolute_error,mean_squared_error
import matplotlib.pyplot as plt
from hyperopt import fmin, tpe, hp, partial, space_eval, STATUS_OK

# 读取数据
train = pd.read_csv("C:\\Users\\伊海迪\\Desktop\\2020MathorCup大数据挑战赛\\赛道A\\赛道A附件\\my_train.csv")
# 填充上行业务量GB、下行业务量GB两列空值数据，用中位数填充
train['上行业务量GB'] = train['上行业务量GB'].fillna(train['上行业务量GB'].median())  # 填充上行业务量GB空值
train['下行业务量GB'] = train['下行业务量GB'].fillna(train['下行业务量GB'].median())  # 填充上行业务量GB空值

feature = ['小区编号', 'month', 'day', 'hour']  #选取特征
X = train[feature]  #构建训练集
y = train['上行业务量GB']  #获取目标值
# 数据集划分
X_train, X_test, y_train, y_test = train_test_split(X.values, y.values, test_size=0.2, random_state=0)
# 数据格式转换
lgb_train = lgb.Dataset(X_train, y_train)
lgb_eval = lgb.Dataset(X_test, y_test, reference=lgb_train)

N_FOLDS = 3  # k折交叉验证


# 损失函数，hyperopt的优化目标
def objective(params, n_folds=N_FOLDS):
    cv_results = lgb.cv(params, lgb_train, nfold=n_folds, num_boost_round=100,
                        early_stopping_rounds=10, metrics='rmse', seed=2018,
                        verbose_eval=True,
                        stratified=False)

    loss = min(cv_results['rmse-mean'])
    return {'loss': loss, 'params': params, 'status': STATUS_OK}

# 定义hyperopt的参数空间space'
space = {
    'boosting_type': 'gbdt',
    'objective': 'regression',
    'metric': 'rmse',
    'max_depth':hp.choice('max_depth',range(1,8,1)),
    'num_leaves':hp.choice('num_leaves',range(2,64,1)),
    'feature_fraction':hp.loguniform('feature_fraction',np.log(0.1), np.log(1)),
    'bagging_fraction':hp.loguniform('bagging_fraction',np.log(0.1), np.log(1)),
    'bagging_freq':hp.choice('bagging_freq',range(1,80,1)),
    'lambda_l1': hp.uniform('lambda_l1', 0.0, 1.0),
    'lambda_l2': hp.uniform('lambda_l2', 0.0, 1.0),
    'min_split_gain':hp.loguniform( 'min_split_gain' ,np.log(0.1), np.log(1)),
    'learning_rate': hp.loguniform('learning_rate', np.log(0.005), np.log(0.6))
}

# 开始优化（自动调参），best即为最优参数
algo = partial(tpe.suggest, n_startup_jobs=1)
best = fmin(fn = objective, space = space, algo = algo, max_evals = 20)
# 将参数转换为lgb的格式
lgb_params = space_eval(space, best)
print(lgb_params)

# 使用最优参数lgb_params训练得到lgb模型
boost_round = 100 # 迭代次数
early_stop_rounds = 10 # 验证数据若在early_stop_rounds轮中未提高，则提前停止
# 训练模型，这里没什么需要改的
results = {}
gbm = lgb.train(lgb_params,  #gbm即为得到的模型
                lgb_train,
                num_boost_round= boost_round, # 迭代次数
                valid_sets=(lgb_eval, lgb_train),
                valid_names=('validate','train'),
                early_stopping_rounds = early_stop_rounds,
                evals_result= results)

shot_test = pd.read_csv("C:\\Users\\伊海迪\\Desktop\\2020MathorCup大数据挑战赛\\赛道A\\赛道A附件\\shot_data.csv")
shot_pred = gbm.predict(shot_test.values, num_iteration=gbm.best_iteration)
shot_test['上行业务量GB'] = shot_pred
shot_test.to_csv("C:\\Users\\伊海迪\\Desktop\\2020MathorCup大数据挑战赛\\赛道A\\赛道A附件\\shot_data_result.csv", index = False)
