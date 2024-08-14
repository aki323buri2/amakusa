# %%
# %%
from utilities.common import dotdict
from sqlalchemy import create_engine
from urllib.parse import quote_plus
import pandas as pd 

config = dotdict(
  # driver = "FreeTDS", 
  driver = "{SQL Server}", 
  server = "XXX.XXXXXX.XXX", # address of server
  port = 1433, 
  uid = "xx", 
  pwd = "xxxxxx", 
  # tds_version = "7.1", 
)

def _engine():
  quoted = quote_plus(";".join([f"{n}={v}" for n, v in config.items()]))
  engine = create_engine(f"mssql+pyodbc:///?odbc_connect={quoted}")
  return engine

def _query(sql, coerce_float=True, **kargs):
  with _engine().connect() as con:
    return pd.read_sql_query(sql, con=con, coerce_float=coerce_float, **kargs).fillna("")

# odein_query("select top 10 * from sui_master.dbo.tmasa")

# %%





