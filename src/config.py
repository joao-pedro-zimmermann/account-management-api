from pydantic_settings import BaseSettings

# ---------------------------------------------------------- #

class Settings(BaseSettings):
    PORT: int = 9000

    class Config:
        env_file = ".env"

settings = Settings() 