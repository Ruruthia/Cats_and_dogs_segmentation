#!/bin/bash

sudo chown -R pets_dl_project /home/pets_dl_project
source /opt/conda/etc/profile.d/conda.sh
conda env create -f src/environment.yml -n cads
conda activate cads
wandb login $(gcloud secrets versions access latest --secret wandb)
