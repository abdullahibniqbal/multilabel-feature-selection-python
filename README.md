# multilabel-feature-selection
This is a customizable pipeline for multilabel classification and feature selection.

To import the project, perform the following:
1. Git clone / download the project.
2. Go to the root folder.
3. Run "pip install -r requirements.txt".

To run the main file, go to the root folder and execute:
> python __main__.py

**Python version used**: 3.7.6

**Pip version used**: 20.0.2

## Creating and executing pipelines

Pipelines can be created and executed as follows:

```
from multilabel.problem_transformation.multilabel_pipeline import multilabel_pipeline_factory, execute_multilabel_pipeline

create_pipeline = multilabel_pipeline_factory(
    dataset="emotions", 
    problem_transformer="binary_relevance", 
    feature_selector="mutual_information", 
	feature_filter="select_k_best", 
    classifier="decision_tree"
)
results = execute_multilabel_pipeline(create_pipeline)

print("results: ", results)
```

Parameters to multilabel_pipeline_factory are as follows:

**dataset_name**

Datasets are taken from skmultilearn.datasets. Following datasets are available:
1. tmc2007_500
2. birds
3. yeast
4. bibtex
5. rcv1subset3
6. rcv1subset5
7. rcv1subset4
8. genbase
9. rcv1subset1
10. rcv1subset2
11. Corel5k
12. enron
13. emotions
14. medical
15. delicious
16. scene
17. mediamill

**problem_transformer**
This is the name of the Problem Transformation algorithm. Currently only one algorithm is available:
1. binary_relevance

**feature_selector**
This is the name of the Feature Selection algorithm. Currently the following feature selectors are available:
Scorers:
1. mutual_information
2. f_classif

**feature_filter**
Currently the following filter method is available:
1. select_k_best

**classifier**
This is the name of the classifier. Following classifiers are available:
1. decision_tree
2. linear_regression
3. naive_bayes
4. random_forest
5. svm

multilabel_pipeline_factory returns a create function which creates the elements of the pipeline.

##  Creating custom pipelines

multilabel_pipeline_factory returns a curried function. It returns the following tuple:
```
([dataset_training, dataset_testing], select_features, transform_problem, classifier)
```

1. **[training_set, testing_set]** - Training and testing sets. Their structure is the same as of skmultilearn.
2. **select_features** - this is a function that takes a dataset and returns a new dataset after selecting features
3. **transform_problem** - this is a function that takes a classifier and datasets [1] as input, and outputs the classification results.
4. **classifier** - this is a classifier which is used by transform_problem function [3].

To customize parts parts of the pipeline, create your own factory method. Following is an example:
###### Creating custom factory method
```
def custom_factory_method():
    def create_pipeline():
        return [custom_dataset, custom_select_features, custom_transform_problem, custom_classifier]
```
Each of the items in return type of create_pipeline need not be custom. You can import any of them from packages in this folder and pass them here for default implementations. For example:
```
from skmultilearn.dataset import load_datasets

from feature_selectors.feature_selector import feature_selector
from problem_transformation.impls.binary_relevance import transform_problem
from classifiers.impls.decision_tree import DecisionTree

def custom_factory_method():
    def create_pipeline():
        dataset_training = load_dataset("emotions", "training")
        dataset_testing = load_dataset("emotions", "testing")
    
        return [[dataset_training, dataset_testing], feature_selector, transform_problem, DecisionTree]
```
To provide your own parts to the pipeline, see the following examples ([path to package.module name]):
- [x] *select_features* => **feature_selectors.feature_selector.py**
- [x] *problem_transformer* => **problem_transformation.impls.binary_relevance.py**
- [x] *classifier* => **classifiers.impls.decision_tree.py**

