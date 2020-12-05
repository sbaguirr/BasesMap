import MapReduce
import pymongo

mr = MapReduce.MapReduce()
# Tarea: Encontrar las categorías predominantes, respecto a la cantidad de descargas para las aplicaciones gratuitas y pagadas respectivamente.
# Ejemplo de linea {'Category': 'MEDICAL', 'Installs': '1,000+', 'Type': 'Free'}

def mapper(record):
    category= record['Category']
    installs= record['Installs']
    mr.emit_intermediate(category, installs)


def reducer(key, list_of_values):
    total = 0 
    for t in list_of_values:
        # Proceso necesario para transformar los valores de la clave "Installs"
        # debido a que están almacenados como una cadena de caracteres 
        # y además utilizan el símbolo "+"
        noplus = str(t).replace("+",'')
        nocom = str(noplus).replace(",", '')
        numero = float(nocom) 
        total += numero

    mr.emit((key, total))


if __name__ == '__main__':
    # Conexión a MongoDB
    cliente = pymongo.MongoClient("mongodb://localhost:27017/")
    base = cliente["googlePlay"]
    coleccion = base["googlecsv"]
    query = {"_id": 0, "Category": 1, "Installs": 1, "Type":"Free"}
    resultado = coleccion.find({}, query)

#    for x in resultado:
#       print(x)

    mr.execute(resultado, mapper, reducer, "appsgratis.txt")