class Conexion:
    def __init__(self, poblacion1, poblacion2, distancia):
        self.poblacion1 = poblacion1
        self.poblacion2 = poblacion2
        self.distancia = distancia

class Poblacion:
    def __init__(self, nombre):
        self.nombre = nombre

class GrafoCiudades:
    def __init__(self):
        self.poblaciones = []
        self.conexiones = []

    def agregar_poblacion(self, nombre):
        poblacion = Poblacion(nombre)
        self.poblaciones.append(poblacion)

    def agregar_conexion(self, nombre_poblacion1, nombre_poblacion2, distancia):
        poblacion1 = next((p for p in self.poblaciones if p.nombre == nombre_poblacion1), None)
        poblacion2 = next((p for p in self.poblaciones if p.nombre == nombre_poblacion2), None)

        if poblacion1 and poblacion2:
            conexion = Conexion(poblacion1, poblacion2, distancia)
            self.conexiones.append(conexion)

    def visualizar_grafo(self):
        for conexion in self.conexiones:
            print(f'{conexion.poblacion1.nombre} --({conexion.distancia})--> {conexion.poblacion2.nombre}')

    def ruta_mas_corta(self, origen, destino):
        distancia_minima = float('inf')
        ruta_optima = None

        for conexion in self.conexiones:
            if conexion.poblacion1.nombre == origen:
                distancia_actual, ruta_actual = self._encontrar_ruta(conexion.poblacion2.nombre, destino, [conexion], set())
                if distancia_actual < distancia_minima:
                    distancia_minima = distancia_actual
                    ruta_optima = ruta_actual

            elif conexion.poblacion2.nombre == origen:
                distancia_actual, ruta_actual = self._encontrar_ruta(conexion.poblacion1.nombre, destino, [conexion], set())
                if distancia_actual < distancia_minima:
                    distancia_minima = distancia_actual
                    ruta_optima = ruta_actual

        if ruta_optima:
            ruta = [conexion.poblacion1.nombre for conexion in ruta_optima] + [destino]
            print(f'La ruta más corta que empieza en {origen} y termina en {destino} es: {ruta}. La distancia total es: {distancia_minima}.')
        else:
            print(f'No existe una ruta posible desde {origen} hasta {destino}.')

    def todas_las_rutas_posibles(self, origen, destino):
        rutas = []
        self._generar_rutas([], origen, destino, rutas, set())
        print(f'Todas las rutas posibles desde {origen} hasta {destino}:')
        
        for i, ruta in enumerate(rutas):
            distancia_total = sum([conexion.distancia for conexion in ruta])
            print(f'Ruta {i+1}: {ruta}. Distancia total: {distancia_total}')

    def _encontrar_ruta(self, origen, destino, ruta_actual, visitados):
        if origen == destino:
            return sum([conexion.distancia for conexion in ruta_actual]), ruta_actual

        visitados.add(origen)

        distancia_minima = float('inf')
        ruta_optima = None

        for conexion in self.conexiones:
            if conexion.poblacion1.nombre == origen and conexion.poblacion2.nombre not in visitados:
                distancia_actual, ruta_actual = self._encontrar_ruta(conexion.poblacion2.nombre, destino, ruta_actual + [conexion], visitados)
                if distancia_actual < distancia_minima:
                    distancia_minima = distancia_actual
                    ruta_optima = ruta_actual
            elif conexion.poblacion2.nombre == origen and conexion.poblacion1.nombre not in visitados:
                distancia_actual, ruta_actual = self._encontrar_ruta(conexion.poblacion1.nombre, destino, ruta_actual + [conexion], visitados)
                if distancia_actual < distancia_minima:
                    distancia_minima = distancia_actual
                    ruta_optima = ruta_actual

        visitados.remove(origen)

        return distancia_minima, ruta_optima

    def _generar_rutas(self, ruta_actual, origen, destino, rutas, visitados):
        if origen in visitados:
            return

        if origen == destino:
            rutas.append(ruta_actual)
            return

        visitados.add(origen)

        for conexion in self.conexiones:
                        if conexion.poblacion1.nombre == origen and conexion.poblacion2.nombre not in ruta_actual:
                            self._generar_rutas(ruta_actual + [conexion], conexion.poblacion2.nombre, destino, rutas, visitados)
                        elif conexion.poblacion2.nombre == origen and conexion.poblacion1.nombre not in ruta_actual:
                          self._generar_rutas(ruta_actual + [conexion], conexion.poblacion1.nombre, destino, rutas, visitados)

        visitados.remove(origen)

# Crear una instancia de la clase GrafoCiudades
grafo = GrafoCiudades()

# Agregar poblaciones al grafo
grafo.agregar_poblacion("Barcelona")
grafo.agregar_poblacion("Valencia")
grafo.agregar_poblacion("Madrid")
grafo.agregar_poblacion("Sevilla")

# Agregar conexiones entre las poblaciones
grafo.agregar_conexion("Barcelona", "Valencia", 350)
grafo.agregar_conexion("Valencia", "Madrid", 350)
grafo.agregar_conexion("Madrid", "Sevilla", 500)

# Visualizar el grafo
grafo.visualizar_grafo()

# Obtener la ruta más corta entre dos poblaciones
origen = input("¿Desde qué población quieres hacer el recorrido?: ")
destino = input("¿Hasta qué población quieres hacer el recorrido?: ")

grafo.ruta_mas_corta(origen, destino)

# Obtener todas las rutas posibles entre dos poblaciones
grafo.todas_las_rutas_posibles(origen, destino) 


