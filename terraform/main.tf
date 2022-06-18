terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "4.25.0"
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
  name = "cads-persistent-disk"
  type = "pd-balanced"
  zone = "europe-central2-a"
  size = 100
}

resource "google_compute_instance" "default" {
  name                    = "cads-instance-1"
  machine_type            = "e2-standard-2"
  zone                    = "europe-central2-a"
  metadata_startup_script = file("${path.module}/startup.sh")

  boot_disk {
    initialize_params {
      image = "projects/ml-images/global/images/c2-deeplearning-pytorch-1-11-xla-v20220316-debian-10"
    }
  }

  attached_disk {
    source      = google_compute_disk.default.self_link
    mode        = "READ_WRITE"
    device_name = "cads-disk"
  }

  network_interface {
    network = "default"

    access_config {

    }
  }
}

