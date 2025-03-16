import os
from dotenv import load_dotenv

class Config:
    """
    Config class for initializing environment variables from a .env file.

    Methods
    -------
    init():
        Loads environment variables from a .env file located at '../../../config/.env.dev'.
    """

    @staticmethod
    def init():
        load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '../../../config/.env.dev'))