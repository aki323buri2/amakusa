import zipfile 
def extract_zipfile(zipfilename, path): 
  with zipfile.ZipFile(zipfilename) as z: 
    for info in z.infolist():
      info.filename = info.filename.encode("cp437").decode("cp932")
      z.extract(info, path=path)
      print(info.filename)
  print("extract zipfile: done!")
