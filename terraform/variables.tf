variable "rg-main-app-name" {
    type = string
    description = "Main resource group name"
}

variable "rg-main-app-location" {
    type = string
    description = "Main resource group location"
}

variable "acr-service-principal-name" {
    type = string
    description = "Name of the service principal that will connect to ACR"
}

variable "acr-service-principal-password-name" {
    type = string
    description = "Name of the service principal secret"
}

variable "github-repository-name" {
    type = string
    description = "Github's repository name"
}

variable "service-principal-github-secret-name" {
    type = string
    description = "Name of the github actions secret"
}

variable "GITHUB_TOKEN" {
    type = "string"
    description = "Github token"
}