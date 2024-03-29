variable "rg-terraform" {
    type = string
    default = "rg-projectf-terraform-prod-001"
    description = "Terraform usables resource group name"
}

variable "rg-terraform-location" {
    type = string
    default = "northeurope"
    description = "Terraform usabled resource group location"
}

variable "sa-terraform-prod-state" {
    type = string
    default = "saprojectfstateprod001"
    description = "Storage account with terraform state file in it"
}

variable "sac-terraform-prod-state" {
    type = string
    default = "state-project-f-prod-001"
    description = "Container with terraform state file in it"
}

variable "terraform-prod-state-filenmae" {
    type = string
    default = "projectf-prod-001.tfstate"
    description = "Name of the prod terraform state file"
}

variable "rg-main-app-name" {
    type = string
    default = "rg-projectf-prod-001"
    description = "Main resource group name"
}

variable "rg-main-app-location" {
    type = string
    default = "northeurope"
    description = "Main resource group location"
}

variable "rg-side-app-name" {
    type = string
    default = "rg-projectf-prod-002"
    description = "Side resource group name"
}

variable "rg-side-app-location" {
    type = string
    default = "northeurope"
    description = "Side resource group location"
}

variable "acr-application-access-name" {
    type = string
    default = "TerraformAcrAccess"
    description = "Name of the service principal that will connect to ACR"
}

variable "acr-access-secret-name" {
  type = string
  default = "GHActionsAcrAccessSecret"
  description = "Name of the acr access app secret"
}

variable "GITHUB_TOKEN" {
  type = string
}

variable "github-secret-acr-aplication-access-password" {
    type = string
    default = "SP_PASSWORD"
    description = "Name of the service principal secret"
}

variable "github-secret-acr-aplication-access-id" {
    type = string
    default = "SP_APPID"
    description = "Name of the service principal appid"
}

variable "github-secret-acr-server-login-name" {
    type = string
    default = "DOCKER_SERVER"
    description = "Name of the ACR server"
}

variable "github-repository-name" {
    type = string
    default = "Project-F"
    description = "Repository name"
}

variable "acr-prod-contianer-registry-name" {
  type = string
  default = "acrprojectfprod001"
}