#!/bin/bash

conda env create -f src/environment.yml -n cads
conda activate cads
wandb login $(gcloud secrets versions access latest --secret wandb)