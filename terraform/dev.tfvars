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

variable "acr-service-principal-name" {
    type = string
    default = "GithubActionsAcrAccess"
    description = "Name of the service principal that will connect to ACR"
}

variable "acr-service-principal-password-name" {
    type = string
    default = "GithubActionsAcrAccessSecret"
    description = "Name of the service principal secret"
}

variable "github-repository-name" {
    type = string
    default = "Project-F"
    description = "Github's repository name"
}

variable "service-principal-github-secret-name" {
    type = string
    default = "GithubActionsAcrAccessSecret"
    description = "Name of the github actions secret"
}