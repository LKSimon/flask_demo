-- CREATE SCHEMA  IF NOT EXISTS public AUTHORIZATION your_user_name;
CREATE SEQUENCE IF NOT EXISTS public.students_id_seq START 1;
CREATE TABLE IF NOT EXISTS public.students (
    id integer NOT NULL DEFAULT nextval('public.students_id_seq'::regclass),
    name text,
    city text,
    addr text,
    pin  text
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;
