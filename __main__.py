from src.multilabel.pipeline.multilabel_pipeline import MultilabelPipelineFactoryArgument, multilabel_pipeline_factory, execute_multilabel_pipeline

argument_obj = MultilabelPipelineFactoryArgument()
argument_obj.dataset = "emotions"
argument_obj.problem_transformer = "binary_relevance"
argument_obj.feature_selector = "mutual_information"
argument_obj.feature_filter = "select_k_best"
argument_obj.num_of_selected_features = 36
argument_obj.classifier = "decision_tree"

create_pipeline = multilabel_pipeline_factory(argument_obj)
results = execute_multilabel_pipeline(create_pipeline)

print("results: ", results)