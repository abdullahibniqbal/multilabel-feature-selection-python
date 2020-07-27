# -*- coding: utf-8 -*-
"""
Created on Wed May 13 21:26:02 2020

@author: Mustehssun
"""

import numpy as numpy
from pandas import DataFrame, concat

from src.multilabel.streams.stream import Stream
from src.multilabel.multilabel_dataset.multilabel_dataset import cons_multilabel_dataset, set_instance_labels_train, get_instance_features_train, get_instance_labels_train, get_total_features_train, get_total_labels_train, get_instance_features_test, get_instance_labels_test, get_total_features_test, get_total_labels_test


def combine_partitioned_results(multilabel_dataset, partitioned_results):
    labels_dataframe = create_labels_dataframe(multilabel_dataset, partitioned_results)
    features_dataframe = create_features_dataframe(multilabel_dataset)

    return concat([features_dataframe, labels_dataframe], axis=1)


def create_features_dataframe(multilabel_dataset):
    features = get_instance_features_test(multilabel_dataset)
    total_features = get_total_features_test(multilabel_dataset)
    feature_names = Stream(total_features).map(lambda elem: elem[0]).as_list()

    return DataFrame(features, columns=feature_names)


def create_labels_dataframe(multilabel_dataset, partitioned_results):
    labels = get_total_labels_test(multilabel_dataset)
    label_names = Stream(labels).map(lambda elem: elem[0]).as_list()

    return DataFrame(partitioned_results, index=label_names).transpose()


def select_features(multilabel_dataset, feature_selector):
    feature_selector.fit(multilabel_dataset)

    return feature_selector.transform(multilabel_dataset)


def augment_label(multilabel_dataset, labels):
    new_dataset = multilabel_dataset.copy()
    set_instance_labels_train(new_dataset, labels)

    return new_dataset


def get_column_as_list(labels, column_number):
    return numpy.array(labels)[0:, column_number].tolist()


def partition_labels(multilabel_dataset):
    total_labels = get_total_labels_train(multilabel_dataset)

    instance_labels = get_instance_labels_train(multilabel_dataset)

    partitioned = []

    for column_number in range(0, len(total_labels)):
        column_as_list = get_column_as_list(instance_labels, column_number)
        partitioned.append(column_as_list)

    return partitioned


def partition_dataset(multilabel_dataset):
    partitioned_labels = partition_labels(multilabel_dataset)

    return                                                                                  \
        Stream(partitioned_labels)                                                          \
        .map(lambda label_partition: augment_label(multilabel_dataset, label_partition))    \
        .as_list()


def classify(multilabel_dataset, classifier):

    classifier.fit(multilabel_dataset)

    return classifier.classify(multilabel_dataset)


def transform_problem(multilabel_dataset, feature_selector, classifier) -> []:
    partitioned_datasets = partition_dataset(multilabel_dataset)

    fitted_feature_selectors =                                                      \
        Stream(partitioned_datasets)                                                \
        .map(lambda elem: select_features(elem, feature_selector)).as_list()

    partitioned_results =                               \
        Stream(fitted_feature_selectors)                \
        .map(lambda elem: classify(elem, classifier))   \
        .as_list()

    return combine_partitioned_results(multilabel_dataset, partitioned_results)

