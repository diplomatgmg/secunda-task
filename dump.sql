--
-- PostgreSQL database dump
--

-- Dumped from database version 17.0
-- Dumped by pg_dump version 17.0

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: activities; Type: TABLE DATA; Schema: public; Owner: dbuser
--

COPY public.activities (id, name, parent_id) FROM stdin;
1	Еда	\N
2	Мясная продукция	1
3	Молочная продукция	1
4	Сыр	3
5	Творог	3
6	Автомобили	\N
7	Грузовые	6
8	Легковые	6
9	Запчасти	8
10	Аксессуары	8
\.


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: dbuser
--

COPY public.alembic_version (version_num) FROM stdin;
34007dcae9dd
\.


--
-- Data for Name: buildings; Type: TABLE DATA; Schema: public; Owner: dbuser
--

COPY public.buildings (id, address, coordinates) FROM stdin;
1	г. Москва, ул. Тверская, д. 1	0101000020E6100000E63FA4DFBECE424037894160E5E04B40
3	г. Санкт-Петербург, Невский проспект, д. 28	0101000020E610000033C4B12E6E533E4039B4C876BEF74D40
4	г. Казань, ул. Баумана, д. 51	0101000020E6100000643BDF4F8D8F4840CB10C7BAB8E54B40
5	г. Екатеринбург, пр. Ленина, д. 51	0101000020E6100000F697DD93874D4E40A54E4013616B4C40
6	г. Новосибирск, Красный проспект, д. 29	0101000020E610000042CF66D5E7BA54406B2BF697DD834B40
\.


--
-- Data for Name: organizations; Type: TABLE DATA; Schema: public; Owner: dbuser
--

COPY public.organizations (id, name, building_id) FROM stdin;
1	Молочная Лавка	1
2	Авто-Экспресс	3
3	Сибирские деликатесы	6
4	Грузоперевозки 'УралТранс'	5
5	Гастроном №1	1
\.


--
-- Data for Name: organization_activity_table; Type: TABLE DATA; Schema: public; Owner: dbuser
--

COPY public.organization_activity_table (organization_id, activity_id) FROM stdin;
1	3
1	4
2	9
2	10
3	2
4	7
5	1
\.


--
-- Data for Name: phone_numbers; Type: TABLE DATA; Schema: public; Owner: dbuser
--

COPY public.phone_numbers (id, number, organization_id) FROM stdin;
1	1-333-455	1
2	7-843-200-30-40	2
3	7-917-200-30-40	2
4	8-383-222-11-22	3
5	7-343-987-65-43	4
6	1-495-777	5
7	2-333-616	5
8	6-156-161	5
\.


--
-- Data for Name: spatial_ref_sys; Type: TABLE DATA; Schema: public; Owner: dbuser
--

COPY public.spatial_ref_sys (srid, auth_name, auth_srid, srtext, proj4text) FROM stdin;
\.


--
-- Data for Name: geocode_settings; Type: TABLE DATA; Schema: tiger; Owner: dbuser
--

COPY tiger.geocode_settings (name, setting, unit, category, short_desc) FROM stdin;
\.


--
-- Data for Name: pagc_gaz; Type: TABLE DATA; Schema: tiger; Owner: dbuser
--

COPY tiger.pagc_gaz (id, seq, word, stdword, token, is_custom) FROM stdin;
\.


--
-- Data for Name: pagc_lex; Type: TABLE DATA; Schema: tiger; Owner: dbuser
--

COPY tiger.pagc_lex (id, seq, word, stdword, token, is_custom) FROM stdin;
\.


--
-- Data for Name: pagc_rules; Type: TABLE DATA; Schema: tiger; Owner: dbuser
--

COPY tiger.pagc_rules (id, rule, is_custom) FROM stdin;
\.


--
-- Data for Name: topology; Type: TABLE DATA; Schema: topology; Owner: dbuser
--

COPY topology.topology (id, name, srid, "precision", hasz) FROM stdin;
\.


--
-- Data for Name: layer; Type: TABLE DATA; Schema: topology; Owner: dbuser
--

COPY topology.layer (topology_id, layer_id, schema_name, table_name, feature_column, feature_type, level, child_id) FROM stdin;
\.


--
-- Name: activities_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dbuser
--

SELECT pg_catalog.setval('public.activities_id_seq', 10, true);


--
-- Name: buildings_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dbuser
--

SELECT pg_catalog.setval('public.buildings_id_seq', 6, true);


--
-- Name: organizations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dbuser
--

SELECT pg_catalog.setval('public.organizations_id_seq', 5, true);


--
-- Name: phone_numbers_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dbuser
--

SELECT pg_catalog.setval('public.phone_numbers_id_seq', 8, true);


--
-- Name: topology_id_seq; Type: SEQUENCE SET; Schema: topology; Owner: dbuser
--

SELECT pg_catalog.setval('topology.topology_id_seq', 1, false);


--
-- PostgreSQL database dump complete
--

