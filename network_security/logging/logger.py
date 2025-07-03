# 🎯 Main Purpose of logger.py
# 🧩 logger.py sets up and configures the logging system once, so you can use it everywhere
#  in the project without repeating code.

# | ✅ Benefit                 | 📌 Description                                                          |
# | ------------------------- | ----------------------------------------------------------------------- |
# | 📦 Central Logging        | Keeps all log setup in one file — clean and reusable                    |
# | 📜 Log Everything         | Records all events (info, warnings, errors) to a file                   |
# | 🔍 Easier Debugging       | Helps trace what happened before an error                               |
# | 📁 Auto Log File Creation | Automatically creates a `logs/` folder with timestamped log files       |
# | 🔄 Reusability            | Can import and use in any module (`from logging.logger import logging`) |


import logging
import os
from datetime import datetime

# 1️⃣ Create a timestamp-based log file name
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# 2️⃣ Create the logs directory path
LOGS_PATH = os.path.join(os.getcwd(), "logs")

# 3️⃣ Make the directory if it doesn't exist
os.makedirs(LOGS_PATH, exist_ok=True)

# 4️⃣ Create the full log file path
LOG_FILE_PATH = os.path.join(LOGS_PATH, LOG_FILE)

# 5️⃣ Set up logging configuration
logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
)

# ✅ Now `logging` is ready to be imported and used
