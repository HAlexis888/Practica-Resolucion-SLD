from sld_practice import *

alimentos = {"pollo", "arroz", "zanahoria"}
# Si comes cereales, leguminosas, verduras o frutas, y alimentos de origen animal 
# entonces tienes un plato bueno para comer.
print(verificar_plato_completo(alimentos))


alimento_en_plato = input("Ingresa un alimento para verificar si esta en el plato del buen comer: ")
print(esta_en_el_plato(alimento_en_plato))