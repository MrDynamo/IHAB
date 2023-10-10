# Check if db exists. Initialize connection if yes, call db_setup if not

from pathlib import Path
import sqlalchemy as db
import pandas as pd

PROJECT_DIR = Path(__file__).parent.parent.parent

#logger = global_logger.get_logger("init_db")

#engine = db.create_engine('sqlite+pysqlite:///data/ihab.db', echo=True)
engine = db.create_engine('sqlite+pysqlite:///:memory:', echo=True)
connection = engine.connect()
metadata = db.MetaData()

test = db.Table('test', metadata,
                db.Column('Id', db.Integer()),
                db.Column('name', db.String(255), nullable=False),
                db.Column('salary', db.Float(), default=100.0),
                db.Column('active', db.Boolean(), default=True)
                )

metadata.create_all(engine)

print('success!')

query = db.select(test)

#ResultProxy = connection.execute(query)
#ResultSet = ResultProxy.fetchall

results = connection.execute(query).fetchall()

df = pd.DataFrame(results)
df.columns = results
df.head(4)



# df = pd.read_sql("SELECT * FROM test", connection)

# print ('test')

metadata.drop_all
connection.close
