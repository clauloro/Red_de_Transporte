class BSTNode:
    def __init__(self, distancia, ciudad1, ciudad2):
        self.distancia = distancia
        self.ciudad1 = ciudad1
        self.ciudad2 = ciudad2
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def agregar_distancia(self, distancia, ciudad1, ciudad2):
        if not self.root:
            self.root = BSTNode(distancia, ciudad1, ciudad2)
        else:
            self._agregar_distancia_recursivo(self.root, distancia, ciudad1, ciudad2)

    def _agregar_distancia_recursivo(self, node, distancia, ciudad1, ciudad2):
        if distancia < node.distancia:
            if node.left:
                self._agregar_distancia_recursivo(node.left, distancia, ciudad1, ciudad2)
            else:
                node.left = BSTNode(distancia, ciudad1, ciudad2)
        else:
            if node.right:
                self._agregar_distancia_recursivo(node.right, distancia, ciudad1, ciudad2)
            else:
                node.right = BSTNode(distancia, ciudad1, ciudad2)

    def mostrar_registro(self):
        self._mostrar_registro_recursivo(self.root)

    def _mostrar_registro_recursivo(self, node):
        if node:
            self._mostrar_registro_recursivo(node.left)
            print(f"Distancia: {node.distancia}, Ciudades: {node.ciudad1} - {node.ciudad2}")
            self._mostrar_registro_recursivo(node.right)
    def arbol_recubrimiento_minimo(self):
        arbol_minimo = Grafo()
        aristas_visitadas = set()

        sorted_edges = sorted(self.get_all_edges(), key=lambda x: x[2]) # Obtener todas las aristas ordenadas por peso

        for edge in sorted_edges:
            origen, destino, peso = edge

            if origen not in arbol_minimo.vertices or destino not in arbol_minimo.vertices:
                arbol_minimo.agregar_ciudad(origen)
                arbol_minimo.agregar_ciudad(destino)
                arbol_minimo.agregar_conexion(origen, destino, peso)
                aristas_visitadas.add((origen, destino))
            else:
                if not existe_camino(arbol_minimo, origen, destino):
                    if (origen, destino) not in aristas_visitadas:
                        arbol_minimo.agregar_conexion(origen, destino, peso)
                        aristas_visitadas.add((origen, destino))

        return arbol_minimo

    class Grafo:
        def __init__(self):
            self.vertices = {}

        def agregar_ciudad(self, ciudad):
            self.vertices[ciudad] = []

        def agregar_conexion(self, origen, destino, peso):
            if origen in self.vertices and destino in self.vertices:
                self.vertices[origen].append((destino, peso))
                self.vertices[destino].append((origen, peso))
            else:
                print("Las ciudades no existen en el grafo.")