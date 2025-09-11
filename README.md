# CopilotConnectorTemplate_python

A Python implementation of a Microsoft Graph Connector API template for integrating external data sources with Microsoft 365 Copilot.

## Overview

This project provides a FastAPI-based web service that enables you to create custom connectors for Microsoft Graph, allowing external data to be indexed and made searchable within Microsoft 365 applications like Copilot.

## Features

- **FastAPI Web Service**: RESTful API endpoints for connector operations
- **Microsoft Graph Integration**: Uses Microsoft Graph SDK for Python
- **Azure AD Authentication**: Secure authentication using client credentials
- **Background Task Processing**: Asynchronous content ingestion workflow
- **Docker Support**: Containerized deployment ready
- **Configurable Schema**: Customizable data schema for external items

## Architecture

The application follows a modular architecture with the following components:

- **Main API** (`main.py`): FastAPI application with three main endpoints
- **Graph Service** (`Setup/graph_service.py`): Microsoft Graph client management
- **Ingestion Workflow** (`ingestion_workflow.py`): ETL pipeline for content processing
- **Background Queue** (`Load/background_queue.py`): Asynchronous task processing
- **Connection Configuration** (`CreateConnection/connection_config.py`): External connection setup
- **Schema Definition** (`Transform/schema_example.py`): Data schema configuration

## API Endpoints

### POST /grantPermissions
Handles admin consent flow for Azure AD permissions. Stores tenant ID and redirects to Microsoft's admin consent URL.

### POST /provisionconnection
Provisions the Graph connector connection for a specific tenant.

### POST /loadcontent
Queues content ingestion as a background task and returns immediately with HTTP 202.

## Prerequisites

- Python 3.11+
- Azure AD App Registration with appropriate Graph permissions
- Microsoft 365 tenant with admin access

## Configuration

1. Copy `.env.txt` to `.env` and configure:
```
AZURE_CLIENT_ID=your-client-id
AZURE_CLIENT_SECRET=your-client-secret
AZURE_TENANT_ID=your-tenant-id
LOG_LEVEL=INFO
```

2. Update `CreateConnection/connection_config.py` with your connection details
3. Modify `Transform/schema_example.py` to match your data schema

## Installation

1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure environment variables
4. Run the application:
```bash
python main.py
```

## Docker Deployment

Build and run using Docker:

```bash
docker build -f Dockerfile.dockerfile -t copilot-connector .
docker run -p 8080:8080 copilot-connector
```

## Data Flow

1. **Extract**: Pull data from external sources (implement in `IngestionWorkflow.extract()`)
2. **Transform**: Convert external data to Graph-compatible format
3. **Load**: Push transformed items to Microsoft Graph

## Customization

- **Data Source**: Implement your data extraction logic in `IngestionWorkflow.extract()`
- **Schema**: Modify `SchemaExample.get_schema()` to match your data structure
- **Transformation**: Update `IngestionWorkflow.transform()` for your data mapping

## Dependencies

Key dependencies include:
- FastAPI for web framework
- Microsoft Graph SDK for Python
- Azure Identity for authentication
- Uvicorn for ASGI server
- Python-dotenv for environment management

## Development

The project uses async/await patterns throughout for optimal performance with I/O operations. Background task processing ensures the API remains responsive during long-running ingestion operations.

## License

[Add your license information here]

## Contributing

[Add contribution guidelines here]
