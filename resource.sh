uniqueId=20210405
resourceGroupName="group$uniqueId"
location='westus2'
sqlServerName="sqlserver$uniqueId"
sqlDatabaseName="sqldb$uniqueId"
storageAccountName="blob$uniqueId" 
containerName='images'
clientIP=$(curl ifconfig.me)
echo $clientIP

# Create a resource group
az group create \
    --name $resourceGroupName \
    --location $location

# Create a SQL server
az sql server create \
    --location $location \
    --resource-group $resourceGroupName \
    --name $sqlServerName \
    --admin-user dbadmin \
    --admin-password p@ssword1234 \
    --enable-public-network true \
    --verbose

# Create the firewall rule
az sql server firewall-rule create \
    --resource-group $resourceGroupName \
    --server $sqlServerName \
    --name azureaccess \
    --start-ip-address 0.0.0.0 \
    --end-ip-address 0.0.0.0 \
    --verbose

az sql server firewall-rule create \
    --resource-group $resourceGroupName \
    --server $sqlServerName \
    --name clientip \
    --start-ip-address $clientIP \
    --end-ip-address $clientIP \
    --verbose

# Create a SQL database
az sql db create \
    --name $sqlDatabaseName \
    --resource-group $resourceGroupName \
    --server $sqlServerName \
    --tier Basic \
    --verbose

# Create a storage account
az storage account create \
    --name $storageAccountName \
    --resource-group $resourceGroupName \
    --location $location

# Create a storage container
az storage container create \
    --account-name $storageAccountName \
    --name $containerName \
    --public-access container

# # Create a webapp
# az webapp up \
#     --resource-group $resourceGroupName \
#     --name webapp20210405 \
#     --sku F1 \
#     --verbose

