# Cats_and_dogs_segmentation

## Task

The goal of the project is to deliver a deep-learning, instance segmentation model for an open-source dataset of Oxford Pets.

The project consists of a training and evaluation scripts wrapped with Kedro project. 
Additionally, the project is prepared to be run on Google Cloud Platform, where it can be provisioned using Terraform.

The summary of experiments can be found in `docs/summary.md`.

## Overview

This is your new Kedro project, which was generated using `Kedro 0.18.1`.

Take a look at the [Kedro documentation](https://kedro.readthedocs.io) to get started.

## How to install dependencies

Declare any dependencies in `src/environment.yml` for `conda` installation.

To install them, run:

```
conda env create -f src/environment.yml
```

## How to run your Kedro pipeline

You can run your Kedro project with:

```
kedro run
```

## Available pipelines

Four pipelines are available:
- `data_processing`
- `train_model`
- `evaluate_model`
- `optimize_hyperparams`

Each of them is described in greater details in its corresponding README, which can be found in `src/pipelines/pipeline_name` directory.

## Running on the GCP

To run the model on Google Cloud Platform:

1. Install Terraform, make an account and project on GCP
2. Add credentials to enable access to GCP by Terraform to `conf/local`. Add your credentials to WandB to GCP Secret Manager.
3. Change project name and credentials path in the `terraform/main.tf` file to the ones you created in steps 1. and 2. 
4. Run `terraform apply` locally. It should build the whole project from scratch.
5. When it is ready, SSH to your new VM through GCP interface. The repository with code should already be available. 
Run `. setup.sh` to setup conda environment and log to WandB.
6. Now, you can run Kedro pipelines in the Cloud! 
If you want to store model checkpoints in Cloud Storage remember to set correct value to `checkpoints_dir_path` parameter.
7. After finishing work, run `terraform destroy` to destroy all the provisioned resources. 
If your Cloud Storage bucket is not empty, it **will not** be deleted.

Unfortunately, the machines with GPUs are unavailable when using free GCP trial, so we were not able to experiment with multi-GPU computations.