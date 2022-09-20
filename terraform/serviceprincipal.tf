data "azuread_client_config" "current" {}

resource "azuread_application" "ACR-access-app" {
  display_name = var.acr-application-access-name
}

resource "azuread_service_principal" "ACR-access-sp" {
  application_id               = azuread_application.ACR-access-app.application_id
  app_role_assignment_required = false
}

resource "azuread_application_password" "ACR-access-app-password" {
  display_name         = var.acr-access-secret-name
  application_object_id = azuread_application.ACR-access-app.id
  end_date    = "2022-09-01T01:02:03Z"
}

data "azuread_service_principal" "data-ACR-access-service-principal" {
  application_id = azuread_service_principal.ACR-access-sp.id
}