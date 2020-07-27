# -*- coding: utf-8 -*-
"""
Created on Wed May 13 01:40:46 2020

@author: Mustehssun
"""

from skmultilearn.dataset import load_dataset

from src.multilabel.multilabel_dataset.multilabel_dataset import cons_multilabel_dataset_mock


# TODO make polymorphic
def import_training_set(dataset_name):
    dataset = load_dataset(dataset_name, "train")

    return cons_multilabel_dataset_mock(dataset)


# TODO make polymorphic
def import_testing_set(dataset_name):
    dataset = load_dataset(dataset_name, "test")

    return cons_multilabel_dataset_mock(dataset)
