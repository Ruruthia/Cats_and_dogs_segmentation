#!/bin/bash

mkdir /home/pets_dl_project
cd /home/pets_dl_project
git clone https://$(gcloud secrets versions access latest --secret github-pat)@github.com/Ruruthia/Cats_and_dogs_segmentation.git
cd Cats_and_dogs_segmentation
git checkout 6-terraform-provisioning