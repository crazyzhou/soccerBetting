__author__ = 'Zhou Yumin'

import numpy as np


def gain(pred, rst, oddH, oddD, oddA):
    if pred == rst:
        if pred == 'H':
            return oddH
        elif pred == 'D':
            return oddD
        else:
            return oddA
    else:
        return 0


def naiveStrategy(probH, probD, probA):
    maxProb = max(probH, probD, probA)
    if maxProb == probH:
        return 'H'
    elif maxProb == probD:
        return 'D'
    else:
        return 'A'


def bestStrategy(prob, odds):
    a = np.transpose(prob)
    b = np.transpose(odds)
    deltaH = a[2] - 1 / b[0]
    deltaD = a[1] - 1 / b[1]
    deltaA = a[0] - 1 / b[2]
    pred = []
    for i in range(0, len(a[0])):
        maxDelta = max(deltaH[i], deltaD[i], deltaA[i])
        if maxDelta == deltaH[i]:
            pred.append(3)
        elif maxDelta == deltaD[i]:
            pred.append(1)
        else:
            pred.append(0)
    return np.transpose(pred)

def accuracy(pred, rst):
    shape = pred.shape
    new = pred - rst
    rst = shape[0] - np.count_nonzero(new)
    return rst / float(shape[0])

def gain(pred, rst, odds):
    ret = 0
    for i in range(0, len(pred)):
        if pred[i] == rst[i]:
            if pred[i] == 3:
                ret += (odds[i][0]-1)
            else:
                ret += (odds[i][2-pred[i]]-1)
        else:
            ret -= 1
    return ret
