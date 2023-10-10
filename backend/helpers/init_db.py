# Check if db exists. Initialize connection if yes, call db_setup if not

from pathlib import Path
import sqlalchemy as db
import pandas as pd
import os

PROJECT_DIR = Path(__file__).parent.parent.parent
DATA_DIR = Path(str(PROJECT_DIR) + "/backend/data")

#logger = global_logger.get_logger("init_db")

### TODO: SETUP_DB()
### Use DB models to create default db
def setup_db():
    print("db setup")



### INIT_DB()

### If /backend/data folder doesn't exist, create it
if not DATA_DIR.exists():
    print("data_dir doesn't exist, creating...")
    os.mkdir(DATA_DIR)
    setup_db()


### Create session
engine = db.create_engine('sqlite+pysqlite:///data/ihab.db', echo=True)
connection = engine.connect()
metadata = db.MetaData()

test = db.Table('test', metadata,
                db.Column('Id', db.Integer()),
                db.Column('name', db.String(255), nullable=False),
                db.Column('salary', db.Float(), default=100.0),
                db.Column('active', db.Boolean(), default=True)
                )

metadata.create_all(engine)

Session = db.sessionmaker()
Session.configure(bind=engine)
session = Session()
