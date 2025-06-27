from msgraph.generated.models.external_connectors.schema import Schema
from msgraph.generated.models.external_connectors.property import Property
from msgraph.generated.models.external_connectors.property_type import PropertyType
from msgraph.generated.models.external_connectors.label import Label

class SchemaExample:
    """Example schema definition for external items"""
    
    @staticmethod
    def get_schema() -> Schema:
        """Return a new Schema object with predefined properties"""
        # Labels Title, Url and IconUrl are required for Copilot usage
        return Schema(
            base_type="microsoft.graph.externalItem",
            properties=[
                Property(
                    name="Title",
                    type=PropertyType.String,
                    is_queryable=True,
                    is_searchable=True,
                    is_retrievable=True,
                    labels=[Label.Title]
                ),
                Property(
                    name="Company", 
                    type=PropertyType.String,
                    is_retrievable=True,
                    is_searchable=True,
                    is_queryable=True
                ),
                Property(
                    name="Url",
                    type=PropertyType.String,
                    is_retrievable=True,
                    labels=[Label.Url]
                ),
                Property(
                    name="IconUrl",
                    type=PropertyType.String,
                    is_retrievable=True,
                    labels=[Label.IconUrl]
                ),
                Property(
                    name="Form",
                    type=PropertyType.String,
                    is_retrievable=True,
                    is_searchable=True,
                    is_queryable=True
                ),
                Property(
                    name="DateFiled",
                    type=PropertyType.DateTime,
                    is_retrievable=True,
                    is_searchable=True,
                    is_queryable=True,
                    labels=[Label.CreatedDateTime]
                )
            ]
        )