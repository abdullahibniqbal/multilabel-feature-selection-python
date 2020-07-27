# -*- coding: utf-8 -*-
"""
Created on Thu May 14 12:39:08 2020

@author: Mustehssun
"""

DATASET_TRAINING = 0
DATASET_TESTING = 1
TOTAL_LABELS = 3
INSTANCE_LABELS = 1
INSTANCE_FEATURES = 0


def get_total_labels(dataset):
    return dataset[TOTAL_LABELS]


def get_instance_labels(dataset):
    return dataset[INSTANCE_LABELS].toarray()


def get_instance_features(dataset):
    return dataset[INSTANCE_FEATURES].toarray()


def get_transformed_features(dataset):
    return dataset[INSTANCE_FEATURES]


def get_transformed_labels(dataset):
    return dataset[INSTANCE_LABELS]


def get_training_set(datasets):
    return datasets[DATASET_TRAINING]


def get_testing_set(datasets):
    return datasets[DATASET_TESTING]
