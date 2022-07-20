data "azurerm_client_config" "current" {}
 
#Create Resource Group
resource "azurerm_resource_group" "rg-projectf-dev-001" {
  name     = var.rg-main-app-name
  location = var.rg-main-app-location
}