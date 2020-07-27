# -*- coding: utf-8 -*-
"""
Created on Wed May 13 01:26:26 2020

@author: Mustehssun
"""

from .impls.decision_tree import DecisionTree
from .impls.linear_regression import LinearRegression
from .impls.naive_bayes import NaiveBayes
from .impls.random_forest import RandomForest
from .impls.svm import SVM


def cons_classifier(classifier_name):
    if classifier_name == "decision_tree":
        return DecisionTree()
    elif classifier_name == "linear_regression":
        return LinearRegression()
    elif classifier_name == "naive_bayes":
        return NaiveBayes()
    elif classifier_name == "random_forest":
        return RandomForest()
    elif classifier_name == "svm":
        return SVM()
    else:
        raise Exception("Unspecified classifier")
    
    return lambda dataset: "results after using " + classifier_name

