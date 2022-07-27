#-------------------------------------------------------------------------------
# Name:        Proyecto Correlativas
# Purpose:     Programa principal
# Author:      MARTINEZ LEONARDO
# Created:     26/07/2022
# Copyright:   (c) Leo Marti 2022
#-------------------------------------------------------------------------------


from listas import *
from funciones import *

# *********************
# Funcion principal
def main():
	#mostrarMaterias()

	idMateria = int(input("Ingrese un materia: "))
	print(f"Correlativas de: {idMateria:3d} {materias[idMateria][1]}")
	lsCorrelativa = ( buscarCorrelativa(idMateria))
	for i in range( len (lsCorrelativa)):
		print(f"\t {lsCorrelativa[i]:3d} {materias[lsCorrelativa[i]][1]} ")




# _______________________________
# *******************************
# Programa Principal ejecuta Main
if __name__ == "__main__":
    main()
    input('Presiona una tecla ... ')

