resource "azurerm_key_vault" "akv-terraform-secrets" {
  name                        = var.akv-terraform-usables-name
  location                    = var.rg-terraform-location
  resource_group_name         = var.rg-terraform
  enabled_for_disk_encryption = true
  tenant_id                   = data.azurerm_client_config.current.tenant_id
  soft_delete_retention_days  = 7
  purge_protection_enabled    = false
  sku_name = "standard"
  tags = {
    "CreatedBy" = data.azurerm_client_config.current.object_id
  }

  access_policy {
    tenant_id = data.azurerm_client_config.current.tenant_id
    object_id = data.azurerm_client_config.current.object_id

    secret_permissions = [
        "Get",
        "Set"
    ]
  }
}