import MapReduce
import pymongo

mr = MapReduce.MapReduce()
# Categoría predominante, respecto a la cantidad de descargas, de categorías Free y Pago respectivamente.
# Ejemplo de linea {'Category': 'MEDICAL', 'Installs': '1,000+', 'Type': 'Free'}

def mapper(record):
 category= record['Category']
 installs= record['Installs']
 mr.emit_intermediate(category, installs)


def reducer(key, list_of_values):
 total = 0 
 for t in list_of_values:
  num= t.strip('+') #No que procede :v  Me sale este error 'int' object has no attribute 'strip'
  nocom= num.replace(',','')
  total += float(nocom)
 mr.emit((key, total))


if __name__ == '__main__':
    # Conexión a MongoDB
 cliente = pymongo.MongoClient("mongodb://localhost:27017/")
 base = cliente["googlePlay"]
 coleccion = base["googlecsv"]
 query = {"_id": 0, "Category": 1, "Installs": 1, "Type":1}
 resultado = coleccion.find({}, query)
 mr.execute(resultado, mapper, reducer)
