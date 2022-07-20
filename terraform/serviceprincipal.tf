data "azuread_client_config" "current" {}

resource "azuread_application" "ACR-application" {
  display_name = var.acr-service-principal-name
}

resource "azuread_application_password" "ACR-application-password" {
  application_object_id = azuread_application.ACR-application.id
  end_date    = "2299-12-31T00:00:00Z"
}

#Output
output "application-passoword-output" {
  value     = azuread_application_password.ACR-application-password.value
  sensitive = true
}
