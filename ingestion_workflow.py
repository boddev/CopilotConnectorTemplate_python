import asyncio
from typing import List, Dict, Any
from urllib.parse import quote
from msgraph.generated.models.external_connectors.external_item import ExternalItem
from setup.graph_service import GraphService
from connection.connection_configuration import ConnectionConfiguration

class IngestionWorkflow:
    """Workflow for ingesting content into Microsoft Graph"""
    
    # Static lists to hold content and transformed items
    content: List[Dict[str, Any]] = []
    items: List[ExternalItem] = []
    
    @staticmethod
    async def extract():
        """Extract data from external service"""
        # Populate the content list with data from the External Service
        # This is where you would implement your data extraction logic
        pass
    
    @staticmethod
    def transform(item: Dict[str, Any]) -> ExternalItem:
        """Transform external item to ExternalItem format"""
        # Create a new ExternalItem object and populate its properties
        external_item = ExternalItem(
            # This is an example layout of how you can transform the item
            # The fields being set have to match 1:1 with the schema defined in SchemaExample
            # id=item.get("Id"),
            # additional_data={
            #     "Url": item.get("Url"),
            #     "IconUrl": item.get("IconUrl"), 
            #     "Title": item.get("Title"),
            #     "Company": item.get("Company"),
            #     "Form": item.get("Form"),
            #     "DateFiled": item.get("DateFiled")
            # }
        )
        
        # Add the transformed item to the items list
        IngestionWorkflow.items.append(external_item)
        return external_item
    
    @staticmethod
    async def load():
        """Load items into Microsoft Graph"""
        # Iterate over each item in the items list
        for item in IngestionWorkflow.items:
            print(f"Loading item {item.id}...", end="")
            try:
                # Put the item into the GraphService client
                connection_id = quote(ConnectionConfiguration.external_connection.id)
                await GraphService.client.external.connections.by_external_connection_id(
                    connection_id
                ).items.by_external_item_id(item.id).put(item)
                
                print("DONE")
                
                # Get the URL from the item's additional_data dictionary
                if item.additional_data and "Url" in item.additional_data:
                    url = item.additional_data["Url"]
                    # Do something with the URL if needed
                    
            except Exception as ex:
                # Output an error message if an exception occurs
                print("ERROR")
                print(f"Error loading item: {ex}")
    
    @staticmethod
    async def load_content():
        """Main method to load content - calls Extract, Transform, and Load"""
        # Call the Extract method to populate the content list
        await IngestionWorkflow.extract()
        
        # Iterate over each item in the content list and transform it
        for item in IngestionWorkflow.content:
            IngestionWorkflow.transform(item)
        
        # Call the Load method to load the transformed items
        await IngestionWorkflow.load()