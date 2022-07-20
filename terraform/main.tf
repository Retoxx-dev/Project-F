terraform {
  backend "azurerm" {
    resource_group_name  = var.rg-terraform
    storage_account_name = var.sa-terraform-dev-state
    container_name       = var.sac-terraform-dev-state
    key                  = var.terraform-dev-state-filenmae
  }
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "=3.0.0"
    }

    azuread = {
      source  = "hashicorp/azuread"
      version = "~> 2.0.0"
    }
  }
}

provider "azurerm" {
  features {
    key_vault {
      purge_soft_delete_on_destroy = true
    }
  }
}

provider "azuread" {}

