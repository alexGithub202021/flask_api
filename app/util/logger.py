from logging.handlers import RotatingFileHandler
import logging

class Logger:

    def __init__(self):
        file = 'logs/logs_api.log'
        
        handler = RotatingFileHandler(filename=file, maxBytes=500*1024, backupCount=5)  # Add backupCount for old log rotation
        handler.setLevel(logging.ERROR)  # Set level for the handler
        
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s - [%(module)s > %(filename)s > %(funcName)s]', datefmt="%d-%m-%Y,%H:%M:%S")
        handler.setFormatter(formatter)
        
        # Get logger and add the handler
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        self.logger.addHandler(handler)
        
    def getLoger(self):
        return self.logger