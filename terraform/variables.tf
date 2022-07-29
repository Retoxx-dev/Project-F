variable "rg-terraform" {
    type = string
    default = "rg-projectf-terraform-dev-001"
    description = "Terraform usables resource group name"
}

variable "rg-terraform-location" {
    type = string
    default = "northeurope"
    description = "Terraform usabled resource group location"
}

variable "sa-terraform-dev-state" {
    type = string
    default = "saprojectfstatedev001"
    description = "Storage account with terraform state file in it"
}

variable "sac-terraform-dev-state" {
    type = string
    default = "state-project-f-dev-001"
    description = "Container with terraform state file in it"
}

variable "terraform-dev-state-filenmae" {
    type = string
    default = "projectf-dev-001.tfstate"
    description = "Name of the dev terraform state file"
}



variable "rg-main-app-name" {
    type = string
    default = "rg-projectf-dev-001"
    description = "Main resource group name"
}

variable "rg-main-app-location" {
    type = string
    default = "northeurope"
    description = "Main resource group location"
}

variable "acr-application-access-name" {
    type = string
    default = "TerraformAcrAccess"
    description = "Name of the service principal that will connect to ACR"
}

variable "GITHUB_TOKEN" {
  type = string
}

variable "github-secret-acr-aplication-access" {
    type = string
    default = "AcrAccessSecret"
    description = "Name of the service principal secret"
}

variable "github-repository-name" {
  type = string
    default = "Project-F"
}