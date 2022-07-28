#-------------------------------------------------------------------------------
# Name:        Proyecto Correlativas
# Purpose:     Hoja de Ruta
# Author:      MARTINEZ LEONARDO
# Created:     27/07/2022
# Copyright:   (c) Leo Marti 2022
#-------------------------------------------------------------------------------

from listas import *
from funciones import *


def estaElegida(ii, elegida):
	for e in elegida:
		if ii == e:
			return True
	return False



def conformarRuta():
	# materiasRuteadas = []
	materiasParaRutear = []

	# Parte 1: Rutear las Aprobadas
	# Agregar a materias Ruteadas las Aprobadas
	# Sacar de materias las agregadas	
	for i in materias:
		if estaAprobada(i[0]):
			materiasRuteadas.append(registroAprobada(i[0]))
		else:
			if i[0]!=0:
				materiasParaRutear.append(i)

	# parte 2: Elegir las materias se la siguiente etapa
	anio     = 22
	semestre = 2
	sigue    = True
	while len(materiasParaRutear)>0 and sigue:
		disponibles = materiasDisponibles(materiasParaRutear)
		elegida = []

		while sigue:
			print(f"\n\n Disponibles para Año: {anio+2000} en el {semestre}º Semestre")
			for i in disponibles:
				print(f" {materias[i]} ", end=" ")
				if estaElegida(i, elegida):
					print("\t\t ----> ELEGIDA")
				else:
					print(" ")

			print(f" Indicar materias: ")
			elegir = int(input("indica el id:  "))

			if elegir == 0:			
				sigue = False
			else:
				elegida.append(elegir)

		for e in elegida:
			tupla = (e, anio * 10 + semestre, "RU")
			materiasRuteadas.append(tupla)
			for ee in materiasParaRutear:
				if e == ee[0]:
					materiasParaRutear.remove(ee)
					break
						
		if semestre == 2:
			anio += 1
			semestre = 1
		else:
			semestre += 1

		if len(elegida)==0:
			sigue = False
		else:
			sigue = True
			

	for i in materiasRuteadas:
		print(f" {i}  ")

	print("\n\n", materiasParaRutear)



