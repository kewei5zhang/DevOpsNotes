terraform {
  required_providers {
    grafana = {
      source  = "grafana/grafana"
      version = "2.12.1"
    }
  }
}

provider "grafana" {
  url  = "http://localhost:3000"
  auth = var.grafana_auth
}