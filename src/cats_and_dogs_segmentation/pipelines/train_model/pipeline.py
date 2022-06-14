"""
This is a boilerplate pipeline 'train_model'
generated using Kedro 0.18.1
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import train


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=train,
            inputs=["train_data_loader", "val_data_loader", "params:config",
                    "params:num_epochs", "params:gpus", "params:project"],
            outputs="model_path",
            name="train_model"
        )
    ])
