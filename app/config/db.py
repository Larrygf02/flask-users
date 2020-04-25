from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
DB_URL = os.environ.get('DB_URL')
#url = 'postgresql://postgres:123@localhost:5433/manage_users'
engine = create_engine(DB_URL)

# create a configured "Session" class
Session = sessionmaker(bind=engine)

with engine.connect() as connection:
    result = connection.execute("SELECT CURRENT_DATE;")
    for row in result:
        print(row)