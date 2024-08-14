from utilities.common import fullpath, load_csv

def columns_and_data(filename, colsname=None, query=None, adjuster=None, **kwargs):
  if colsname is None: 
    colsname = filename.parent / f"{filename.stem}_columns.csv"
  elif type(colsname) == str:
    colsname = fullpath(filename.parent, colsname)
  
  df = load_csv(filename, **kwargs).fillna("")
  if (query is not None):
    df = df.query(query)
  
  if (adjuster):
    df = adjuster(df)

  columns = load_csv(colsname)
  res = dict(
    columns=columns.to_dict(orient="records"), 
    query=query, 
    count=len(df), 
    data=df.to_dict(orient="records")
  )
  return res

# skydir = fullpath("skysea")
# filename = skydir / "targets.csv"
# filename = skydir / "links.csv"
# filename = skydir / "targets_suisvr.csv"
# columns_and_data(filename, "targets_columns.csv")