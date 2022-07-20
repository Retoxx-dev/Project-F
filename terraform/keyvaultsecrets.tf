resource "azurerm_key_vault_secret" "ACR-access-app-password-akv-secret" {
  name         = var.acr-application-access-secret-name
  value        = data.azuread_application_password.ACR-access-app-password.value
  key_vault_id = azurerm_key_vault.akv-terraform-secrets.id
}