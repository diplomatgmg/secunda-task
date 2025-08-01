from logging.config import fileConfig
from pathlib import Path
import sys
from typing import Literal

from dotenv import load_dotenv
from sqlalchemy import pool
from sqlalchemy.engine import Connection
from sqlalchemy.ext.asyncio import async_engine_from_config
from sqlalchemy.sql.schema import SchemaItem
import uvloop

from alembic import context


load_dotenv()

ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT_DIR / "src"))

# App imports
from core.config.database import db_config  # isort:skip
from database.models import Base  # isort:skip


config = context.config

db_config.host = "localhost"  # Подмена хоста, т.к. используется снаружи docker сети
config.set_main_option("sqlalchemy.url", db_config.url.render_as_string(hide_password=False))

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata

def include_object(
        obj: SchemaItem,
        name: str | None,
        type_: Literal["schema", "table", "column", "index", "unique_constraint", "foreign_key_constraint"],
        _reflected: bool,
        _compare_to: SchemaItem | None,
) -> bool:
    return type_ == "table" and name in target_metadata.tables


def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def do_run_migrations(connection: Connection) -> None:
    context.configure(
        connection=connection,
        target_metadata=target_metadata,
        include_object=include_object,
    )

    with context.begin_transaction():
        context.run_migrations()


async def run_async_migrations() -> None:
    connectable = async_engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)

    await connectable.dispose()


def run_migrations_online() -> None:
    uvloop.run(run_async_migrations())


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
