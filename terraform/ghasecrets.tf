resource "github_actions_secret" "github-acr-access-app-password" {
  repository       = var.github-repository-name
  secret_name      = var.github-secret-acr-aplication-access-password
  plaintext_value  = azuread_service_principal_password.ACR-access-sp-password.value
  depends_on = [
    azuread_service_principal_password.ACR-access-sp-password
  ]
}

resource "github_actions_secret" "github-docker-server-name" {
  repository       = var.github-repository-name
  secret_name      = var.github-secret-acr-server-login-name
  plaintext_value  = azurerm_container_registry.acr-prod.login_server
  depends_on = [
    azurerm_container_registry.acr-prod
  ]
}

resource "github_actions_secret" "github-acr-access-app-id" {
  repository       = var.github-repository-name
  secret_name      = var.github-secret-acr-aplication-access-id
  plaintext_value  = azuread_application.ACR-access-app.application_id
  depends_on = [
    azuread_application.ACR-access-app
  ]
}