# Base de Datos Relacional (BD Relacional)

Una **base de datos relacional** es un conjunto de información perteneciente a un mismo contexto, ordenada de manera sistemática para facilitar su recuperación y análisis. Sus principios fundamentales son:  

- **Confidencialidad**: Asegurar que la información solo esté disponible para quienes tengan autorización.  
- **Integridad**: Garantizar la precisión y consistencia de los datos almacenados.  
- **Disponibilidad**: Asegurar que los datos estén accesibles cuando se necesiten.  

---

## Conceptos Clave  

### **Entidad**  
Cualquier cosa de interés que necesita ser representada dentro de la base de datos, relacionada con una operación empresarial o requerimiento.  

### **Antes y Ahora**  
- Anteriormente, las entidades se representaban como "tablas".  
- Los campos ahora son conocidos como "atributos".  

Ejemplo de tabla:  

| **Campo 1** | **Campo 2** | **Campo 3** |
| ----------- | ----------- | ----------- |
| a           | b           | c           |

- Las filas de la tabla se denominan **tuplas** (representan un registro individual de datos).  

---

### **Campos Compuestos**  
Un **campo compuesto** es una combinación de varios campos (atributos). Este tipo de campo puede dividirse en subpartes para formar jerarquías.  

Por ejemplo:  
- Dirección:  
  - Calle  
  - Número  
  - Ciudad  

---

### **Tupla**  
Una **tupla** es un conjunto de datos almacenados de forma secuencial en una fila. Se utiliza para agrupar varios valores como si fueran un único valor.  

Ejemplo:  
`(1, "Juan", "López")`  
Aquí, la tupla agrupa un ID, un nombre y un apellido.  

---

### **Claves**  
Las **claves** son campos o conjuntos de campos de una entidad que identifican de manera única un registro.  

- Los valores de una clave no pueden repetirse entre registros de la misma entidad.  
- Tipos de claves:  
  - **Clave primaria**: Identificador único para cada registro, es univoca.  

#### **Claves Candidatas y Clave Primaria**  
- Dentro de los campos que cumplen con la condición de identificar un registro de forma única, se les llama **claves candidatas**.  
- De estas, el diseñador elige una para que sea la **clave primaria**.  

#### **Clave Compuesta**  
La clave primaria puede estar formada por más de un campo. Esto se denomina **clave compuesta**.  

---

## Relaciones  

### **Relaciones entre Entidades**  
- Una relación corresponde a la asociación entre dos entidades.  
- El símbolo universal para representar una relación es un **rombo**.  

Ejemplo:  
- Persona **posee** Auto.  
- Auto **pertenece a** Persona.  

### **Campos en Relaciones**  
En ocasiones, algunos campos no son propios de ninguna de las entidades, sino de la relación en sí.  

Ejemplo:  
- Relación "Compra":  
  - Campo: Fecha de compra.  
  - La fecha pertenece al hecho de la compra, no a la Persona ni al Auto.  
  - Estos campos se representan igual que los campos de las entidades, pero se colocan dentro de la relación.  

---

### **Cardinalidad**  
La cardinalidad define la cantidad de asociaciones que pueden existir entre dos tipos de registros de datos.  

Tipos de cardinalidad:  
1. **Uno a Uno**:  
   - Un registro de una entidad A se relaciona con solo un registro de una entidad B.  

2. **Uno a Muchos**:  
   - Un registro de una entidad A se relaciona con varios registros de una entidad B.  

3. **Muchos a Muchos**:  
   - Un registro de una entidad A se relaciona con varios registros de una entidad B, y viceversa.  
   - En este caso, las dos tablas no pueden estar relacionadas directamente; se necesita crear una **tabla intermedia** que incluya los pares de valores relacionados entre sí.  

---

### **Ejercicio en Clase**  
Agregue a cada uno de los ejemplos campos o atributos y demuestre por qué el tipo de cardinalidad que existe entre las entidades es correcto.

---

#### **Relación Uno a Uno**  
Un registro de una entidad A se relaciona con un único registro de una entidad B.  

**Ejemplo: Vehículo y Matrícula**  

**Vehículo:**  

| **ID** | **Marca** | **Modelo** | **Motor** | **Color** |
| ------ | --------- | ---------- | --------- | --------- |

**Matrícula:**  

| **ID Vehículo** | **Concesionario** | **ID Matrícula** | **Nombre** |
| --------------- | ----------------- | ---------------- | ---------- |

Cada vehículo tiene una única matrícula, y cada matrícula pertenece a un único vehículo.  

---

#### **Relación Uno a Muchos**  
Un registro de una entidad A se relaciona con varios registros de una entidad B.  

**Ejemplo: Departamento y Municipios**  

**Departamento:**  

| **Nombre** | **Tamaño** | **Población** |
| ---------- | ---------- | ------------- |

**Municipio:**  

| **Departamento** | **Nombre** | **Tamaño** | **Población** |
| ---------------- | ---------- | ---------- | ------------- |

Un departamento puede tener varios municipios, pero un municipio pertenece a un solo departamento.  

---

#### **Relación Muchos a Muchos**  
Un registro de una entidad A se relaciona con varios registros de una entidad B, y viceversa.  

**Ejemplo: Estudiantes y Cursos**  

**Estudiante:**  

| **Carné** | **Nombre** | **Apellido** | **Carrera** |
| --------- | ---------- | ------------ | ----------- |

**Curso:**  

| **Código** | **Nombre** | **Capacidad** |
| ---------- | ---------- | ------------- |

En una relación muchos a muchos, es necesario incluir una **entidad auxiliar** para evitar la repetición excesiva de datos.  

**Relación Auxiliar: Asignación (Estudiante-Curso)**  

| **Carné Estudiante** | **Código Curso** |
| -------------------- | ---------------- |

Cada estudiante puede estar inscrito en varios cursos, y cada curso puede tener varios estudiantes inscritos. La entidad auxiliar "Estudiante-Curso" permite manejar esta relación de manera eficiente.  

---

#### **Por qué es necesario usar una Entidad Auxiliar en Muchos a Muchos**  
Si no utilizamos una entidad auxiliar:  
1. Repetiríamos innecesariamente los datos del estudiante o del curso en cada relación, generando redundancia.  
2. En caso de que se elimine un estudiante o curso, podría ser difícil mantener la consistencia de los datos.  


