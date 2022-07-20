data "azuread_client_config" "current" {}

#Random string - create SP password
resource "random_string" "application-password" {
  length  = 32
  special = true
}

resource "azuread_application" "ACR-application" {
  display_name = var.acr-service-principal-name
  owners       = [data.azuread_client_config.current.object_id]
}

resource "azuread_application_password" "ACR-application-password" {
  application_object_id = azuread_application.ACR-application.id
  value                = random_string.application-password.result
  end_date    = "2299-12-31T00:00:00Z"
}

#Output
output "application-passoword-output" {
  value     = azuread_application_password.ACR-application-password.value
  sensitive = true
}
