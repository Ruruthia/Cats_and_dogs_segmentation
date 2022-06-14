"""Project pipelines."""
from typing import Dict

from kedro.pipeline import Pipeline

from .pipelines import data_processing, train_model, evaluate_model


def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from a pipeline name to a ``Pipeline`` object.
    """
    data_processing_pipeline = data_processing.create_pipeline()
    train_model_pipeline = train_model.create_pipeline()
    evaluate_model_pipeline = evaluate_model.create_pipeline()
    evaluate_model_independent_pipeline = evaluate_model.create_pipeline_independent()
    return {"__default__": data_processing_pipeline + train_model_pipeline + evaluate_model_pipeline,
            "data_processing": data_processing_pipeline,
            "train_model": data_processing_pipeline + train_model_pipeline + evaluate_model_pipeline,
            "evaluate_model": evaluate_model_independent_pipeline
            }
