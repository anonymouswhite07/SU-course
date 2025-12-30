import os

# Check if running on Vercel
if os.environ.get("VERCEL"):
    # Use /tmp for SQLite on Vercel (ephemeral) or proper env var
    SQLALCHEMY_DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:////tmp/courses.db")
else:
    SQLALCHEMY_DATABASE_URL = "sqlite:///./courses.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
