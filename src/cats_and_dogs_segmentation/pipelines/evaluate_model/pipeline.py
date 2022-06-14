"""
This is a boilerplate pipeline 'evaluate_model'
generated using Kedro 0.18.1
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import evaluate


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=evaluate,
            inputs=["test_data_loader", "model_path", "params:gpus", "params:project"],
            outputs=None,
            name="evaluate_model"
        ),
    ])


def create_pipeline_independent(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=evaluate,
            inputs=["test_data_loader", "params:model_path", "params:gpus", "params:project"],
            outputs=None,
            name="evaluate_model"
        ),
    ])
