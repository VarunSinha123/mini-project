from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context
from flask import current_app

# Import all your models here
from models.user import User
from models.student import Student
from models.faculty import Faculty
from models.course import Course
from models.examination import Examination
from models.library import Library

config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

def get_engine():
    """
    Get SQLAlchemy engine either from Flask app or config
    """
    try:
        # Try to get it from the Flask app first
        return current_app.extensions['migrate'].db.get_engine()
    except (TypeError, KeyError):
        # Fallback to config from alembic.ini
        return engine_from_config(
            config.get_section(config.config_ini_section),
            prefix='sqlalchemy.',
            poolclass=pool.NullPool)

def get_metadata():
    """
    Get metadata from Flask app or models
    """
    if hasattr(current_app, 'extensions') and 'migrate' in current_app.extensions:
        return current_app.extensions['migrate'].db.metadata
    # fallback to base metadata
    from models.base import Base
    return Base.metadata

target_metadata = get_metadata()

def run_migrations_offline():
    """
    Run migrations in 'offline' mode.
    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """
    Run migrations in 'online' mode.
    """
    engine = get_engine()
    
    with engine.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
            compare_server_default=True
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()