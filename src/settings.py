from pydantic_settings import BaseSettings

ENV_FILE = '.env'


class Settings(BaseSettings):
    host: str
    port: int

    class Config:
        env_file = ENV_FILE
        env_prefix = 'APP_'


settings = Settings()
