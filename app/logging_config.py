import logging
import sys
from logging.handlers import RotatingFileHandler

def setup_logging():
    """
    Configures logging for the application.
    Sets up a console handler and a file handler.
    """
    import os
    print(f"DEBUG: setup_logging called from {os.getcwd()}")
    # Create a custom logger
    logger = logging.getLogger("devsecops_app")
    logger.setLevel(logging.INFO)

    # Create handlers
    c_handler = logging.StreamHandler(sys.stdout)
    f_handler = RotatingFileHandler('app.log', maxBytes=10*1024*1024, backupCount=5)
    
    c_handler.setLevel(logging.INFO)
    f_handler.setLevel(logging.INFO)

    # Create formatters and add it to handlers
    c_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    c_handler.setFormatter(c_format)
    f_handler.setFormatter(f_format)

    # Add handlers to the logger
    if not logger.handlers:
        logger.addHandler(c_handler)
        logger.addHandler(f_handler)

    return logger
