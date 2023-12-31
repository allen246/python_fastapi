from app.models import Base
from app.config import settings

from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context
# ---------------- added code here -------------------------#
import os, sys
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(BASE_DIR, ".env"))
sys.path.append(BASE_DIR)
#------------------------------------------------------------#
# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config
# ---------------- added code here -------------------------#
# this will overwrite the ini-file sqlalchemy.url path
# with the path given in the config of the main code

config.set_main_option("sqlalchemy.url", f"postgresql+psycopg2://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_HOSTNAME}:{settings.DATABASE_PORT}")

#------------------------------------------------------------#
# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
# ---------------- added code here -------------------------#

#------------------------------------------------------------#
# ---------------- changed code here -------------------------#
# here target_metadata was equal to None
target_metadata = Base.metadata
#------------------------------------------------------------#
