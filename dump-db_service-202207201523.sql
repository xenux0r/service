--
-- PostgreSQL database dump
--

-- Dumped from database version 13.7 (Debian 13.7-1.pgdg110+1)
-- Dumped by pg_dump version 14.3

-- Started on 2022-07-20 15:23:39 MSK

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 202 (class 1259 OID 16392)
-- Name: requests; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.requests (
    id integer NOT NULL,
    value_name character varying(80),
    groups json,
    created_at timestamp with time zone DEFAULT now()
);


--
-- TOC entry 201 (class 1259 OID 16390)
-- Name: requests_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.requests_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 2997 (class 0 OID 0)
-- Dependencies: 201
-- Name: requests_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.requests_id_seq OWNED BY public.requests.id;


--
-- TOC entry 2856 (class 2604 OID 16395)
-- Name: requests id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.requests ALTER COLUMN id SET DEFAULT nextval('public.requests_id_seq'::regclass);


--
-- TOC entry 2991 (class 0 OID 16392)
-- Dependencies: 202
-- Data for Name: requests; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.requests (id, value_name, groups, created_at) FROM stdin;
1	im	[]	2022-07-20 10:05:20.678891+00
2	im	[{"id": 5, "name": "imba"}]	2022-07-20 10:06:12.929407+00
3	gr	[{"id": 1, "name": "group1"}, {"id": 3, "name": "group3"}]	2022-07-20 10:07:30.967029+00
\.


--
-- TOC entry 2998 (class 0 OID 0)
-- Dependencies: 201
-- Name: requests_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.requests_id_seq', 3, true);


--
-- TOC entry 2859 (class 2606 OID 16401)
-- Name: requests requests_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.requests
    ADD CONSTRAINT requests_pkey PRIMARY KEY (id);


-- Completed on 2022-07-20 15:23:39 MSK

--
-- PostgreSQL database dump complete
--

