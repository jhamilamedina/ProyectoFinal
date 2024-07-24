BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "empresas" (
	"empresa_id"	INTEGER,
	"logo"	BLOB,
	"nombre"	TEXT,
	"sede_principal"	TEXT,
	"descripcion"	TEXT,
	"sitio_web"	TEXT,
	"fecha_creacion"	datetime,
	"fecha_actualizacion"	datetime,
	PRIMARY KEY("empresa_id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "departamentos" (
	"departamento_id"	int,
	"nombre"	TEXT,
	PRIMARY KEY("departamento_id")
);
CREATE TABLE IF NOT EXISTS "estrellas" (
	"estrella_id"	INTEGER,
	"empresa_id"	INTEGER,
	"estrella_1"	INTEGER,
	"estrella_2"	INTEGER,
	"estrella_3"	INTEGER,
	"estrella_4"	INTEGER,
	"estrella_5"	INTEGER,
	FOREIGN KEY("empresa_id") REFERENCES "empresas"("empresa_id"),
	PRIMARY KEY("estrella_id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "valoracion" (
	"valoracion_id"	INTEGER,
	"empresa_id"	INTEGER,
	"puntualidad"	INTEGER,
	"seguridad"	INTEGER,
	"economica"	INTEGER,
	"amabilidad"	INTEGER,
	"caro"	INTEGER,
	"inseguro"	INTEGER,
	"impuntual"	INTEGER,
	FOREIGN KEY("empresa_id") REFERENCES "empresas"("empresa_id"),
	PRIMARY KEY("valoracion_id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "usuario" (
	"user_id"	INTEGER NOT NULL UNIQUE,
	"foto_usuario"	BLOB,
	"nombre"	TEXT,
	"email"	TEXT,
	"contraseña"	TEXT,
	"fecha_creacion"	datetime,
	"fecha_actualizacion"	datetime,
	PRIMARY KEY("user_id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "comentarios" (
	"comentario_id"	INTEGER,
	"fecha"	datetime,
	"comentario"	TEXT,
	"user_id"	INTEGER,
	"empresa_id"	INTEGER,
	FOREIGN KEY("user_id") REFERENCES "usuario"("user_id"),
	FOREIGN KEY("empresa_id") REFERENCES "empresas"("empresa_id"),
	PRIMARY KEY("comentario_id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "distritos" (
	"distrito_id"	INTEGER,
	"agenciaslima_id"	INTEGER,
	"provincia_id"	INTEGER,
	"nombre"	TEXT,
	FOREIGN KEY("provincia_id") REFERENCES "provincia"("provincia_id"),
	FOREIGN KEY("agenciaslima_id") REFERENCES "agencias_lima"("agenciaslima_id"),
	PRIMARY KEY("distrito_id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "provincias" (
	"provincia_id"	INTEGER,
	"departamento_id"	INTEGER,
	"nombre"	TEXT,
	FOREIGN KEY("departamento_id") REFERENCES "departamentos"("departamento_id"),
	PRIMARY KEY("provincia_id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "agencias_lima" (
	"agenciaslima_id"	INTEGER,
	"empresa_id"	INTEGER,
	"foto"	BLOB,
	"direccion"	TEXT,
	"horario_de_atencion"	TEXT,
	"telefono"	INTEGER,
	"cochera"	INTEGER,
	FOREIGN KEY("empresa_id") REFERENCES "empresas"("empresa_id"),
	PRIMARY KEY("agenciaslima_id" AUTOINCREMENT)
);
COMMIT;
