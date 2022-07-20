data "azuread_client_config" "current" {}

resource "azuread_application" "ACR-access-app" {
  display_name = var.acr-application-access-name
}

resource "azuread_application_password" "ACR-access-app-password" {
  display_name         = var.acr-application-access-secret-name
  application_object_id = azuread_application.ACR-access-app.id
  end_date    = "2022-09-01T01:02:03Z"
}

#Output
output "service-principal-passoword-output" {
  value     = azuread_application_password.ACR-access-app-password.value
  sensitive = true
}
