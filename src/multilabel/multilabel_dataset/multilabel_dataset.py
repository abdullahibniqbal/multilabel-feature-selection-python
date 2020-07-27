from pandas import DataFrame

DATASET_TRAINING = "train"
DATASET_TESTING = "test"
TOTAL_LABELS = 3
TOTAL_FEATURES = 2
INSTANCE_LABELS = 1
INSTANCE_FEATURES = 0


def get_instance_features_test(multilabel_dataset):
    dataset_training = multilabel_dataset[DATASET_TESTING]

    return dataset_training[INSTANCE_FEATURES]


def get_instance_labels_test(multilabel_dataset):
    dataset_training = multilabel_dataset[DATASET_TESTING]

    return dataset_training[INSTANCE_LABELS]


def get_total_features_test(multilabel_dataset):
    dataset_training = multilabel_dataset[DATASET_TESTING]

    return dataset_training[TOTAL_FEATURES]


def get_total_labels_test(multilabel_dataset):
    dataset_training = multilabel_dataset[DATASET_TESTING]

    return dataset_training[TOTAL_LABELS]


def get_instance_features_train(multilabel_dataset):
    dataset_training = multilabel_dataset[DATASET_TRAINING]

    return dataset_training[INSTANCE_FEATURES]


def get_instance_labels_train(multilabel_dataset):
    dataset_training = multilabel_dataset[DATASET_TRAINING]

    return dataset_training[INSTANCE_LABELS]


def get_total_features_train(multilabel_dataset):
    dataset_training = multilabel_dataset[DATASET_TRAINING]

    return dataset_training[TOTAL_FEATURES]


def get_total_labels_train(multilabel_dataset):
    dataset_training = multilabel_dataset[DATASET_TRAINING]

    return dataset_training[TOTAL_LABELS]


def set_instance_features_train(multilabel_dataset, features):
    dataset_training = multilabel_dataset[DATASET_TRAINING]
    dataset_training[INSTANCE_FEATURES] = features

    return multilabel_dataset

def set_instance_features_test(multilabel_dataset, features):
    dataset_test = multilabel_dataset[DATASET_TESTING]
    dataset_test[INSTANCE_FEATURES] = features

    return multilabel_dataset


def set_instance_labels_train(multilabel_dataset, labels):
    dataset_training = multilabel_dataset[DATASET_TRAINING]
    dataset_training[INSTANCE_LABELS] = labels

    return multilabel_dataset


def set_total_features_train(multilabel_dataset, features):
    dataset_training = multilabel_dataset[DATASET_TRAINING]
    dataset_training[TOTAL_FEATURES] = features

    return multilabel_dataset


def set_total_features_test(multilabel_dataset, features):
    dataset_testing = multilabel_dataset[DATASET_TESTING]
    dataset_testing[TOTAL_FEATURES] = features

    return multilabel_dataset


def sparse_matrix_to_list(sparse_matrix):
    list_of_numpy_arrays = list(sparse_matrix)
    list_of_lists = list(map(lambda numpy_array: numpy_array.toarray()[0], list_of_numpy_arrays))

    return list_of_lists


def list_of_tuples_to_list_of_lists(list_of_tuples):
    return list(map(lambda tuple: [tuple[0], tuple[1]], list_of_tuples))


def cons_multilabel_dataset(dataset_train, dataset_test):
    return {
        "train": [
            sparse_matrix_to_list(dataset_train[INSTANCE_FEATURES]),
            sparse_matrix_to_list(dataset_train[INSTANCE_LABELS]),
            list_of_tuples_to_list_of_lists(dataset_train[TOTAL_FEATURES]),
            list_of_tuples_to_list_of_lists(dataset_train[TOTAL_LABELS])
        ],
        "test": [
            sparse_matrix_to_list(dataset_test[INSTANCE_FEATURES]),
            sparse_matrix_to_list(dataset_test[INSTANCE_LABELS]),
            list_of_tuples_to_list_of_lists(dataset_test[TOTAL_FEATURES]),
            list_of_tuples_to_list_of_lists(dataset_test[TOTAL_LABELS])
        ]
    }


def cons_multilabel_dataset_mock(dataset):
    return dataset