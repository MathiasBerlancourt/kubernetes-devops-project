from sqlalchemy import create_engine, MetaData

engine = create_engine(
    "mysql+pymysql://root:password@mysql-service:3306/storedb")

meta = MetaData()

conn = engine.connect()
# test update 2
