from scipy.sparse import csr_matrix
from pandas import DataFrame
import copy

from src.multilabel.multilabel_dataset.multilabel_dataset import set_instance_features_train, set_instance_features_test, set_total_features_train, set_total_features_test, get_instance_features_train, get_instance_labels_train, get_total_features_train, get_total_features_test, get_instance_features_test
from src.multilabel.streams.stream import Stream


class FeatureSelectorAdapter:
    def __init__(self, selector):
        self.selector_train = selector
        self.selector_test = copy.deepcopy(selector)

    def fit(self, multilabel_dataset):
        features = get_instance_features_train(multilabel_dataset)
        labels = get_instance_labels_train(multilabel_dataset)

        features_matrix = csr_matrix(features)
        self.selector_train.fit(features_matrix, labels)
        self.selector_test.fit(features_matrix, labels)

        return self.selector_train

    def filter_total_features_and_update_train(self, multilabel_dataset):
        total_features = get_total_features_train(multilabel_dataset)
        selected_feature_booleans = self.selector_train.get_support().tolist()

        selected_features = []

        for index in range(0, len(selected_feature_booleans)):
            if selected_feature_booleans[index] == True:
                selected_features.append(total_features[index])

        set_total_features_train(multilabel_dataset, selected_features)

        return multilabel_dataset

    def filter_total_features_and_update_test(self, multilabel_dataset):
        total_features = get_total_features_test(multilabel_dataset)
        selected_feature_booleans = self.selector_train.get_support().tolist()

        selected_features = []

        for index in range(0, len(selected_feature_booleans)):
            if selected_feature_booleans[index] == True:
                selected_features.append(total_features[index])

        set_total_features_test(multilabel_dataset, selected_features)

        return multilabel_dataset

    def transform(self, multilabel_dataset):
        features_train = get_instance_features_train(multilabel_dataset)
        selected_train = self.selector_train.transform(features_train)

        set_instance_features_train(multilabel_dataset, selected_train)
        self.filter_total_features_and_update_train(multilabel_dataset)

        features_test = get_instance_features_test(multilabel_dataset)
        selected_test = self.selector_test.transform(features_test)

        set_instance_features_test(multilabel_dataset, selected_test)
        self.filter_total_features_and_update_test(multilabel_dataset)

        return multilabel_dataset
