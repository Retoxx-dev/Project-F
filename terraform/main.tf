terraform {
  backend "azurerm" {
    resource_group_name  = "rg-projectf-terraform-dev-001"
    storage_account_name = "saprojectfstatedev001"
    container_name       = "state-project-f-dev-001"
    key                  = "projectfdev.tfstate"
  }
}
 
provider "azurerm" {
  version = "~>2.0"
  features {}
}
 
data "azurerm_client_config" "current" {}
 
#Create Resource Group
resource "azurerm_resource_group" "rg-test" {
  name     = "rg-projectf-dev-001"
  location = "northeurope"
}