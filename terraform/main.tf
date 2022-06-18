terraform {
  required_providers {
    google = {
      source = "hashicorp/google"
      version = "3.5.0"
    }
  }
}

provider "google" {
  credentials = file("../conf/local/citric-bee-353709-db31daa193e1.json")

  project = "citric-bee-353709"
  region  = "europe-central2"
  zone    = "europe-central2-a"
}

resource "google_compute_disk" "default" {
  name  = "cads-persistent-disc"
  type  = "pd-balanced"
  zone  = "europe-central2-a"
  size = 100
}

