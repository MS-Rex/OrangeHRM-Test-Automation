import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """Configuration class to manage test environment variables"""

    # Base URL
    BASE_URL = os.getenv("ORANGEHRM_URL", "")

    # Login credentials
    USERNAME = os.getenv("ORANGEHRM_USERNAME", "")
    PASSWORD = os.getenv("ORANGEHRM_PASSWORD", "")

    # Timeouts
    DEFAULT_TIMEOUT = int(
        os.getenv("DEFAULT_TIMEOUT", "10")
    )  # Had to increase the timeout to 20 seconds to avoid timeout errors
