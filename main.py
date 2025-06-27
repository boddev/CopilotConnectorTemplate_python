import asyncio
import os
from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException, Request, status, BackgroundTasks
from fastapi.responses import RedirectResponse
import logging
from typing import Optional
from dotenv import load_dotenv

from services.logging_service import LoggingService
from services.background_task_queue import BackgroundTaskQueue
from workflows.ingestion_workflow import IngestionWorkflow
from connection.connection_service import ConnectionService

# Load environment variables
load_dotenv()

# Global variables
task_queue: Optional[BackgroundTaskQueue] = None
logger: Optional[LoggingService] = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    global task_queue, logger
    # Startup
    task_queue = BackgroundTaskQueue(max_size=100)
    logger = LoggingService()
    
    # Start background task processor
    asyncio.create_task(task_queue.process_tasks())
    
    yield
    
    # Shutdown
    if task_queue:
        await task_queue.stop()

app = FastAPI(
    title="Graph Connector API",
    description="Python recreation of C# Graph Connector API Template",
    version="1.0.0",
    lifespan=lifespan
)

@app.post("/grantPermissions")
async def grant_permissions(request: Request):
    """Grant permissions endpoint - stores tenant ID and redirects for admin consent"""
    body = await request.body()
    tenant_id = body.decode('utf-8')
    
    # Log the tenant ID
    logger.log_information(f"Received tenant ID: {tenant_id}")
    
    # Store the tenant ID in a text file
    async with open("tenantid.txt", "w") as f:
        await f.write(tenant_id)
    
    # Redirect the user to the specified URL
    client_id = "your-client-id"  # Replace with your actual client ID
    redirect_url = f"https://login.microsoftonline.com/organizations/adminconsent?client_id={client_id}"
    
    return RedirectResponse(url=redirect_url, status_code=status.HTTP_302_FOUND)

@app.post("/provisionconnection")
async def provision_connection(request: Request):
    """Provision connection endpoint"""
    body = await request.body()
    tenant_id = body.decode('utf-8')
    
    # Log the tenant ID
    logger.log_information(f"Provisioning connection for tenant ID: {tenant_id}")
    
    # Call the ProvisionConnection method with the tenant ID
    await ConnectionService.provision_connection()
    
    return {"status": "Connection provisioned successfully"}

@app.post("/loadcontent")
async def load_content(request: Request, background_tasks: BackgroundTasks):
    """Load content endpoint with background processing"""
    body = await request.body()
    tenant_id = body.decode('utf-8')
    
    # Log the tenant ID
    logger.log_information(f"Loading content for tenant ID: {tenant_id}")
    
    # Queue the long-running task
    async def background_task():
        await IngestionWorkflow.load_content()
    
    await task_queue.queue_background_work_item(background_task)
    
    # Return a response immediately
    return {"status": "Content loading queued"}, status.HTTP_202_ACCEPTED

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)