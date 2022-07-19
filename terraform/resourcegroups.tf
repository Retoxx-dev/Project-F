#Create Resource Group
resource "azurerm_resource_group" "rg-projectf-dev-001" {
  name     = "rg-projectf-dev-001"
  location = "northeurope"
}