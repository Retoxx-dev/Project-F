terraform {
  backend "azurerm" {
    resource_group_name  = "rg-projectf-terraform-dev-001"
    storage_account_name = "saprojectfstatedev001"
    container_name       = "state-project-f-dev-001"
    key                  = "projectf-dev-001.tfstate"
  }
}

provider "azurerm" {
  version = "3.14.0"
  features {}
}

data "azurerm_client_config" "current" {}