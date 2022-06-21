# Pipeline optimize_hyperparams

## Overview

This pipeline is handling optimization of model's hyperparameters.

## Pipeline inputs

Following inputs are supplied from the parameters file or previous pipelines:
train_dataloader, val_dataloader (from data_processing pipeline)
params:default_config
params:hyperparams_config
params:num_epochs
params:gpus 
params:project 
params:checkpoints_dir_path

Their meaning is documented in the nodes.py file.

## Pipeline outputs

The pipeline does not output anything, but it logs the results of optimization to stdout and wandb.