#coding=utf-8
import sys
from MW_SVDD.SVDD.svdd import SVDD
from MW_SVDD.SVDD.visualize import Visualization as draw
import MW_SVDD.data as load
import numpy as np

# load TE process data
trainData, testData, trainLabel, testLabel = load.TE()

# set SVDD parameters
parameters = {"positive penalty": 0.9,
              "negative penalty": [],
              "kernel": {"type": 'gauss', "width": 1},
              "option": {"display": 'on'}}


# construct an SVDD model
svdd = SVDD(parameters)

# train SVDD model
svdd.train(trainData, trainLabel)

# test SVDD model
distance, accuracy = svdd.test(testData, testLabel)

# visualize the results
draw.testResult(svdd, distance)
# draw.testROC(testLabel, distance)



