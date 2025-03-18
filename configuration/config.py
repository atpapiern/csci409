from pydantic_settings import BaseSettings
from pydantic import BaseModel

class ServerSettings(BaseSettings):
    api_key:str = 'be5ec94292c64bfabc8ae27290df855c'
    endpoint:str = 'https://api-v3.mbta.com/'

class Message(BaseModel): # Create a message model for handling errors
    message: str # A string to store the message