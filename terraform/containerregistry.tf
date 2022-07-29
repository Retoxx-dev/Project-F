resource "azurerm_container_registry" "acr-dev" {
  name                = var.acr-dev-contianer-registry-name
  resource_group_name = azurerm_resource_group.rg-projectf-dev-002.name
  location            = azurerm_resource_group.rg-projectf-dev-002.location
  sku                 = "Standard"
  admin_enabled       = false
  tags = {
    "CreatedBy" = data.azurerm_client_config.current.object_id
  }
}

resource "azurerm_role_assignment" "acr-role-assignment-dev" {
  principal_id                     = data.azuread_service_principal.data-ACR-access-app-service-principal.id
  role_definition_name             = "AcrPush"
  scope                            = azurerm_container_registry.acr-dev.id
  skip_service_principal_aad_check = true
}