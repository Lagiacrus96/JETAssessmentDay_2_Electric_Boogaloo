# Define the provider
provider "azurerm" {
  features {}
}


# Create a resource group
resource "azurerm_resource_group" "rg" {
    name     = "jetWebsiteRG"
    location = "West Europe"
}

# Create a storage account
resource "azurerm_storage_account" "sa" {
    name                     = "jetwebsitestorage"
    resource_group_name      = azurerm_resource_group.rg.name
    location                 = azurerm_resource_group.rg.location
    account_tier             = "Standard"
    account_replication_type = "LRS"
    account_kind             = "StorageV2"

    static_website {
        index_document = "index.html"
        error_404_document = "404.html"
    }
}
