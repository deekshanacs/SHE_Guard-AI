import os
from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

BASE_DIR = Path(__file__).resolve().parent
DEFAULT_SQLITE_PATH = BASE_DIR / "sheguard.db"


def load_env_file(env_path: Path):
    if not env_path.exists():
        return
    for raw_line in env_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        os.environ.setdefault(key, value)


load_env_file(BASE_DIR / ".env")


def _sqlite_url(path: Path) -> str:
    return f"sqlite:///{path.as_posix()}"


# Prefer an explicit DATABASE_URL when provided, otherwise use the bundled
# SQLite file beside backend/database.py so the app opens the same DB file no
# matter where it is launched from.
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL") or _sqlite_url(DEFAULT_SQLITE_PATH)

# If Render provides a writable disk, keep using the same database file there.
database_dir = Path("/data")
if database_dir.exists() and os.access(database_dir, os.W_OK):
    SQLALCHEMY_DATABASE_URL = _sqlite_url(database_dir / "sheguard.db")

if SQLALCHEMY_DATABASE_URL.startswith("sqlite:///"):
    DEFAULT_SQLITE_PATH.parent.mkdir(parents=True, exist_ok=True)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency to get db session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
