#!/bin/bash

git clone https://$(gcloud secrets versions access latest --secret github-pat)@github.com/Ruruthia/Cats_and_dogs_segmentation.git
cd Cats_and_dogs_segmentation
conda env create -f src/environment.yml -n cads
conda activate cads
wandb login $(gcloud secrets versions access latest --secret wandb)