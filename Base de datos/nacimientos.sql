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
CREATE DATABASE new_database;
-- ddl-end --


-- object: public.bebe | type: TABLE --
-- DROP TABLE IF EXISTS public.bebe CASCADE;
CREATE TABLE public.bebe (
	id_bebe text NOT NULL,
	genero text,
	peso integer,
	talla integer,
	fecha_nacimiento date,
	tiempo_gestacion integer,
	tipo_parto text,
	multiplicidad text,
	apgar1 integer,
	apgar2 integer,
	id_madre_madre text,
	id_padre_padre text,
	CONSTRAINT bebe_pk PRIMARY KEY (id_bebe)

);
-- ddl-end --
ALTER TABLE public.bebe OWNER TO postgres;
-- ddl-end --

-- object: public.madre | type: TABLE --
-- DROP TABLE IF EXISTS public.madre CASCADE;
CREATE TABLE public.madre (
	id_madre text NOT NULL,
	edad_madre integer,
	embarazos integer,
	hijos_vivos integer,
	CONSTRAINT madre_pk PRIMARY KEY (id_madre)

);
-- ddl-end --
ALTER TABLE public.madre OWNER TO postgres;
-- ddl-end --

-- object: public.padre | type: TABLE --
-- DROP TABLE IF EXISTS public.padre CASCADE;
CREATE TABLE public.padre (
	id_padre text NOT NULL,
	edad_padre integer,
	CONSTRAINT padre_pk PRIMARY KEY (id_padre)

);
-- ddl-end --
ALTER TABLE public.padre OWNER TO postgres;
-- ddl-end --

-- object: madre_fk | type: CONSTRAINT --
-- ALTER TABLE public.bebe DROP CONSTRAINT IF EXISTS madre_fk CASCADE;
ALTER TABLE public.bebe ADD CONSTRAINT madre_fk FOREIGN KEY (id_madre_madre)
REFERENCES public.madre (id_madre) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: padre_fk | type: CONSTRAINT --
-- ALTER TABLE public.bebe DROP CONSTRAINT IF EXISTS padre_fk CASCADE;
ALTER TABLE public.bebe ADD CONSTRAINT padre_fk FOREIGN KEY (id_padre_padre)
REFERENCES public.padre (id_padre) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --


