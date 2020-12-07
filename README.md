# BasesMapReduce
Proyecto de Base de Datos Avanzados
## Integrantes
Aguirre Larrosa Stefanny
Vera Garcia Pedro
# Installar pymongo
Sirve para la conexión con la base de datos en MongoDB
python -m pip install pymongo
# Código para las operaciones CRUD en MongoDB
### Modificar datos
db.googlecsv.updateOne({"App": "App ejemplo"}, {$set: {"Type": "Paid", "Price": 10 }}, {upsert:true})
db.googlecsv.updateOne({"App": "App ejemplo 2"}, {$set: {"Current Ver": 10 }}, {upsert:true})
db.googlecsv.updateOne({"App": "App ejemplo 3"}, {$set: {"Installs": "100+" }}, {upsert:true})
### Eliminar datos
db.googlecsv.remove({"App": "App ejemplo"}, true)
db.googlecsv.remove({"App": "App ejemplo 2"}, true)
db.googlecsv.remove({"App": "App ejemplo 3"}, true)
### Código para consultas
db.googlecsv.find({ "Genres": "Finance", "Rating": {$eq:5} }).pretty()
db.googlecsv.find({ "Genres": "Finance", "Rating": {$eq:5} }).count()

db.googlecsv.find({ "Type": {$ne: "Free"}, "Rating": {$lte:2 } }).pretty()
db.googlecsv.find({ "Type": {$ne: "Free"}, "Rating": {$lte:2 } }).count()