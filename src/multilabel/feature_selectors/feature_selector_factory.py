# -*- coding: utf-8 -*-
"""
Created on Wed May 13 01:34:52 2020

@author: Mustehssun
"""

from sklearn.feature_selection import mutual_info_classif, f_classif, SelectKBest

from .feature_selector_adapter import FeatureSelectorAdapter


def create_scorer(scorer_name):
    if scorer_name == "mutual_information":
        return mutual_info_classif
    elif scorer_name == "f_classif":
        return f_classif
    else:
        raise Exception("Unspecified feature selector's scorer")


def create_filter(filter_name, scorer, num_of_selected_features):
    if filter_name == "select_k_best":
        return FeatureSelectorAdapter(SelectKBest(scorer, num_of_selected_features))
    else:
        raise Exception("Unspecified feature selector's filter")


def create_feature_selector(scorer_name, filter_name, num_of_selected_features):
    scorer = create_scorer(scorer_name)

    return create_filter(filter_name, scorer, num_of_selected_features)
