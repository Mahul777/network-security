# 🎯 Purpose of exception.py
# The exception.py file is used to create a custom exception handler in your Python project.

# | 🔧 Feature                       | ✅ Purpose                                                                       |
# | -------------------------------- | ------------------------------------------------------------------------------- |
# | `NetworkSecurityException` class | A custom exception to catch and format errors in a user-friendly way.           |
# | `__init__` method                | Captures file name, line number, and error message using `sys` and `traceback`. |
# | `__str__` method                 | Defines how the exception is displayed (a clean, formatted string).             |
# | `logging` integration            | Logs the errors into a log file for future reference.                           |
# | `try-except` example (main)      | A small test to raise and handle an exception (like `1/0`).                     |

import sys
import os

# ✅ Import the logger from the logger.py file
from network_security.logging.logger import logging


class NetworkSecurityException(Exception):
    def __init__(self, error_message: Exception, error_detail: sys):
        """
        Custom exception class to capture detailed error information.
        """
        super().__init__(error_message)

        # 🧠 Get traceback details
        _, _, exc_tb = error_detail.exc_info()
        self.error_message = f"""
Error occurred in script: [{os.path.basename(exc_tb.tb_frame.f_code.co_filename)}]
at line number: [{exc_tb.tb_lineno}]
error message: [{str(error_message)}]
        """

    def __str__(self):
        return self.error_message


# ✅ TEST BLOCK - Only runs if this file is executed directly
if __name__ == "__main__":
    try:
        logging.info("Entered try block")

        # ⚠️ Example error: division by zero
        x = 1 / 0

    except Exception as e:
        logging.error("Exception occurred")
        raise NetworkSecurityException(e, sys)
