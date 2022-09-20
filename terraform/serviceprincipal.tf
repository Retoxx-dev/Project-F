data "azuread_client_config" "current" {}

resource "azuread_application" "ACR-access-app" {
  display_name = var.acr-application-access-name
}

resource "azuread_service_principal" "ACR-access-sp" {
  application_id = azuread_application.ACR-access-app.application_id
}

resource "azuread_service_principal_password" "ACR-access-sp-password" {
  service_principal_id = azuread_service_principal.ACR-access-sp.id
  end_date    = "2022-12-30T01:02:03Z"
}

data "azuread_service_principal" "data-ACR-access-service-principal" {
  application_id = azuread_service_principal.ACR-access-sp.id
}