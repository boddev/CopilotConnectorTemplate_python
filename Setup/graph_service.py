from azure.identity import ClientSecretCredential
from msgraph import GraphServiceClient
from typing import Optional
import os

class GraphService:
    """Service for Microsoft Graph API interactions"""
    
    _client: Optional[GraphServiceClient] = None
    
    @classmethod
    @property
    def client(cls) -> GraphServiceClient:
        """Get the GraphServiceClient instance (singleton pattern)"""
        if cls._client is None:
            # Retrieve the Azure AD credentials from environment variables
            client_id = os.getenv("AZURE_CLIENT_ID")
            client_secret = os.getenv("AZURE_CLIENT_SECRET") 
            tenant_id = os.getenv("AZURE_TENANT_ID")
            
            if not all([client_id, client_secret, tenant_id]):
                raise ValueError("Azure AD credentials not found in environment variables")
            
            # Create a ClientSecretCredential using the retrieved credentials
            credential = ClientSecretCredential(tenant_id, client_id, client_secret)
            
            # Initialize the GraphServiceClient with the credential
            cls._client = GraphServiceClient(credential)
        
        return cls._client