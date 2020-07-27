import unittest

from src.multilabel.dataset_importers.dataset_importer import import_training_set, import_testing_set

from src.multilabel.multilabel_dataset.multilabel_dataset import cons_multilabel_dataset, set_instance_features_train, set_instance_labels_train, get_instance_features_train, get_instance_labels_train, get_total_features_train, get_total_labels_train, get_instance_features_test, get_instance_labels_test, get_total_features_test, get_total_labels_test


class MultilabelDatasetTest(unittest.TestCase):
    def setUp(self) -> None:
        self.multilabel_dataset = cons_multilabel_dataset(import_training_set("emotions"), import_testing_set("emotions"))

    def test_cons(self):
        print(type(self.multilabel_dataset))
        print(type([]))
        assert type(self.multilabel_dataset) == type({}), "multilabel dataset should be a list"

    def test_get_instance_features_train(self):
        features = get_instance_features_train(self.multilabel_dataset)

        assert type(features) == type([]), "instance_features_train should be a list"

    def test_get_instance_labels_train(self):
        labels = get_instance_labels_train(self.multilabel_dataset)

        assert type(labels) == type([]), "instance_labels_train should be a list"

    def test_get_total_features_train(self):
        features = get_total_features_train(self.multilabel_dataset)

        assert type(features) == type([]), "total_features_train should be a list"

    def test_get_total_labels_train(self):
        labels = get_total_labels_train(self.multilabel_dataset)

        assert type(labels) == type([]), "total_labels_train should be a list"

    def test_get_instance_features_test(self):
        features = get_instance_features_test(self.multilabel_dataset)

        assert type(features) == type([]), "instance_features_test should be a list"

    def test_get_instance_labels_test(self):
        labels = get_instance_labels_test(self.multilabel_dataset)

        assert type(labels) == type([]), "instance_labels_test should be a list"

    def test_get_total_features_test(self):
        features = get_instance_features_test(self.multilabel_dataset)

        assert type(features) == type([]), "total_features_test should be a list"

    def test_get_total_labels_test(self):
        labels = get_total_labels_test(self.multilabel_dataset)

        assert type(labels) == type([]), "total_labels_test should be a list"


if __name__ == '__main__':
    unittest.main()
