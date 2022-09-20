resource "azurerm_container_registry" "acr-prod" {
  name                = var.acr-prod-contianer-registry-name
  resource_group_name = azurerm_resource_group.rg-projectf-prod-002.name
  location            = azurerm_resource_group.rg-projectf-prod-002.location
  sku                 = "Standard"
  admin_enabled       = false
  tags = {
    "CreatedBy" = data.azurerm_client_config.current.object_id
  }
}

resource "azurerm_role_assignment" "acr-role-assignment-prod" {
  principal_id                     = azuread_service_principal_password.ACR-access-sp-password.service_principal_id
  role_definition_name             = "AcrPush"
  scope                            = azurerm_container_registry.acr-prod.id
  skip_service_principal_aad_check = true
}