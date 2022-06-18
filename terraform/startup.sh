#!/bin/bash

cd ~
git clone https://$(gcloud secrets versions access latest --secret github-pat)@github.com/Ruruthia/Cats_and_dogs_segmentation.git
cd Cats_and_dogs_segmentation
git checkout 6-terraform-provisioning