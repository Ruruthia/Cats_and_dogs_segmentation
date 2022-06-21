# Pipeline data_processing

## Overview

This pipeline is handling downloading and transforming the Oxford Pets data.

## Pipeline inputs

Following inputs are supplied from the parameters file:
params:raw_data_filepath
params:val_ratio
params:test_ratio 
params:seed
params:batch_size 
params:num_workers

Their meaning is documented in the nodes.py file.

## Pipeline outputs

The pipeline outputs prepared data in form of following Dataloaders: train_dataloader, val_dataloader and test_dataloader.
