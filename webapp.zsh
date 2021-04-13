uniqueId=20210405
resourceGroupName="group$uniqueId"
webAppName="webapp$uniqueId"

# Create a webapp
az webapp up \
    --resource-group $resourceGroupName \
    --name $webAppName \
    --sku F1 \
    --verbose
