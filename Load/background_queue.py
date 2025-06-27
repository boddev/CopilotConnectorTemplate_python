import asyncio
from typing import Callable, Awaitable, Optional
from asyncio import Queue

class BackgroundTaskQueue:
    """Queue for background tasks"""
    
    def __init__(self, max_size: int = 100):
        self._queue: Queue = Queue(maxsize=max_size)
        self._running = False
    
    async def queue_background_work_item(self, work_item: Callable[[], Awaitable[None]]):
        """Queue a background work item"""
        await self._queue.put(work_item)
    
    async def dequeue_async(self) -> Optional[Callable[[], Awaitable[None]]]:
        """Dequeue a work item"""
        try:
            return await asyncio.wait_for(self._queue.get(), timeout=1.0)
        except asyncio.TimeoutError:
            return None
    
    async def process_tasks(self):
        """Process queued tasks"""
        self._running = True
        while self._running:
            work_item = await self.dequeue_async()
            if work_item:
                try:
                    await work_item()
                except Exception as ex:
                    print(f"Error processing background task: {ex}")
            await asyncio.sleep(0.1)  # Small delay to prevent busy waiting
    
    async def stop(self):
        """Stop processing tasks"""
        self._running = False