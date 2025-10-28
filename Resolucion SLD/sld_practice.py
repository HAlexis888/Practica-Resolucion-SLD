from base_conocimiento import grupos

def verificar_plato_completo(x, grupos_lista=None):
    if grupos_lista is None:
        frutas_verduras = set(grupos['frutas']) | set(grupos['verduras'])
        leguminosas_animales = set(grupos['leguminosas']) | set(grupos['animales'])
        grupos_lista = [frutas_verduras, set(grupos['cereales']), leguminosas_animales]
                       
    if not grupos_lista:
        return "Tu plato es bueno para comer"
    grupo_actual = grupos_lista[0]
    x_set = set(x) if isinstance(x, list) else x
    if not (x_set & grupo_actual):
        return "Tu plato no es bueno para comer"  
    return verificar_plato_completo(x, grupos_lista[1:])

def esta_en_el_plato(x, grupos_lista=None, indice=0):
    if grupos_lista is None:
        grupos_lista = list(grupos.values())  
    # Revisa los grupos para encontrar el alimento
    if indice >= len(grupos_lista):
        return "Tu alimento no esta en el plato del buen comer"
    # En caso de encontrar el alimento
    if x in grupos_lista[indice]:
        return "Tu alimento esta en el plato"    
    return esta_en_el_plato(x, grupos_lista, indice + 1)