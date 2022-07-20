resource "github_actions_secret" "service-principal-password-github-secret" {
  repository       = var.github-repository-name
  secret_name      = var.service-principal-github-secret-name
  plaintext_value  = azuread_service_principal_password.ACR-service-principal-password.value
}