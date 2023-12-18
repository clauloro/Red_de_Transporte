from heapq import heappop, heappush

class Grafo:
    def __init__(self):
        self.nodos = {}

    def agregar_ciudad(self, ciudad):
        self.nodos[ciudad] = {}

    def agregar_conexion(self, ciudad1, ciudad2, distancia):
        if ciudad1 in self.nodos and ciudad2 in self.nodos:
            self.nodos[ciudad1][ciudad2] = distancia
            self.nodos[ciudad2][ciudad1] = distancia
        else:
            print("Una o ambas ciudades no existen en el grafo.")

    def mostrar_grafo(self):
        for ciudad, conexiones in self.nodos.items():
            print(f"Ciudad: {ciudad}")
            print("Conexiones:")
            for ciudad_conectada, distancia in conexiones.items():
                print(f"- {ciudad_conectada}: {distancia}")
            print()
    
    def ruta_mas_corta(self, origen, destino):
        if origen not in self.nodos or destino not in self.nodos:
            print("Una o ambas ciudades no existen en el grafo.")
            return None

        distancias = {ciudad: float('inf') for ciudad in self.nodos}
        distancias[origen] = 0

        cola_prioridad = [(0, origen)]
        ruta_anterior = {}

        while cola_prioridad:
            distancia_actual, ciudad_actual = heappop(cola_prioridad)

            if distancia_actual > distancias[ciudad_actual]:
                continue

            if ciudad_actual == destino:
                ruta = []
                while ciudad_actual in ruta_anterior:
                    ruta.insert(0, ciudad_actual)
                    ciudad_actual = ruta_anterior[ciudad_actual]
                ruta.insert(0, origen)
                return ruta, distancias[destino]

            for ciudad_vecina, distancia_vecina in self.nodos[ciudad_actual].items():
                distancia_total = distancia_actual + distancia_vecina
                if distancia_total < distancias[ciudad_vecina]:
                    distancias[ciudad_vecina] = distancia_total
                    ruta_anterior[ciudad_vecina] = ciudad_actual
                    heappush(cola_prioridad, (distancia_total, ciudad_vecina))

        print("No se encontró una ruta.")
        return None

# Creamos una instancia de la clase Grafo
red_transporte = Grafo()

# Agregamos las ciudades al grafo
red_transporte.agregar_ciudad("Ciudad_A")
red_transporte.agregar_ciudad("Ciudad_B")
red_transporte.agregar_ciudad("Ciudad_C")
red_transporte.agregar_ciudad("Ciudad_D")

# Agregamos las conexiones y distancias entre las ciudades
red_transporte.agregar_conexion("Ciudad_A", "Ciudad_B", 10)
red_transporte.agregar_conexion("Ciudad_A", "Ciudad_C", 12)
red_transporte.agregar_conexion("Ciudad_B", "Ciudad_D", 5)
red_transporte.agregar_conexion("Ciudad_C", "Ciudad_D", 8)

# Mostramos el grafo resultante
red_transporte.mostrar_grafo()

# Encontrar la ruta más corta entre Ciudad_A y Ciudad_D
ruta, distancia = red_transporte.ruta_mas_corta("Ciudad_A", "Ciudad_D")
print("Ruta más corta:", "->".join(ruta))
print("Distancia total:", distancia)
