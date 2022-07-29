resource "github_actions_secret" "example_secret" {
  repository       = var.github-repository-name
  secret_name      = var.github-secret-acr-aplication-access
  plaintext_value  = azuread_application_password.ACR-access-app-password.value
  depends_on = [
    azuread_application_password.ACR-access-app-password
  ]
}