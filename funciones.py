#-------------------------------------------------------------------------------
# Name:        Proyecto Correlativas
# Purpose:     Funciones
# Author:      MARTINEZ LEONARDO
# Created:     26/07/2022
# Copyright:   (c) Leo Marti 2022
#-------------------------------------------------------------------------------

from listas import *

materiasRuteadas= []

def mostrarMaterias():
	print(f"Cantidad de Materias {len(materias)-1} ")
	for i in range(1,len(materias)):
		print(f"{materias[i][0]:3d} - {materias[i][1]} ")


def encontrarCorrelativa(id):
	corr = []
	for i in range(len(correlativas)):
		if (correlativas[i][0] == id):
			corr.append(correlativas[i][1])
	return corr	

def buscarcorrelativa():
	idMateria = int(input("Ingrese un materia: "))
	print(f"Correlativas de: {idMateria:3d} {materias[idMateria][1]}")
	lsCorrelativa = ( encontrarCorrelativa(idMateria))
	for i in range( len (lsCorrelativa)):
		print(f"\t {lsCorrelativa[i]:3d} {materias[lsCorrelativa[i]][1]} ")


def mostrarAprobadas():
	print("Materias Aprobadas")
	print("------------------")
	periodo=0
	for i in range(len(aprobadas)):
		id = aprobadas[i][0]
		if (periodo != aprobadas[i][1]):
			periodo = aprobadas[i][1]
			anio = int(str(periodo)[:2])+2000
			semestre = str(periodo)[2]
			print(f"\t Año: {anio} \t Semestre: {semestre}")
		print(f"\t {id:3d} {materias[aprobadas[i][0]][1]} ")


def estaAprobada(id):
	for i in range(len(aprobadas)):
		if (aprobadas[i][0] == id):
			return True
	return False


def estaRuteada(id):
	for i in range(len(materiasRuteadas)):
		if (materiasRuteadas[i][0] == id):
			return True
	return False



def registroAprobada(id):
	for i in aprobadas:
		if (i[0]==id):
			return i
	return None



def repiteDisponible(dispo, m):
	for ma in dispo:
		if ma == m:
			return True
	return False


def tieneAprobadaCorrelativas(correl):
	for k in correl:
		if not estaAprobada(k):
			return False	
	return True


def tieneRuteadaCorrelativas(correl):
	for k in correl:
		if not estaRuteada(k):
			return False	
	return True



def mostrarDisponibles():
	print("Materias Están disponibles")
	print("--------------------------")
	disponibles = []
	for i in materias:
		if not estaAprobada(i[0]) and i[0]>0 :
			correlativa = encontrarCorrelativa(i[0])
			if tieneAprobadaCorrelativas(correlativa) and not repiteDisponible(disponibles, i[0]):
				disponibles.append(i[0])
	if (len(disponibles)>0):
		for i in disponibles:
			print(f"\t {i:3d} {materias[i][1]} ")


def materiasDisponibles(mater1as):
	disponibles = []
	for i in mater1as:
		correlativa = encontrarCorrelativa(i[0])
		if tieneRuteadaCorrelativas(correlativa) and not repiteDisponible(disponibles, i[0]):
			disponibles.append(i[0])
	return disponibles



