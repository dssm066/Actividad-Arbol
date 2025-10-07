# pip install bigtree   ← Solo necesitas esto

from bigtree import Node, print_tree

def peso(nodo):
    """Cuenta todos los nodos del árbol (peso)."""
    if not nodo:
        return 0
    total = 1
    for hijo in nodo.children:
        total += peso(hijo)
    return total

def orden(nodo):
    """Devuelve el número máximo de hijos que tiene algún nodo (orden)."""
    if not nodo:
        return 0
    max_hijos = len(nodo.children)
    for hijo in nodo.children:
        max_hijos = max(max_hijos, orden(hijo))
    return max_hijos

def altura(nodo):
    """Calcula la altura del árbol (número de niveles)."""
    if not nodo or not nodo.children:
        return 1
    return 1 + max(altura(hijo) for hijo in nodo.children)

def main():
    raiz_valor = input("Ingrese el valor de la raíz: ").strip()
    raiz = Node(raiz_valor)
    nodos = {raiz_valor: raiz}

    print("\nAgregue relaciones padre-hijo (escriba 'fin' para terminar):")
    while True:
        padre = input("Padre (o 'fin' para terminar): ").strip()
        if padre.lower() == "fin":
            break
        if padre not in nodos:
            print(f"El nodo padre '{padre}' no existe.")
            continue
        hijo = input(f"Hijo de {padre}: ").strip()
        nuevo_hijo = Node(hijo, parent=nodos[padre])
        nodos[hijo] = nuevo_hijo

    print("\n---  Árbol creado ---")
    print_tree(raiz)  # imprime el árbol en texto

    print("\n---  Propiedades ---")
    print("Peso del árbol:", peso(raiz))
    print("Orden del árbol:", orden(raiz))
    print("Altura del árbol:", altura(raiz))

if __name__ == "__main__":
    main()
