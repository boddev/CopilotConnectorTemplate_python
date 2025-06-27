import logging
from datetime import datetime

class LoggingService:
    """Custom logging service"""
    
    def __init__(self):
        # Configure logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)
    
    def log_information(self, message: str):
        """Log an information message"""
        self.logger.info(message)
    
    def log_error(self, message: str):
        """Log an error message"""
        self.logger.error(message)
    
    def log_warning(self, message: str):
        """Log a warning message"""
        self.logger.warning(message)