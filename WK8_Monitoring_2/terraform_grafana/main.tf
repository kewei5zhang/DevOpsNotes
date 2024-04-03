resource "grafana_folder" "terraform" {
  title = "Managed by Terraform"
}

resource "grafana_dashboard" "terraform" {
  folder      = grafana_folder.terraform.uid
  config_json = file("app_health.json")
}
