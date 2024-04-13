from sqlalchemy import MetaData, Table, Column, Integer, String, DateTime, Boolean

metadata = MetaData()

user_table = Table(
    "user_account",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("username", String, nullable=False, unique=True),
    Column("password", String, nullable=False),
    Column("email", String, nullable=False, unique=True),
    Column("created_at", DateTime, nullable=False, server_default="now()"),
    Column("is_active", Boolean, nullable=False, server_default="true"),
)
