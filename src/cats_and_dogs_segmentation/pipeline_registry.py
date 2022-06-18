"""Project pipelines."""
from typing import Dict

from kedro.pipeline import Pipeline

from .pipelines import data_processing, train_model, evaluate_model, optimize_hyperparams


def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from a pipeline name to a ``Pipeline`` object.
    """
    data_processing_pipeline = data_processing.create_pipeline()
    train_model_pipeline = train_model.create_pipeline()
    evaluate_model_pipeline = evaluate_model.create_pipeline()
    evaluate_model_independent_pipeline = evaluate_model.create_pipeline_independent()
    optimize_hyperparams_pipeline = optimize_hyperparams.create_pipeline()
    return {"__default__": data_processing_pipeline + train_model_pipeline + evaluate_model_pipeline,
            "data_processing": data_processing_pipeline,
            "train_model": data_processing_pipeline + train_model_pipeline + evaluate_model_pipeline,
            "evaluate_model": data_processing_pipeline + evaluate_model_independent_pipeline,
            "optimize_hyperparams": data_processing_pipeline + optimize_hyperparams_pipeline,
            }
