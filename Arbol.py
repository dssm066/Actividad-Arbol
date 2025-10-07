# David Santiago Sandoval Mancilla - 2242009
        
class NodoArbol:
    def __init__(self, valor):
        self.valor = valor              # valor de sí mismo
        self.primer_hijo = None         # apuntador al primer hijo
        self.hermano_siguiente = None   # apuntador al siguiente hermano

# ===========================
#  CLASE DEL ÁRBOL
# ===========================

class Arbol:
    def __init__(self, valor_raiz):
        self.raiz = NodoArbol(valor_raiz)
  
    # Buscar un nodo por su valor
    def buscar(self, nodo, valor):
        if nodo is None:
            return None
        
        if nodo.valor == valor:
            return nodo
        
        # buscar entre los hijos
        hijo = nodo.primer_hijo
        
        while hijo:
            encontrado = self.buscar(hijo, valor)
            if encontrado:
                return encontrado
            hijo = hijo.hermano_siguiente
        return None
    
    # Agregar un hijo a un nodo
    def agregar_hijo(self, valor_padre, valor_hijo):
        padre = self.buscar(self.raiz, valor_padre)
        
        if padre is None:
            print(f"No se encontró el nodo con valor '{valor_padre}'")
            return
        
        nuevo = NodoArbol(valor_hijo)

        if padre.primer_hijo is None:
            padre.primer_hijo = nuevo
        else:
            actual = padre.primer_hijo
            while actual.hermano_siguiente:
                actual = actual.hermano_siguiente
            actual.hermano_siguiente = nuevo

    #  Peso del árbol (cantidad de nodos)
    def peso(self, nodo=None):
        if nodo is None:
            nodo = self.raiz
            
        if nodo is None:
            return 0
        
        total = 1
        hijo = nodo.primer_hijo
        
        while hijo:
            total += self.peso(hijo)
            hijo = hijo.hermano_siguiente
        return total

    # Orden del árbol (máx. número de hijos de un nodo)
    def orden(self, nodo=None):
        if nodo is None:
            nodo = self.raiz
            
        if nodo is None:
            return 0

        # contar hijos directos
        contador_hijos = 0
        hijo = nodo.primer_hijo
        
        while hijo:
            contador_hijos += 1
            hijo = hijo.hermano_siguiente

        # comparar con los subárboles
        max_suborden = 0
        hijo = nodo.primer_hijo
        while hijo:
            max_suborden = max(max_suborden, self.orden(hijo))
            hijo = hijo.hermano_siguiente

        return max(contador_hijos, max_suborden)

    #  Altura del árbol (número de niveles)
    def altura(self, nodo=None):
        if nodo is None:
            nodo = self.raiz
        if nodo is None:
            return 0
        if nodo.primer_hijo is None:
            return 1
        
        max_altura = 0
        hijo = nodo.primer_hijo
        while hijo:
            max_altura = max(max_altura, self.altura(hijo))
            hijo = hijo.hermano_siguiente
        return 1 + max_altura

# ===========================
#  INTERFAZ PRINCIPAL
# ===========================

def main():
    raiz = input("Ingrese el valor de la raíz: ")
    arbol = Arbol(raiz)

    print("\nAgregue relaciones padre-hijo (escriba 'fin' para terminar):")
    while True:
        padre = input("Padre (o 'fin' para terminar): ").strip()
        
        if padre.lower() == "fin":
            break
        
        hijo = input("Hijo de " + padre + ": ").strip()
        arbol.agregar_hijo(padre, hijo)

    print("\n--- Resultados ---")
    print("Peso del árbol:", arbol.peso())
    print("Orden del árbol:", arbol.orden())
    print("Altura del árbol:", arbol.altura())

if __name__ == "__main__":
    main()
