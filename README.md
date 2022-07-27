# Proyecto Correlativas

## Origen
Se inicia el proyecto a partir de las materias de la carrera *Licenciatura en Sistemas* de la UNGS.

## Insumos
Se utiliza una lista de materias y una lista de correlativas

La lista **materias** es un *array* de *tuplas*. Ejemplo: 

* Materias = [
	* (0, ''),
	* (1, 'Taller Inicial Común: Taller de Lectura y Escritura'), 
	* (2, 'Taller Inicial Orientado: Ciencias Exactas'), 
	* (3, 'Taller Inicial Obligatorio del Área de Matemática'), 
	* (4, 'Introducción a la Programación'), 
	* (5, 'Introducción a la Matemática'), 
	* (6, 'Taller de Lectura y Escritura en las Disciplinas'), 
	* (7, 'Programación I'), 
	]

La primera con orden cero no tiene valor. Entonces coincide el **Id** de la materia con el orden de la lista. 

> La lista de **correlativas** es un *array* de *tuplas*  

Cada tupla refiere a la materia y su correlativa. Puede haber varias tuplas con la misma materia. solo cambia la correlativa. En los siguientes ejemplos se ve como la materia 5 y 7 tiene 2 correlativas. Para la 5 su correlativas son las materias 2 y 3. Para la materia 7 necesita la 4 y la 1.

* Correlativas = [
	* (1, 0), 
	* (2, 0), 
	* (3, 0), 
	* (4, 2), 
	* (4, 3), 
	* (5, 2), 
	* (5, 3), 
	* (6, 1), 
	* (7, 4), 
	* (7, 1), 
	* (8, 5), 
	]

Si la *correlativa* es:

| correlativa | significado |
|-------------|-------------|
| 0 (cero)    | no tiene | 
| de 1 a 36   | Corresponda a la materia en cuestion | 
| 40          | Necesita 14 materias |


## Resultado

1. Dada una materia, obtener las correlativas
2. **Disponibles**: Dala la lista de Materias *Aprobadas* Obtener las siguientes materias que están disponibles.
	- *Materia Disponible*: Es aquella que está primera para cursar y/o aprobar porque tiene sus correlativas cursadas y aprobadas.
3. **Hoja de Ruta**: Por *semestre* obtener listado de materias disponibles. 

## Aprobadas  

> aprobadas = [ (1, 221, 'R'), (2, 221, 'R'), (3, 221, 'R'), (4, 221, 'CA'), (5, 221, 'A'), (15, 221, 'E')]

Son las materias que ya han sido aprobadas por distintas circunstancias.

Sse forma con una *tupla* 

| Materia | Año y Semestre | Codigo | Circunstancia | 
|---------|----------------|--------|---------------|
| 1       | 22 .... 1      |  'R'   |  Resolución   |
| 4       | 22 .... 1      |  'CA'  |  Cursada y Aprobada   |
| 15      | 22 .... 1      |  'E'   |  Equivalencia |

