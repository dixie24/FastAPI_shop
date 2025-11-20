from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "FastAPI Shop App"
    debug: bool = True
    database_url: str = "sqlite:///./shop.db"
    cors_origins: list[str] = [
        "http://localhost:5173",
        "http://localhost:8000",
        "http://127.0.0.1:5173",
        "http://127.0.0.1:8000",
    ]
    
    static_dir: str = "static"
    images_dir: str = "static/images"
    
    class Config:
        env_file = ".env"
        
        
settings = Settings()

def get_settings() -> Settings:
    return settings
from pydantic_settings import BaseSettings
from pydantic_settings import BaseSettings
class Settings(BaseSettings):
    app_name: str = "FastAPI Shop App"
    debug: bool = True
    database_url: str = "sqlite:///./shop.db"
    cors_origins: list[str] = [
        "http://localhost:5173",
        "http://localhost:8000",
        "http://