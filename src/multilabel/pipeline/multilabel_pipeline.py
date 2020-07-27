# -*- coding: utf-8 -*-
"""
Created on Wed May 13 01:21:50 2020

@author: Mustehssun
"""
import sklearn.metrics as metrics

from ..dataset_importers.dataset_importer import import_training_set, import_testing_set
from ..multilabel_dataset.multilabel_dataset import cons_multilabel_dataset, get_instance_labels_test, get_total_labels_test
from ..problem_transformation.problem_transformer import cons_problem_transformer
from ..feature_selectors.feature_selector_factory import create_feature_selector
from ..classifiers.classifier_factory import cons_classifier
from src.multilabel.visualizer.visualizer import display_dataframe


class MultilabelPipelineFactoryArgument:
    def __init__(self):
        self.dataset = "emotions"
        self.problem_transformer = "binary_relevance", 
        self.feature_selector = "mutual_information"
        self.feature_filter_name = "select_k_best"
        self.num_of_selected_features = 2
        self.classifier = "decision_tree"


def multilabel_pipeline_factory(args):
    def create_pipeline():
        dataset_training = import_training_set(args.dataset)
        dataset_testing = import_testing_set(args.dataset)

        multilabel_dataset = cons_multilabel_dataset(dataset_training, dataset_testing)

        feature_selector = create_feature_selector(args.feature_selector, args.feature_filter, args.num_of_selected_features)
        classifier = cons_classifier(args.classifier)
        transform_datasets = cons_problem_transformer(args.problem_transformer)
        
        return (multilabel_dataset, feature_selector, transform_datasets, classifier)
    
    return create_pipeline


def execute_multilabel_pipeline(create_pipeline):
    multilabel_dataset, feature_selector, transform_problem, classify = create_pipeline()

    results = transform_problem(multilabel_dataset, feature_selector, classify)

    labels_test = get_instance_labels_test(multilabel_dataset)
    total_labels = get_total_labels_test(multilabel_dataset)

    print("hamming loss: ", metrics.hamming_loss(labels_test, results.iloc[:, -len(total_labels):]))

    display_dataframe(results)

    return results
