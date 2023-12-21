
from heapq import heappop, heappush
import networkx as nx
import matplotlib.pyplot as plt

class Grafo:
    def __init__(self):
        self.ciudades = {}  # Diccionario para almacenar las ciudades y sus conexiones
        self.distancias_bst = None  # Árbol binario de búsqueda para las distancias

    def agregar_ciudad(self, ciudad):
        if ciudad not in self.ciudades:
            self.ciudades[ciudad] = {}

    def agregar_conexion(self, ciudad1, ciudad2, distancia):
        if ciudad1 in self.ciudades and ciudad2 in self.ciudades:
            self.ciudades[ciudad1][ciudad2] = distancia
            self.ciudades[ciudad2][ciudad1] = distancia

            # Agregar la distancia al BST
            self.agregar_distancia_bst(distancia, ciudad1, ciudad2)

    def mostrar_grafo(self):
        for ciudad, conexiones in self.ciudades.items():
            print(f"{ciudad}: {conexiones}")

    def agregar_distancia_bst(self, distancia, ciudad1, ciudad2):
        if self.distancias_bst is None:
            self.distancias_bst = BST(distancia, ciudad1, ciudad2)
        else:
            self.distancias_bst.insert(distancia, ciudad1, ciudad2)

    def ruta_mas_corta(self, origen, destino):
        distancias = {ciudad: float('inf') for ciudad in self.ciudades}
        distancias[origen] = 0
        cola_prioridad = [(0, origen)]
        padre = {origen: None}

        while cola_prioridad:
            actual_dist, actual_ciudad = heappop(cola_prioridad)

            if actual_ciudad == destino:
                ruta = []
                while actual_ciudad is not None:
                    ruta.insert(0, actual_ciudad)
                    actual_ciudad = padre[actual_ciudad]
                return ruta, distancias[destino]

            for vecino, peso in self.ciudades[actual_ciudad].items():
                nueva_distancia = distancias[actual_ciudad] + peso
                if nueva_distancia < distancias[vecino]:
                    distancias[vecino] = nueva_distancia
                    padre[vecino] = actual_ciudad
                    heappush(cola_prioridad, (nueva_distancia, vecino))

        return None, None

    def mostrar_registro_distancias(self):
        if self.distancias_bst:
            self._inorden(self.distancias_bst.raiz)

    def _inorden(self, nodo):
        if nodo:
            self._inorden(nodo.izquierda)
            print(f"Distancia: {nodo.distancia}, Ciudades: {nodo.ciudad1}, {nodo.ciudad2}")
            self._inorden(nodo.derecha)

    def arbol_recubrimiento_minimo(self):
        aristas = []

        for ciudad1, conexiones in self.ciudades.items():
            for ciudad2, distancia in conexiones.items():
                aristas.append((distancia, ciudad1, ciudad2))

        aristas.sort()

        arbol_recubrimiento = Grafo()
        for arista in aristas:
            distancia, ciudad1, ciudad2 = arista
            if not arbol_recubrimiento.hay_ciclo(ciudad1, ciudad2):
                arbol_recubrimiento.agregar_ciudad(ciudad1)
                arbol_recubrimiento.agregar_ciudad(ciudad2)
                arbol_recubrimiento.agregar_conexion(ciudad1, ciudad2, distancia)

        return arbol_recubrimiento

    def hay_ciclo(self, ciudad1, ciudad2):
        padre = {}
        rango = {}

        def encontrar(ciudad):
            if padre[ciudad] != ciudad:
                padre[ciudad] = encontrar(padre[ciudad])
            return padre[ciudad]

        def unir(conjunto1, conjunto2):
            raiz1 = encontrar(conjunto1)
            raiz2 = encontrar(conjunto2)

            if rango[raiz1] < rango[raiz2]:
                padre[raiz1] = raiz2
            elif rango[raiz1] > rango[raiz2]:
                padre[raiz2] = raiz1
            else:
                padre[raiz1] = raiz2
                rango[raiz2] += 1

        for ciudad in self.ciudades:
            padre[ciudad] = ciudad
            rango[ciudad] = 0

        for ciudad1, conexiones in self.ciudades.items():
            for ciudad2 in conexiones:
                if encontrar(ciudad1) == encontrar(ciudad2):
                    return True
                unir(ciudad1, ciudad2)

        return False

    def visualizar_grafo(self):
        G = nx.Graph()

        for ciudad, conexiones in self.ciudades.items():
            for vecino, distancia in conexiones.items():
                G.add_edge(ciudad, vecino, weight=distancia)

        pos = nx.spring_layout(G)  # Puedes cambiar el layout según tus preferencias
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw(G, pos, with_labels=True, font_weight='bold')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.show()

    def visualizar_arbol_recubrimiento(self):
        G = nx.Graph()

        for ciudad, conexiones in self.ciudades.items():
            for vecino, distancia in conexiones.items():
                G.add_edge(ciudad, vecino, weight=distancia)

        pos = nx.spring_layout(G)  # Puedes cambiar el layout según tus preferencias
        labels = nx.get_edge_attributes(G, 'weight')
        mst_edges = self.obtener_aristas_arbol_recubrimiento()
        mst_labels = {(ciudad1, ciudad2): labels[(ciudad1, ciudad2)] for ciudad1, ciudad2 in mst_edges}
        nx.draw(G, pos, with_labels=True, font_weight='bold', edgelist=mst_edges)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=mst_labels)
        plt.show()

    def obtener_aristas_arbol_recubrimiento(self):
        aristas = []

        for ciudad1, conexiones in self.ciudades.items():
            for ciudad2, distancia in conexiones.items():
                aristas.append((ciudad1, ciudad2, distancia))

        aristas.sort(key=lambda x: x[2])

        aristas_mst = []
        conjunto_ciudades = set()

        for arista in aristas:
            ciudad1, ciudad2, distancia = arista
            if ciudad1 not in conjunto_ciudades or ciudad2 not in conjunto_ciudades:
                aristas_mst.append((ciudad1, ciudad2))
                conjunto_ciudades.update([ciudad1, ciudad2])

        return aristas_mst



class NodoBST:
    def __init__(self, distancia, ciudad1, ciudad2):
        self.distancia = distancia
        self.ciudad1 = ciudad1
        self.ciudad2 = ciudad2
        self.izquierda = None
        self.derecha = None

class BST:
    def __init__(self, distancia, ciudad1, ciudad2):
        self.raiz = NodoBST(distancia, ciudad1, ciudad2)

    def insert(self, distancia, ciudad1, ciudad2):
        self._insert_recursivo(self.raiz, distancia, ciudad1, ciudad2)

    def _insert_recursivo(self, nodo, distancia, ciudad1, ciudad2):
        if distancia < nodo.distancia:
            if nodo.izquierda is None:
                nodo.izquierda = NodoBST(distancia, ciudad1, ciudad2)
            else:
                self._insert_recursivo(nodo.izquierda, distancia, ciudad1, ciudad2)
        elif distancia > nodo.distancia:
            if nodo.derecha is None:
                nodo.derecha = NodoBST(distancia, ciudad1, ciudad2)
            else:
                self._insert_recursivo(nodo.derecha, distancia, ciudad1, ciudad2)

# Ejemplo de uso
grafo = Grafo()

# Agregar ciudades
grafo.agregar_ciudad("A")
grafo.agregar_ciudad("B")
grafo.agregar_ciudad("C")
grafo.agregar_ciudad("D")
grafo.agregar_ciudad("E")

# Agregar conexiones con distancias
grafo.agregar_conexion("A", "B", 2)
grafo.agregar_conexion("A", "C", 4)
grafo.agregar_conexion("B", "C", 1)
grafo.agregar_conexion("B", "D", 7)
grafo.agregar_conexion("C", "D", 3)
grafo.agregar_conexion("C", "E", 5)
grafo.agregar_conexion("D", "E", 8)

# Mostrar el grafo
print("Grafo:")
grafo.mostrar_grafo()

# Encontrar la ruta más corta entre dos ciudades
origen = "A"
destino = "E"
ruta, distancia_total = grafo.ruta_mas_corta(origen, destino)
print(f"\nRuta más corta desde {origen} hasta {destino}:")
print(f"Ruta: {ruta}")
print(f"Distancia total: {distancia_total}")

# Mostrar el registro ordenado de distancias
print("\nRegistro ordenado de distancias:")
grafo.mostrar_registro_distancias()

# Encontrar el Árbol de Recubrimiento Mínimo
arbol_recubrimiento = grafo.arbol_recubrimiento_minimo()
print("\nÁrbol de Recubrimiento Mínimo:")
arbol_recubrimiento.mostrar_grafo()
