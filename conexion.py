import pymongo
#Codigo para probar la conexion
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["googlePlay"]
mycol = mydb["googlecsv"]
myquery = {"_id":0, "Category": 1, "Installs": 1, "Type":1}
mydoc = mycol.find({}, myquery)

for x in mydoc:
  print(x)