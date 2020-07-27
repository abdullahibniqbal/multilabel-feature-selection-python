# -*- coding: utf-8 -*-
"""
Created on Thu May 14 20:27:16 2020

@author: Mustehssun
"""

import abc


class Classifier(abc.ABC):
    @abc.abstractmethod
    def fit(self, multilabel_dataset):
        pass
    
    @abc.abstractmethod
    def classify(self, multilabel_dataset):
        pass
