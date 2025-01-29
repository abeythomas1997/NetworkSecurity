import sys
import Networksecurity.Logging import logger 

    
# Custom exception class inheriting from Exception
class NetworkSecurityException(Exception):
    def __init__(self, error_message, error_details: sys):
        # Initialize the parent Exception class with the error message
        super().__init__(error_message)  # This calls the __init__ of the Exception class
        
        # Extract traceback details
        _, _, exc_tb = error_details.exc_info()  
        
        # Store the line number and file name where the error occurred
        self.lineno = exc_tb.tb_lineno
        self.file_name = exc_tb.tb_frame.f_code.co_filename

    # Custom string representation of the error
    def __str__(self):
       return "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        self.file_name, self.lineno, str(self.error_message))
    