data "github_repository" "main-repo" {
  full_name = var.github-repository-name
}
resource "github_actions_secret" "service-principal-password-github-secret" {
  repository       = data.github_repository.main-repo.name
  secret_name      = var.service-principal-github-secret-name
  plaintext_value  = azuread_application_password.ACR-application-password.value
}