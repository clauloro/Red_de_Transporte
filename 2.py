class Grafo:
    def __init__(self):
        self.nodos = {}  # Diccionario para almacenar los nodos y sus conexiones

    def agregar_ciudad(self, ciudad):
        self.nodos[ciudad] = {}  # Crea un diccionario vacío para las conexiones de la ciudad

    def agregar_conexion(self, ciudad1, ciudad2, distancia):
        # Para agregar una conexión entre ciudades, primero verificamos si las ciudades ya existen en el grafo
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