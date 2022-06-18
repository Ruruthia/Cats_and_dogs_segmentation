"""
This is a boilerplate pipeline 'optimize_hyperparams'
generated using Kedro 0.18.1
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import optimize_hyperparams


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=optimize_hyperparams,
            inputs=["train_dataloader", "val_dataloader", "params:default_config",
                    "params:hyperparams_config", "params:num_epochs", "params:gpus", "params:project"],
            outputs=None,
            name="optimize_hyperparams"
        )
    ])
