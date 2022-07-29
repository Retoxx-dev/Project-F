terraform {
  backend "azurerm" {
    resource_group_name  = "rg-projectf-terraform-dev-001"
    storage_account_name = "saprojectfstatedev001"
    container_name       = "state-project-f-dev-001"
    key                  = "projectf-dev-001.tfstate"
  }
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "=3.0.0"
    }

    azuread = {
      source  = "hashicorp/azuread"
      version = "=2.6.0"
    }

    github = {
      source = "integrations/github"
      version = "~> 4.0"
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

provider "github" {
  token = var.GITHUB_TOKEN
}

