# BasesMapReduce
Proyecto de Base de Datos Avanzados
## Integrantes
- Aguirre Larrosa Stefanny
+ Vera Garcia Pedro

# Código de implementación de la base de datos

## Crear base de datos en mongoDB
use googlePlay

## Cargar datos a mongoDB
mongoimport -d googlePlay -c googlecsv --type csv --headerline --file RUTAHACIAELARCHIVO

## Código para las operaciones CRUD en MongoDB

### Código para insertar datos

db.googlecsv.insertOne({
"App": "App ejemplo",
"Category": "ART_AND_DESIGN",
"Rating": 5,
"Reviews": 20,
"Size": "2M",
"Installs": "20+",
"Type": "Free",
"Price": 0,
"Content Rating": "Everyone",
"Genres": "Art & Design",
"Last Updated": "November 21,2020",
"Current Ver": 1,
"Android Ver": "2.3 and up"})

db.googlecsv.insertOne({
"App": "App ejemplo 2",
"Category": "ART_AND_DESIGN",
"Rating": 5,
"Reviews": 20,
"Size": "2M",
"Installs": "20+",
"Type": "Free",
"Price": 0,
"Content Rating": "Everyone",
"Genres": "Art & Design",
"Last Updated": "November 22,2020",
"Current Ver": 1,
"Android Ver": "2.9 and up"})

db.googlecsv.insertOne({
"App": "App ejemplo 3",
"Category": "ART_AND_DESIGN",
"Rating": 5,
"Reviews": 200,
"Size": "2M",
"Installs": "20+",
"Type": "Paid",
"Price": 0.50,
"Content Rating": "Everyone",
"Genres": "Art & Design",
"Last Updated": "November 23,2020",
"Current Ver": 2,
"Android Ver": "2.9 and up"})

### Modificar datos
- db.googlecsv.updateOne({"App": "App ejemplo"}, {$set: {"Type": "Paid", "Price": 10 }}, {upsert:true})
+ db.googlecsv.updateOne({"App": "App ejemplo 2"}, {$set: {"Current Ver": 10 }}, {upsert:true})
- db.googlecsv.updateOne({"App": "App ejemplo 3"}, {$set: {"Installs": "100+" }}, {upsert:true})
### Eliminar datos
- db.googlecsv.remove({"App": "App ejemplo"}, true)
+ db.googlecsv.remove({"App": "App ejemplo 2"}, true)
-  db.googlecsv.remove({"App": "App ejemplo 3"}, true)
### Código para consultas
- db.googlecsv.find({ "Genres": "Finance", "Rating": {$eq:5} }).pretty()
+ db.googlecsv.find({ "Genres": "Finance", "Rating": {$eq:5} }).count()
- db.googlecsv.find({ "Type": {$ne: "Free"}, "Rating": {$lte:2 } }).pretty()
+ db.googlecsv.find({ "Type": {$ne: "Free"}, "Rating": {$lte:2 } }).count()

# Instalar Pymongo
Sirve para la conexión con la base de datos en MongoDB
- python -m pip install pymongo
