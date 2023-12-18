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