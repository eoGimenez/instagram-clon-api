from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache
from enviroment import config_env

class Settings(BaseSettings):
    origin: str
    secret_key: str
    algorithm: str

    model_config = SettingsConfigDict(env_file= '.env')


@lru_cache()
def get_settings():
    return config_env.Settings()