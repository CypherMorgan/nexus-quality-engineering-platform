from pydantic import BaseModel, Field


class ApplicationConfig(BaseModel):
    base_url: str


class DatabaseConfig(BaseModel):
    connection_string: str


class ApiConfig(BaseModel):
    base_url: str
    timeout: int = Field(default=30)


class BrowserConfig(BaseModel):
    browser_name: str
    headless: bool = True
    timeout: int = 30000


class EnvironmentConfig(BaseModel):
    application: ApplicationConfig
    api: ApiConfig
    database: DatabaseConfig
    browser: BrowserConfig