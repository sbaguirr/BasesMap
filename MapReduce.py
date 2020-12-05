import json

class MapReduce:
    def __init__(self):
        self.intermediate = {}
        self.result = []

    def emit_intermediate(self, key, value):
        self.intermediate.setdefault(key, [])
        self.intermediate[key].append(value)

    def emit(self, value):
        self.result.append(value) 

    def execute(self, data, mapper, reducer, nombre_archivo):
        for line in data:
            mapper(line)

        for key in self.intermediate:
            reducer(key, self.intermediate[key])

        jenc = json.JSONEncoder()
        file = open(nombre_archivo, 'w', encoding="utf-8")
        file.write('La categoría predominante es ')
        # Obtener la cantidad mayor
        maxi = max(self.result, key= lambda tupla: tupla[1])
        # Escribir en el archivo
        file.write(maxi[0]+' con '+ str(maxi[1])+" descargas")
        file.write('\n\nResumen del conteo\n')
        for item in self.result:
            file.write(jenc.encode(item)+'\n')
        file.close()
