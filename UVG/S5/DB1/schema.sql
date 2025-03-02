CREATE TABLE Hospital (
id_hospital SERIAL PRIMARY KEY,
nombre VARCHAR(255) NOT NULL,
direccion TEXT NOT NULL
);
CREATE TABLE Pacientes (
id_paciente SERIAL PRIMARY KEY,
nombre VARCHAR(255) NOT NULL,
fecha_nacimiento DATE NOT NULL,
direccion TEXT,
telefono VARCHAR(20),
id_hospital INT,
FOREIGN KEY (id_hospital) REFERENCES Hospital(id_hospital)
);
CREATE TABLE Medicos (
id_medico SERIAL PRIMARY KEY,
nombre VARCHAR(255) NOT NULL,
especialidad VARCHAR(100) NOT NULL,
telefono VARCHAR(20),
id_hospital INT,
FOREIGN KEY (id_hospital) REFERENCES Hospital(id_hospital)
);
CREATE TABLE Citas (
id_cita SERIAL PRIMARY KEY,
id_paciente INT,
id_medico INT,
fecha_hora TIMESTAMP NOT NULL,
estado VARCHAR(50) CHECK (estado IN ('Pendiente', 'Atendida', 'Cancelada')) NOT
NULL,
FOREIGN KEY (id_paciente) REFERENCES Pacientes(id_paciente),
FOREIGN KEY (id_medico) REFERENCES Medicos(id_medico)
);
CREATE TABLE Consulta (
id_consulta SERIAL PRIMARY KEY,
id_cita INT,
diagnostico TEXT,
observaciones TEXT,
FOREIGN KEY (id_cita) REFERENCES Citas(id_cita)
);
CREATE TABLE Tratamiento_Maestro (
id_tratamiento_maestro SERIAL PRIMARY KEY,
id_consulta INT,
fecha_inicio DATE NOT NULL,
fecha_fin DATE,
FOREIGN KEY (id_consulta) REFERENCES Consulta(id_consulta)
);
CREATE TABLE Tratamiento_Detalle (
id_tratamiento_detalle SERIAL PRIMARY KEY,
id_tratamiento_maestro INT,
medicamento VARCHAR(255) NOT NULL,
dosis VARCHAR(50) NOT NULL,
frecuencia VARCHAR(50) NOT NULL,
FOREIGN KEY (id_tratamiento_maestro) REFERENCES
Tratamiento_Maestro(id_tratamiento_maestro)
);
CREATE TABLE Factura_Maestro (
id_factura_maestro SERIAL PRIMARY KEY,
id_paciente INT,
fecha_emision DATE NOT NULL,
total DECIMAL(10,2) NOT NULL,
FOREIGN KEY (id_paciente) REFERENCES Pacientes(id_paciente)
);
CREATE TABLE Factura_Detalle (
id_factura_detalle SERIAL PRIMARY KEY,
id_factura_maestro INT,
descripcion VARCHAR(255) NOT NULL,
cantidad INT NOT NULL,
precio_unitario DECIMAL(10,2) NOT NULL,
FOREIGN KEY (id_factura_maestro) REFERENCES
Factura_Maestro(id_factura_maestro)
);
CREATE TABLE Usuarios (
id_usuario SERIAL PRIMARY KEY,
nombre_usuario VARCHAR(100) UNIQUE NOT NULL,
clave_hash VARCHAR(255) NOT NULL,
id_hospital INT,
FOREIGN KEY (id_hospital) REFERENCES Hospital(id_hospital)
);
CREATE TABLE Perfiles_Roles_Usuarios (
id_perfil SERIAL PRIMARY KEY,
id_usuario INT,
rol VARCHAR(50) NOT NULL,
FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario)
);
CREATE TABLE Usuarios_Menu (
id_menu SERIAL PRIMARY KEY,
id_usuario INT,
menu VARCHAR(100) NOT NULL,
FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario)
);
-- Creación de las tablas de bitácora
CREATE TABLE Bitacora (
id_bitacora SERIAL PRIMARY KEY,
fecha_hora TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
usuario VARCHAR(100) NOT NULL,
tabla_afectada VARCHAR(100) NOT NULL,
operacion VARCHAR(50) CHECK (operacion IN ('SELECT', 'INSERT', 'UPDATE',
'DELETE')) NOT NULL,
id_registro_afectado INT,
detalles TEXT
);
CREATE TABLE Perfiles_Roles_Usuarios (
id_perfil SERIAL PRIMARY KEY,
id_usuario INT,
rol VARCHAR(50) NOT NULL,
FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario)
);
CREATE TABLE Usuarios_Menu (
id_menu SERIAL PRIMARY KEY,
id_usuario INT,
menu VARCHAR(100) NOT NULL,
FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario)
);
-- Creación de las tablas de bitácora
CREATE TABLE Bitacora (
id_bitacora SERIAL PRIMARY KEY,
fecha_hora TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
usuario VARCHAR(100) NOT NULL,
tabla_afectada VARCHAR(100) NOT NULL,
operacion VARCHAR(50) CHECK (operacion IN ('SELECT', 'INSERT', 'UPDATE',
'DELETE')) NOT NULL,
id_registro_afectado INT,
detalles TEXT);
