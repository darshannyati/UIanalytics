from sqlmodel import create_engine, Session, SQLModel
from sqlalchemy import inspect

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)

def create_db_and_tables():
    # Only create tables if they don't exist
    inspector = inspect(engine)
    if 'user' not in inspector.get_table_names():
        SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session