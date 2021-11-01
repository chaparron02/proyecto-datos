-- Database generated with pgModeler (PostgreSQL Database Modeler).
-- pgModeler  version: 0.9.3
-- PostgreSQL version: 12.0
-- Project Site: pgmodeler.io
-- Model Author: ---

-- Database creation must be performed outside a multi lined SQL file. 
-- These commands were put in this file only as a convenience.
-- 
-- object: new_database | type: DATABASE --
-- DROP DATABASE IF EXISTS new_database;
--CREATE DATABASE new_database;
-- ddl-end --


-- object: public."Bebe" | type: TABLE --
-- DROP TABLE IF EXISTS public."Bebe" CASCADE;
CREATE TABLE public."bebe" (
	"id" serial NOT NULL,
	"genero" text NOT NULL,
	"peso" real NOT NULL,
	"talla" smallint NOT NULL,
	"fecha_nacimiento" date NOT NULL,
	"apgar_1" smallint,
	"apgar_2" smallint,
	"tiempo_gestacion" smallint NOT NULL,
	"tipo_parto" text,
	"id_madre" integer NOT NULL,
	"id_padre" integer,
	CONSTRAINT "Bebe_pk" PRIMARY KEY ("id")

);
-- ddl-end --
ALTER TABLE public."bebe" OWNER TO postgres;
-- ddl-end --

-- object: public."Madre" | type: TABLE --
-- DROP TABLE IF EXISTS public."Madre" CASCADE;
CREATE TABLE public."madre" (
	"id" serial NOT NULL,
	"edad" smallint NOT NULL,
	"multiplicidad" text,
	"embarazos" smallint,
	"hijos_vivos" smallint,
	CONSTRAINT "Madre_pk" PRIMARY KEY ("id")

);
-- ddl-end --
ALTER TABLE public."madre" OWNER TO postgres;
-- ddl-end --

-- object: public."padre" | type: TABLE --
-- DROP TABLE IF EXISTS public."Padre" CASCADE;
CREATE TABLE public."padre" (
	"id" serial NOT NULL,
	"edad" smallint NOT NULL,
	CONSTRAINT "Padre_pk" PRIMARY KEY ("id")

);
-- ddl-end --
ALTER TABLE public."padre" OWNER TO postgres;
-- ddl-end --

-- object: "Madre_fk" | type: CONSTRAINT --
-- ALTER TABLE public."Bebe" DROP CONSTRAINT IF EXISTS "Madre_fk" CASCADE;
ALTER TABLE public."bebe" ADD CONSTRAINT "Madre_fk" FOREIGN KEY ("id_madre")
REFERENCES public."madre" ("id") MATCH FULL
ON DELETE RESTRICT ON UPDATE CASCADE;
-- ddl-end --

-- object: "Padre_fk" | type: CONSTRAINT --
-- ALTER TABLE public."bebe" DROP CONSTRAINT IF EXISTS "Padre_fk" CASCADE;
ALTER TABLE public."bebe" ADD CONSTRAINT "Padre_fk" FOREIGN KEY ("id_padre")
REFERENCES public."padre" ("id") MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

