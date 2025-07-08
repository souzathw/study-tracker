from dotenv import load_dotenv
import os

load_dotenv()

def env_or_fail(var: str) -> str:
    value = os.getenv(var)
    if value is None:
        raise RuntimeError(f"Missing environment variable: {var}")
    return value

DB_USER = env_or_fail("DB_USER")
DB_PASSWORD = env_or_fail("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "3306")
DB_NAME = env_or_fail("DB_NAME")

SQLALCHEMY_DATABASE_URL = (
    f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

SECRET_KEY = env_or_fail("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60
