data "azuread_client_config" "current" {}

resource "azuread_application" "ACR-service-principal" {
  display_name = var.acr-service-principal-name
  owners       = [data.azuread_client_config.current.object_id]
}

resource "azuread_service_principal_password" "ACR-service-principal-password" {
  display_name         = var.acr-service-principal-password-name
  service_principal_id = azuread_application.ACR-service-principal.id
  end_date    = "2022-09-01T00:00:00Z"
  value                = random_string.service-principal-password.result
}

#Random string - create SP password
resource "random_string" "service-principal-password" {
  length  = 64
  special = true
}

#Output
output "service-principal-passoword-output" {
  value     = azuread_service_principal_password.ACR-service-principal-password.value
  sensitive = true
}
