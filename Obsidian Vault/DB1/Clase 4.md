# Introducción a las Bases de Datos

## ¿Qué es una llave primaria?

Una **llave primaria** es aquel atributo (o atributos) que se utiliza para identificar de forma única los demás atributos que describen a una entidad.

### Ejemplo 1: Entidad ALUMNO

La entidad **ALUMNO** podría tener los siguientes atributos o campos:  
- **Carnet**  
- Nombre  
- Dirección  
- Teléfono  

De estos atributos, el **Carnet** puede designarse como llave primaria, ya que es único para cada alumno y permite identificarlo de forma inequívoca dentro de la entidad.

### Ejemplo 2: Entidad CURSO

La entidad **CURSO** podría tener los siguientes atributos o campos:  
- **Código**  
- Nombre  
- Créditos  

En este caso, el atributo **Código** sería la llave primaria, ya que identifica de forma única a cada curso.

---

## ¿Qué es una llave foránea?

Una **llave foránea** es uno o más campos de una tabla que hacen referencia al campo o a los campos de la llave primaria de otra tabla. Las llaves foráneas indican cómo están relacionadas las entidades.

### Características de las llaves foráneas:
- Los datos en los atributos de la llave primaria y la llave foránea deben coincidir en tipo de dato y tamaño.  
- No es necesario que los nombres de los atributos coincidan.

### Ejemplo: Relación entre CLIENTE y FACTURA

En la entidad **CLIENTE**, la llave primaria es:  
- **No_Cliente**  

En la entidad **FACTURA**, la llave foránea es:  
- **Cod_Cliente**  

En este caso, el valor de **Cod_Cliente** en la tabla FACTURA indica el cliente al que pertenece dicha factura.

# DBMS (Sistema de Gestión de Bases de Datos)

## Bases de Datos Relacionales vs No Relacionales

### Bases de Datos Relacionales
- **Estructura fija**: Los datos se organizan en tablas con columnas y filas.
- Usan **SQL** como estándar para la consulta y manipulación de datos.
- Son **ideales para aplicaciones transaccionales**, donde la consistencia y las relaciones entre datos son esenciales.

---

### Bases de Datos No Relacionales
- **Flexibilidad**: Soportan datos no estructurados, como documentos JSON, pares clave-valor, grafos, entre otros.
- Permiten **escalabilidad horizontal**, facilitando la distribución de datos en múltiples servidores.
- Son **ideales para Big Data** y aplicaciones que requieren procesamiento en **tiempo real**.

---

## Clasificación por Tipo de Uso

### Centralizados
- Toda la base de datos se encuentra en un solo lugar.

### Distribuidos
- Los datos están replicados o fragmentados en múltiples ubicaciones.  
- **Ejemplo**: Amazon DynamoDB.

### En Memoria
- Los datos se almacenan en RAM para mayor velocidad.  
- **Ejemplo**: Redis.

---

## Arquitectura de un DBMS

### Monolítica
- Todo integrado en una instancia.  
- **Ejemplo**: SQLite.

### Cliente-Servidor
- Separación entre cliente y almacenamiento.  
- **Ejemplo**: MySQL.

### Multinivel
- Diseñado para grandes sistemas empresariales.  
- **Ejemplo**: Oracle.

---

## ¿Cómo Funciona un DBMS?

1. El usuario envía una consulta.  
2. El DBMS interpreta la consulta y planifica su ejecución.  
3. El motor de almacenamiento accede a los datos requeridos.  
4. Se envían los resultados al usuario.

---

## Almacenamiento de Datos

- **Tablas**: Organizan datos en filas y columnas.  
- **Índices**: Mejoran la velocidad de búsqueda.  
- **Espacios de Tablas (Tablespaces)**:  
  - Son las unidades lógicas que agrupan uno o más archivos físicos.  
  - Proveen **segregación** y **seguridad** para los datos.  
  - Donde residen físicamente las tablas e índices.


# Ejercicio 1 - Modelo Relacional

## Parte #1
### 1)
- Identifique las claves primarias y foráneas en ambas tablas. 
	clientes: id es la primaria
	pedidos: id es la primaria, cliente_id es la foránea
- Describa la relación entre las tablas. 
	La tabla de pedidos tiene una relacion con clientes, esta relaciona el id tabla cliente (llave primaria) con cliente_id (llave foránea)
- ¿Qué ocurriría si se elimina un cliente que tiene pedidos asociados?
	Se eliminan las tuplas que tengan relación con los pedidos en la tabla pedidos.

### 2)
- Identifique las claves primarias y foráneas en todas las tablas.
	libros: 
		llave primaria: id
	prestamos: 
		llave primaria: id 
		llave foránea; libro_id, usuario_id
	usuarios:
		llave primaria: id
- Describa las relaciones entre las tablas.
	Prestamos es la tabla que une las otras 2, teniendo como llave foránea libro_id y usuario_id, correspondiendo a las llaves primarias del campo id de las tablas y libros

### 3)

- Identifique las claves primarias y foráneas en las tablas.
	cursos:
		llave primaria: id
	profesores:
		llave primaria: id
	asignaciones:
		llave primaria: id
		llave foránea: curso_id, profesor_id
- Explique la relación entre las 3 tablas
	asignaciones es la tabla que une las otras 2, teniendo como llave foránea curso_id y profesor_id, correspondiendo a las llaves primarias del campo id de las cursos y asignaciones.

## Parte #2
### Sistema de Tienda en Línea

#### Tablas
###### 1. Usuarios
- usuario_id (Primaria)
- email
- nombre
- apellido
- direccion
- telefono
- fecha_registro

###### 2. Productos
- producto_id (Primaria)
- categoria_id (Foránea)
- nombre
- descripcion
- precio
- stock
- imagen_url

###### 3. Categorias
- categoria_id (Primaria)
- nombre
- descripcion

###### 4. Pedidos
- pedido_id (Primaria)
- usuario_id (Foránea)
- fecha_pedido
- estado
- total

###### 5. Detalles_Pedido
- detalle_id (Primaria)
- pedido_id (Foránea)
- producto_id (Foránea)
- cantidad
- precio_unitario
- subtotal

#### Relaciones
1. Productos y Categorias
	- Productos.categoria_id → Categorias.categoria_id
	- Relación: Muchos a Uno

2. Pedidos y Usuarios
	- Pedidos.usuario_id → Usuarios.usuario_id
	- Relación: Muchos a Uno

3. Detalles_Pedido y Pedidos
	- Detalles_Pedido.pedido_id → Pedidos.pedido_id
	- Relación: Muchos a Uno

4. Detalles_Pedido y Productos
	- Detalles_Pedido.producto_id → Productos.producto_id
	- Relación: Muchos a Uno


### Sistema de Universidad

#### Tablas
###### 1. Estudiantes
- estudiante_id (Primaria)
- matricula
- nombre
- apellido
- fecha_nacimiento
- email
- telefono

###### 2. Profesores
- profesor_id (Primaria)
- numero_empleado
- nombre
- apellido
- email
- departamento_id (Foránea)

###### 3. Departamentos
- departamento_id (Primaria)
- nombre
- director_id (Foránea)
- ubicacion

###### 4. Cursos
- curso_id (Primaria)
- departamento_id (Foránea)
- nombre
- codigo
- creditos

###### 5. Seccion
- seccion_id (Primaria)
- curso_id (Foránea)
- profesor_id (Foránea)
- semestre
- horario
- aula

###### 6. Inscripciones
- inscripcion_id (Primaria)
- estudiante_id (Foránea)
- Seccion_id (Foránea)
- calificacion
- fecha_inscripcion

###### 7. Carreras
- carrera_id (Primaria)
- nombre
- departamento_id (Foránea)
- duracion_semestres

#### Relaciones
1. Profesores y Departamentos
	- Profesores.departamento_id → Departamentos.departamento_id
	- Relación: Muchos a Uno

2. Departamentos y Profesores
	- Departamentos.director_id → Profesores.profesor_id
	- Relación: Uno a Uno

3. Cursos y Departamentos
	- Cursos.departamento_id → Departamentos.departamento_id
	- Relación: Muchos a Uno

4. Seccion y Cursos
	- Seccion.curso_id → Cursos.curso_id
	- Relación: Muchos a Uno

5. Seccion y Profesores
	- Seccion.profesor_id → Profesores.profesor_id
	- Relación: Muchos a Uno

6. Inscripciones y Estudiantes
	- Inscripciones.estudiante_id → Estudiantes.estudiante_id
	- Relación: Muchos a Uno

7. Inscripciones y Seccion
	- Inscripciones.Seccion_id → Seccion.seccion_id
	- Relación: Muchos a Uno

8. Carreras y Departamentos
	- Carreras.departamento_id → Departamentos.departamento_id
	- Relación: Muchos a Uno


### Sistema de Hospital

#### Tablas
###### 1. Pacientes
- paciente_id (Primaria)
- nombre
- apellido
- fecha_nacimiento
- genero
- direccion
- telefono
- email

###### 2. Médicos
- medico_id (Primaria)
- nombre
- apellido
- especialidad_id (Foránea)
- telefono
- email

###### 3. Especialidades
- especialidad_id (Primaria)
- nombre
- descripcion

###### 4. Citas
- cita_id (Primaria)
- paciente_id (Foránea)
- medico_id (Foránea)
- fecha_hora
- motivo
- estado

###### 5. Historiales_Médicos
- historial_id (Primaria)
- paciente_id (Foránea)
- fecha_creacion
- grupo_sanguineo
- alergias
- antecedentes

###### 6. Consultas
- consulta_id (Primaria)
- cita_id (Foránea)
- diagnostico
- tratamiento
- notas
- fecha_consulta

###### 7. Medicamentos
- medicamento_id (Primaria)
- nombre
- descripcion
- fabricante
- stock
- precio

###### 8. Recetas
- receta_id (Primaria)
- consulta_id (Foránea)
- fecha_emision
- fecha_vencimiento

###### 9. Detalles_Receta
- detalle_id (Primaria)
- receta_id (Foránea)
- medicamento_id (Foránea)
- dosis
- frecuencia
- duracion

###### 10. Internaciones
- internacion_id (Primaria)
- paciente_id (Foránea)
- habitacion_id (Foránea)
- medico_id (Foránea)
- fecha_ingreso
- fecha_alta
- motivo
- estado

#### Relaciones
1. Médicos y Especialidades
	- Médicos.especialidad_id → Especialidades.especialidad_id
	- Relación: Muchos a Uno

2. Citas y Pacientes
	- Citas.paciente_id → Pacientes.paciente_id
	- Relación: Muchos a Uno

3. Citas y Médicos
	- Citas.medico_id → Médicos.medico_id
	- Relación: Muchos a Uno

4. Historiales_Médicos y Pacientes
	- Historiales_Médicos.paciente_id → Pacientes.paciente_id
	- Relación: Uno a Uno

5. Consultas y Citas
	- Consultas.cita_id → Citas.cita_id
	- Relación: Uno a Uno

6. Recetas y Consultas
	- Recetas.consulta_id → Consultas.consulta_id
	- Relación: Muchos a Uno

7. Detalles_Receta y Recetas
	- Detalles_Receta.receta_id → Recetas.receta_id
	- Relación: Muchos a Uno

8. Detalles_Receta y Medicamentos
	- Detalles_Receta.medicamento_id → Medicamentos.medicamento_id
	- Relación: Muchos a Uno

9. Internaciones y Pacientes
	- Internaciones.paciente_id → Pacientes.paciente_id
	- Relación: Muchos a Uno

10. Internaciones y Médicos
	- Internaciones.medico_id → Médicos.medico_id
	- Relación: Muchos a Uno




