--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.14
-- Dumped by pg_dump version 9.5.14

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: farid
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO farid;

--
-- Name: exchange_rate; Type: TABLE; Schema: public; Owner: farid
--

CREATE TABLE public.exchange_rate (
    id integer NOT NULL,
    "cur_From" character varying NOT NULL,
    "cur_To" character varying NOT NULL,
    "cur_Rate" double precision NOT NULL,
    "cur_avg_Rate" double precision NOT NULL,
    "cur_Date" timestamp without time zone NOT NULL
);


ALTER TABLE public.exchange_rate OWNER TO farid;

--
-- Name: exchange_rate_id_seq; Type: SEQUENCE; Schema: public; Owner: farid
--

CREATE SEQUENCE public.exchange_rate_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.exchange_rate_id_seq OWNER TO farid;

--
-- Name: exchange_rate_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: farid
--

ALTER SEQUENCE public.exchange_rate_id_seq OWNED BY public.exchange_rate.id;


--
-- Name: masukan_rate; Type: TABLE; Schema: public; Owner: farid
--

CREATE TABLE public.masukan_rate (
    id integer NOT NULL,
    "cur_From" character varying NOT NULL,
    "cur_To" character varying NOT NULL,
    "cur_Rate" double precision NOT NULL,
    "cur_Date" timestamp without time zone NOT NULL
);


ALTER TABLE public.masukan_rate OWNER TO farid;

--
-- Name: masukan_rate_id_seq; Type: SEQUENCE; Schema: public; Owner: farid
--

CREATE SEQUENCE public.masukan_rate_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.masukan_rate_id_seq OWNER TO farid;

--
-- Name: masukan_rate_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: farid
--

ALTER SEQUENCE public.masukan_rate_id_seq OWNED BY public.masukan_rate.id;


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: farid
--

ALTER TABLE ONLY public.exchange_rate ALTER COLUMN id SET DEFAULT nextval('public.exchange_rate_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: farid
--

ALTER TABLE ONLY public.masukan_rate ALTER COLUMN id SET DEFAULT nextval('public.masukan_rate_id_seq'::regclass);


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: farid
--

COPY public.alembic_version (version_num) FROM stdin;
e0ee829a7e89
\.


--
-- Data for Name: exchange_rate; Type: TABLE DATA; Schema: public; Owner: farid
--

COPY public.exchange_rate (id, "cur_From", "cur_To", "cur_Rate", "cur_avg_Rate", "cur_Date") FROM stdin;
1	GBP	USD	1.10499999999999998	0	2018-07-03 00:00:00
5	USD	GBP	0.0940000000000000002	0	2018-07-03 00:00:00
\.


--
-- Name: exchange_rate_id_seq; Type: SEQUENCE SET; Schema: public; Owner: farid
--

SELECT pg_catalog.setval('public.exchange_rate_id_seq', 6, true);


--
-- Data for Name: masukan_rate; Type: TABLE DATA; Schema: public; Owner: farid
--

COPY public.masukan_rate (id, "cur_From", "cur_To", "cur_Rate", "cur_Date") FROM stdin;
3	GBP	USD	1.10499999999999998	2018-07-03 00:00:00
4	USD	GBP	0.0940000000000000002	2018-07-03 00:00:00
5	USD	GBP	0.757900000000000018	2018-07-01 00:00:00
\.


--
-- Name: masukan_rate_id_seq; Type: SEQUENCE SET; Schema: public; Owner: farid
--

SELECT pg_catalog.setval('public.masukan_rate_id_seq', 5, true);


--
-- Name: alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: farid
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: exchange_rate_pkey; Type: CONSTRAINT; Schema: public; Owner: farid
--

ALTER TABLE ONLY public.exchange_rate
    ADD CONSTRAINT exchange_rate_pkey PRIMARY KEY (id);


--
-- Name: masukan_rate_pkey; Type: CONSTRAINT; Schema: public; Owner: farid
--

ALTER TABLE ONLY public.masukan_rate
    ADD CONSTRAINT masukan_rate_pkey PRIMARY KEY (id);


--
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

