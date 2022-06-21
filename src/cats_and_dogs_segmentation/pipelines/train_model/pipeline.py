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
            inputs=["train_dataloader", "val_dataloader", "params:config",
                    "params:num_epochs", "params:gpus", "params:project", "params:checkpoints_dir_path"],
            outputs="model_path",
            name="train_model"
        )
    ])
