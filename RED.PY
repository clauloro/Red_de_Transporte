import networkx as nx
import matplotlib.pyplot as plt

class Grafo:
    def __init__(self):
        self.G = nx.Graph()
        self.BST = BST()

    def agregar_ciudad(self, nombre):
        self.G.add_node(nombre)

    def agregar_conexion(self, ciudad1, ciudad2, distancia):
        self.G.add_edge(ciudad1, ciudad2, weight=distancia)
        self.BST.agregar(distancia, (ciudad1, ciudad2))

    def mostrar_grafo(self):
        pos = nx.spring_layout(self.G)
        labels = nx.get_edge_attributes(self.G, 'weight')
        nx.draw(self.G, pos, with_labels=True, font_weight='bold')
        nx.draw_networkx_edge_labels(self.G, pos, edge_labels=labels)
        plt.show()

    def ruta_mas_corta(self, origen, destino):
        distancia_total, ruta = nx.dijkstra_path(self.G, origen, destino, weight='weight')
        print(f'Ruta más corta desde {origen} hasta {destino}: {ruta}, Distancia total: {distancia_total}')

    def arbol_recubrimiento_minimo(self):
        MST = nx.minimum_spanning_tree(self.G, weight='weight')
        pos = nx.spring_layout(self.G)
        labels = nx.get_edge_attributes(self.G, 'weight')
        nx.draw(MST, pos, with_labels=True, font_weight='bold')
        nx.draw_networkx_edge_labels(self.G, pos, edge_labels=labels)
        plt.show()

class NodoBST:
    def __init__(self, clave, valor):
        self.clave = clave
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

class BST:
    def __init__(self):
        self.raiz = None

    def agregar(self, clave, valor):
        nuevo_nodo = NodoBST(clave, valor)

        if self.raiz is None:
            self.raiz = nuevo_nodo
        else:
            self._agregar_recursivo(self.raiz, nuevo_nodo)

    def _agregar_recursivo(self, nodo_actual, nuevo_nodo):
        if nuevo_nodo.clave < nodo_actual.clave:
            if nodo_actual.izquierdo is None:
                nodo_actual.izquierdo = nuevo_nodo
            else:
                self._agregar_recursivo(nodo_actual.izquierdo, nuevo_nodo)
        else:
            if nodo_actual.derecho is None:
                nodo_actual.derecho = nuevo_nodo
            else:
                self._agregar_recursivo(nodo_actual.derecho, nuevo_nodo)

    def mostrar_ordenado(self):
        self._mostrar_ordenado_recursivo(self.raiz)

    def _mostrar_ordenado_recursivo(self, nodo_actual):
        if nodo_actual is not None:
            self._mostrar_ordenado_recursivo(nodo_actual.izquierdo)
            print(f'Distancia: {nodo_actual.clave}, Ciudades: {nodo_actual.valor}')
            self._mostrar_ordenado_recursivo(nodo_actual.derecho)

# Ejemplo de uso
mi_grafo = Grafo()

# Agregar ciudades
mi_grafo.agregar_ciudad("A")
mi_grafo.agregar_ciudad("B")
mi_grafo.agregar_ciudad("C")
mi_grafo.agregar_ciudad("D")
mi_grafo.agregar_ciudad("E")

# Agregar conexiones con distancias
mi_grafo.agregar_conexion("A", "B", 10)
mi_grafo.agregar_conexion("B", "C", 6)
mi_grafo.agregar_conexion("A", "C", 15)
mi_grafo.agregar_conexion("C", "D", 8)
mi_grafo.agregar_conexion("B", "D", 3)
mi_grafo.agregar_conexion("A", "D", 8)
mi_grafo.agregar_conexion("C", "E", 9)

# Mostrar grafo
mi_grafo.mostrar_grafo()

# Mostrar registro ordenado de distancias
mi_grafo.BST.mostrar_ordenado()

# Encontrar la ruta más corta
mi_grafo.ruta_mas_corta("A", "D")

# Construir el árbol
class NodoBST:
    def __init__(self, clave, valor):
        self.clave = clave
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

class BST:
    def __init__(self):
        self.raiz = None

    def agregar(self, clave, valor):
        nuevo_nodo = NodoBST(clave, valor)

        if self.raiz is None:
            self.raiz = nuevo_nodo
        else:
            self._agregar_recursivo(self.raiz, nuevo_nodo)

    def _agregar_recursivo(self, nodo_actual, nuevo_nodo):
        if nuevo_nodo.clave < nodo_actual.clave:
            if nodo_actual.izquierdo is None:
                nodo_actual.izquierdo = nuevo_nodo
            else:
                self._agregar_recursivo(nodo_actual.izquierdo, nuevo_nodo)
        else:
            if nodo_actual.derecho is None:
                nodo_actual.derecho = nuevo_nodo
            else:
                self._agregar_recursivo(nodo_actual.derecho, nuevo_nodo)

    def mostrar_ordenado(self):
        self._mostrar_ordenado_recursivo(self.raiz)

    def _mostrar_ordenado_recursivo(self, nodo_actual):
        if nodo_actual is not None:
            self._mostrar_ordenado_recursivo(nodo_actual.izquierdo)
            print(f'Distancia: {nodo_actual.clave}, Ciudades: {nodo_actual.valor}')
            self._mostrar_ordenado_recursivo(nodo_actual.derecho)


