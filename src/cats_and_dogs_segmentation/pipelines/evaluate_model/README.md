# Pipeline evaluate_model

## Overview

This pipeline is handling evaluation of a model, either produced by train_model pipeline or loaded from checkpoint.

## Pipeline inputs

Following inputs are supplied from the parameters file or previous pipelines:
test_dataloader (from data_processing pipeline)
model_path (from train_model pipeline) or params:model_path
params:gpus
params:project

Their meaning is documented in the nodes.py file.

## Pipeline outputs

The pipeline does not output anything, but it logs the results of evaluation to stdout and wandb.