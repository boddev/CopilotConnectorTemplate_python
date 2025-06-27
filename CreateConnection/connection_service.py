import logging
from setup.graph_service import GraphService
from connection.connection_configuration import ConnectionConfiguration
from transform.schema_example import SchemaExample

class ConnectionService:
    """Service for managing external connections"""
    
    @staticmethod
    async def create_connection():
        """Create a new external connection"""
        print("Creating connection...", end="")
        
        # Post a new connection to the GraphService client
        await GraphService.client.external.connections.post(
            ConnectionConfiguration.external_connection
        )
        
        print("DONE")
    
    @staticmethod
    async def create_schema():
        """Create schema for the connection"""
        print("Creating schema...")
        
        # Patch the schema for the specified connection
        connection_id = ConnectionConfiguration.external_connection.id
        await GraphService.client.external.connections.by_external_connection_id(
            connection_id
        ).schema.patch(SchemaExample.get_schema())
        
        print("DONE")
    
    @staticmethod
    async def provision_connection():
        """Provision connection by creating connection and schema"""
        try:
            # Attempt to create a connection
            await ConnectionService.create_connection()
            # Attempt to create a schema
            await ConnectionService.create_schema()
        except Exception as ex:
            # Log any exceptions that occur
            print(f"Error provisioning connection: {ex}")
            raise