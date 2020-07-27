# -*- coding: utf-8 -*-
"""
Created on Wed May 13 01:48:47 2020

@author: Mustehssun
"""

from sklearn.ensemble import RandomForestClassifier

from src.multilabel.classifiers.classifier import Classifier
from src.multilabel.multilabel_dataset.multilabel_dataset import cons_multilabel_dataset, set_instance_features_train, set_instance_labels_train, get_instance_features_train, get_instance_labels_train, get_total_features_train, get_total_labels_train, get_instance_features_test, get_instance_labels_test, get_total_features_test, get_total_labels_test


class RandomForest(Classifier):
    def __init__(self):
        self.classifier = RandomForestClassifier()
    
    def fit(self, multilabel_dataset):
        features = get_instance_features_train(multilabel_dataset)
        labels = get_instance_labels_train(multilabel_dataset)

        self.classifier.fit(features, labels)
        
        return self
        
    def classify(self, multilabel_dataset):
        features = get_instance_features_test(multilabel_dataset)

        results = list(self.classifier.predict(features))
        
        return results
