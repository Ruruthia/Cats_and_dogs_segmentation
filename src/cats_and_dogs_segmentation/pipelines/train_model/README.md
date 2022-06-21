# Pipeline train_model

## Overview

This pipeline is handling training of a model.

## Pipeline inputs
Following inputs are supplied from the parameters file or previous pipelines:
train_dataloader, val_dataloader (from data_processing pipeline)
params:config
params:num_epochs
params:gpus 
params:project
params:checkpoints_dir_path

Their meaning is documented in the nodes.py file.

## Pipeline outputs

The pipeline outputs the path of the checkpoint of model with the best validation accuracy.