#-------------------------------------------------------------------------------
# Name:        Proyecto Correlativas
# Purpose:     Funciones
# Author:      MARTINEZ LEONARDO
# Created:     26/07/2022
# Copyright:   (c) Leo Marti 2022
#-------------------------------------------------------------------------------

from listas import *


def mostrarMaterias():
	print(f"Cantidad de Materias {len(materias)-1} ")
	for i in range(1,len(materias)):
		print(f"{materias[i][0]:3d} - {materias[i][1]} ")


def buscarCorrelativa(id):
	corr = []
	for i in range(len(correlativas)):
		if (correlativas[i][0] == id):
			corr.append(correlativas[i][1])
	return corr	
