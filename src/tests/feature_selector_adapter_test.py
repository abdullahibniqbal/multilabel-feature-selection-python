# import unittest
# from sklearn.feature_selection import mutual_info_classif, SelectKBest
#
# from src.multilabel.dataset_importers.dataset_importer import import_training_set, import_testing_set
# from src.multilabel.multilabel_dataset.multilabel_dataset import cons_multilabel_dataset
#
# from src.multilabel.feature_selectors.feature_selector_adapter import FeatureSelectorAdapter
#
#
# class FeatureSelectorAdapterTest(unittest.TestCase):
#     def setUp(self) -> None:
#         self.feature_selector = FeatureSelectorAdapter(SelectKBest(mutual_info_classif, 3))
#
#         self.multilabel_dataset = cons_multilabel_dataset(import_training_set("emotions"), import_testing_set("emotions"))
#
#     def test_fit(self):
#         self.feature_selector.fit(self.multilabel_dataset)
#
#     def test_transform(self):
#         self.feature_selector.fit(self.multilabel_dataset)
#
#         features_test = [
#             [1, 2, 3, 4],
#             [5, 8, 6, 7],
#             [1.5, 1.8, 6, 7],
#             [8, 8, 8, 5],
#             [1, 0.6, 9, 7],
#             [9, 11, 10, 8]
#         ]
#
#         selected_features = self.feature_selector.transform(features_test)
#
#         assert len(selected_features) == 6, "number of instances should be the same"
#         assert len(selected_features[0]) == 3, "number of selected features should be 3"
#
#
# if __name__ == '__main__':
#     unittest.main()
