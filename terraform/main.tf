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

resource "google_storage_bucket" "default" {
  name     = "cads-bucket"
  location = "EU"
}

resource "google_service_account" "cads_service_account" {
  account_id   = "cads-instance-sa"
  display_name = "Cads compute instance service account"

}

resource "google_project_iam_binding" "bucket_admin" {
  role = "roles/storage.objectAdmin"
  project = "citric-bee-353709"
  members = [
    "serviceAccount:${google_service_account.cads_service_account.email}"
  ]
}

resource "google_project_iam_binding" "secrets_accessor" {
  role = "roles/secretmanager.secretAccessor"
  project = "citric-bee-353709"
  members = [
    "serviceAccount:${google_service_account.cads_service_account.email}"
  ]
}

resource "google_compute_instance" "default" {
  name         = "cads-instance-1"
  machine_type = "e2-standard-2"
  zone         = "europe-central2-a"
  allow_stopping_for_update = true

  metadata_startup_script = file("${path.module}/startup.sh")

  boot_disk {
    initialize_params {
      image = "projects/ml-images/global/images/c2-deeplearning-pytorch-1-11-xla-v20220316-debian-10"
    }
  }

  network_interface {
    network = "default"

    access_config {
    }
  }

  service_account {
    email  = google_service_account.cads_service_account.email
    scopes = ["cloud-platform"]
  }
}

