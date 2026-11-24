from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    app_name: str = "Carsharing Rental API"
    app_version: str = "1.0.0"
    app_env: str = "development"
    http_port: int = 8000

settings = Settings()
