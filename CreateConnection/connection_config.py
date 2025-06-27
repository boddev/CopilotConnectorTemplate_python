from msgraph.generated.models.external_connectors.external_connection import ExternalConnection
from msgraph.generated.models.external_connectors.configuration import Configuration

class ConnectionConfiguration:
    """Configuration for external connection"""
    
    @staticmethod
    def get_external_connection() -> ExternalConnection:
        """Returns the external connection configuration"""
        return ExternalConnection(
            id="your-connection-id",  # Replace with your connection ID
            name="Your Connection Name",
            description="Your connection description",
            configuration=Configuration(
                # Add configuration properties as needed
            )
        )
    
    external_connection = get_external_connection()