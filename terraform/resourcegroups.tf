data "azurerm_client_config" "current" {}
 
#Create Resource Group
resource "azurerm_resource_group" "rg-projectf-dev-001" {
  name     = var.rg-main-app-name
  location = var.rg-main-app-location
}

#Create Resource Group
resource "azurerm_resource_group" "rg-projectf-dev-002" {
  name     = var.rg-side-app-name
  location = var.rg-side-app-location
  tags = {
    "CreatedBy" = data.azurerm_client_config.current.object_id
  }
}