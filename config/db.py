from sqlalchemy import create_engine, MetaData
import base64
import os

encoded_password = os.environ.get("MYSQL_ROOT_PASSWORD")


password = base64.b64decode(encoded_password).decode("utf-8")


engine = create_engine(
    "mysql+pymysql://root:{password}@mysql-service:3306/storedb")

meta = MetaData()

conn = engine.connect()
# test update 2
