# -*- coding: utf-8 -*-
"""
Created on Tue May 19 21:18:50 2020

@author: Mustehssun
"""

from unittest import TestCase


class BinaryRelevanceTest(TestCase):
    def test_transform_data(self):
        total_features = ["action_scenes", "jokes", "cgi_effects", "tech_scenes"]
        instance_features = [
                [1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12]
            ]
        total_labels = ["action", "comedy", "sci_fi"]
        instance_labels = [
                [1, 1, 1],
                [1, 0, 1],
                [0, 0, 1]
            ]
        dataset = [instance_features, instance_labels, total_features, total_labels]

        # transformed_dataset = transform_dataset(dataset)
        #
        # print("transformed_dataset: ", transformed_dataset)

    def test_sum(self):
        assert 1 == 1, "Should be 1"



