"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.18.1
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import download_and_transform_data, split_data, prepare_dataloaders


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=download_and_transform_data,
            inputs=["params:raw_data_filepath"],
            outputs="pets_dataset",
            name="download_and_transform_data_node"
        ),
        node(
            func=split_data,
            inputs=["pets_dataset", "params:val_ratio", "params:test_ratio", "params:seed"],
            outputs="pets_dataset_splits",
            name="split_data_node"
        ),
        node(
            func=prepare_dataloaders,
            inputs=["pets_dataset_splits", "params:batch_size", "params:num_workers"],
            outputs=["train_dataloader", "val_dataloader", "test_dataloader"],
            name="prepare_dataloaders_node"

        )
    ])
