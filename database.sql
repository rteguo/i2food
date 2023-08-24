--
-- PostgreSQL database dump
--

-- Dumped from database version 13.10 (Ubuntu 13.10-1.pgdg22.04+1)
-- Dumped by pg_dump version 13.10 (Ubuntu 13.10-1.pgdg22.04+1)

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
-- Name: categories; Type: TABLE; Schema: public; Owner: rteguo
--

CREATE TABLE public.categories (
    category_id integer NOT NULL,
    name character varying NOT NULL,
    description character varying,
    weight integer,
    status integer,
    create_time timestamp without time zone,
    update_time timestamp without time zone
);


ALTER TABLE public.categories OWNER TO rteguo;

--
-- Name: categories_category_id_seq; Type: SEQUENCE; Schema: public; Owner: rteguo
--

CREATE SEQUENCE public.categories_category_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.categories_category_id_seq OWNER TO rteguo;

--
-- Name: categories_category_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: rteguo
--

ALTER SEQUENCE public.categories_category_id_seq OWNED BY public.categories.category_id;


--
-- Name: order_items; Type: TABLE; Schema: public; Owner: rteguo
--

CREATE TABLE public.order_items (
    order_item_id integer NOT NULL,
    order_id integer NOT NULL,
    product_id integer,
    quantity timestamp without time zone,
    sub_total double precision,
    status integer,
    create_time timestamp without time zone,
    update_time timestamp without time zone
);


ALTER TABLE public.order_items OWNER TO rteguo;

--
-- Name: order_items_order_item_id_seq; Type: SEQUENCE; Schema: public; Owner: rteguo
--

CREATE SEQUENCE public.order_items_order_item_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.order_items_order_item_id_seq OWNER TO rteguo;

--
-- Name: order_items_order_item_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: rteguo
--

ALTER SEQUENCE public.order_items_order_item_id_seq OWNED BY public.order_items.order_item_id;


--
-- Name: orders; Type: TABLE; Schema: public; Owner: rteguo
--

CREATE TABLE public.orders (
    order_id integer NOT NULL,
    user_id integer NOT NULL,
    order_date timestamp without time zone,
    total_amount double precision,
    status integer,
    create_time timestamp without time zone,
    update_time timestamp without time zone
);


ALTER TABLE public.orders OWNER TO rteguo;

--
-- Name: orders_order_id_seq; Type: SEQUENCE; Schema: public; Owner: rteguo
--

CREATE SEQUENCE public.orders_order_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.orders_order_id_seq OWNER TO rteguo;

--
-- Name: orders_order_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: rteguo
--

ALTER SEQUENCE public.orders_order_id_seq OWNED BY public.orders.order_id;


--
-- Name: products; Type: TABLE; Schema: public; Owner: rteguo
--

CREATE TABLE public.products (
    product_id integer NOT NULL,
    category_id integer,
    name character varying NOT NULL,
    description text,
    price double precision,
    image_url character varying,
    stock_qty integer,
    unit_measure character varying,
    rating integer,
    status integer,
    create_time timestamp without time zone,
    update_time timestamp without time zone
);


ALTER TABLE public.products OWNER TO rteguo;

--
-- Name: products_product_id_seq; Type: SEQUENCE; Schema: public; Owner: rteguo
--

CREATE SEQUENCE public.products_product_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.products_product_id_seq OWNER TO rteguo;

--
-- Name: products_product_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: rteguo
--

ALTER SEQUENCE public.products_product_id_seq OWNED BY public.products.product_id;


--
-- Name: profiles; Type: TABLE; Schema: public; Owner: rteguo
--

CREATE TABLE public.profiles (
    profile_id integer NOT NULL,
    name character varying,
    description character varying,
    status integer,
    create_time timestamp without time zone,
    update_time timestamp without time zone
);


ALTER TABLE public.profiles OWNER TO rteguo;

--
-- Name: profiles_profile_id_seq; Type: SEQUENCE; Schema: public; Owner: rteguo
--

CREATE SEQUENCE public.profiles_profile_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.profiles_profile_id_seq OWNER TO rteguo;

--
-- Name: profiles_profile_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: rteguo
--

ALTER SEQUENCE public.profiles_profile_id_seq OWNED BY public.profiles.profile_id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: rteguo
--

CREATE TABLE public.users (
    user_id integer NOT NULL,
    profile_id integer,
    email character varying NOT NULL,
    password character varying,
    last_name character varying,
    first_name character varying,
    address character varying,
    phone character varying,
    activity character varying,
    title character varying,
    sex character varying,
    status integer,
    create_time timestamp without time zone,
    update_time timestamp without time zone
);


ALTER TABLE public.users OWNER TO rteguo;

--
-- Name: users_user_id_seq; Type: SEQUENCE; Schema: public; Owner: rteguo
--

CREATE SEQUENCE public.users_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_user_id_seq OWNER TO rteguo;

--
-- Name: users_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: rteguo
--

ALTER SEQUENCE public.users_user_id_seq OWNED BY public.users.user_id;


--
-- Name: categories category_id; Type: DEFAULT; Schema: public; Owner: rteguo
--

ALTER TABLE ONLY public.categories ALTER COLUMN category_id SET DEFAULT nextval('public.categories_category_id_seq'::regclass);


--
-- Name: order_items order_item_id; Type: DEFAULT; Schema: public; Owner: rteguo
--

ALTER TABLE ONLY public.order_items ALTER COLUMN order_item_id SET DEFAULT nextval('public.order_items_order_item_id_seq'::regclass);


--
-- Name: orders order_id; Type: DEFAULT; Schema: public; Owner: rteguo
--

ALTER TABLE ONLY public.orders ALTER COLUMN order_id SET DEFAULT nextval('public.orders_order_id_seq'::regclass);


--
-- Name: products product_id; Type: DEFAULT; Schema: public; Owner: rteguo
--

ALTER TABLE ONLY public.products ALTER COLUMN product_id SET DEFAULT nextval('public.products_product_id_seq'::regclass);


--
-- Name: profiles profile_id; Type: DEFAULT; Schema: public; Owner: rteguo
--

ALTER TABLE ONLY public.profiles ALTER COLUMN profile_id SET DEFAULT nextval('public.profiles_profile_id_seq'::regclass);


--
-- Name: users user_id; Type: DEFAULT; Schema: public; Owner: rteguo
--

ALTER TABLE ONLY public.users ALTER COLUMN user_id SET DEFAULT nextval('public.users_user_id_seq'::regclass);


--
-- Data for Name: categories; Type: TABLE DATA; Schema: public; Owner: rteguo
--

COPY public.categories (category_id, name, description, weight, status, create_time, update_time) FROM stdin;
1	Fruits	Variety of fruits for all seasons	2	1	2023-08-18 22:38:33.211595	2023-08-18 22:38:33.211648
2	Vegetables	Variety of vegetables for all seasons	1	1	2023-08-18 22:38:33.211654	2023-08-18 22:38:33.211656
\.


--
-- Data for Name: order_items; Type: TABLE DATA; Schema: public; Owner: rteguo
--

COPY public.order_items (order_item_id, order_id, product_id, quantity, sub_total, status, create_time, update_time) FROM stdin;
\.


--
-- Data for Name: orders; Type: TABLE DATA; Schema: public; Owner: rteguo
--

COPY public.orders (order_id, user_id, order_date, total_amount, status, create_time, update_time) FROM stdin;
\.


--
-- Data for Name: products; Type: TABLE DATA; Schema: public; Owner: rteguo
--

COPY public.products (product_id, category_id, name, description, price, image_url, stock_qty, unit_measure, rating, status, create_time, update_time) FROM stdin;
1	1	Fresh Avocado	Nice Fruit	2	/static/img/product/3.jpg	100	Unit	3	1	2023-08-18 22:43:41.353369	2023-08-18 22:43:41.35338
2	2	Fresh Spinach	Fresh Vegetable	1	/static/img/product/11.jpg	150	lb	1	1	2023-08-18 22:43:41.353384	2023-08-18 22:43:41.353385
3	1	Fresh Mango	Nice Fruit	6	/static/img/product/4.jpg	100	Unit	2	1	2023-08-18 22:43:41.353387	2023-08-18 22:43:41.353389
4	2	Fresh Okra	Fresh Vegetable	7.2	/static/img/product/9.jpg	150	lb	1	1	2023-08-18 22:43:41.35339	2023-08-18 22:43:41.353392
\.


--
-- Data for Name: profiles; Type: TABLE DATA; Schema: public; Owner: rteguo
--

COPY public.profiles (profile_id, name, description, status, create_time, update_time) FROM stdin;
1	Administrator	Allow to work in backend	1	2023-08-18 22:21:15.373446	2023-08-18 22:21:15.37345
2	Customer	Allow to check and order products in front end	1	2023-08-18 22:21:15.373453	2023-08-18 22:21:15.373454
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: rteguo
--

COPY public.users (user_id, profile_id, email, password, last_name, first_name, address, phone, activity, title, sex, status, create_time, update_time) FROM stdin;
1	1	admin@test.com	test	admin test	test	Brindle ST	9406292800	IT	Engineer	M	1	2023-08-18 22:32:25.596765	2023-08-18 22:32:25.596771
2	2	customer@test.com	test	customer test	test	Brindle ST	9406292800	IT	Engineer	M	1	2023-08-18 22:32:25.596774	2023-08-18 22:32:25.596776
3	2	tegsromaric@gmail.com	deco	TEGUO	ROMARIC CYRILLE	1516 Brindle St	9406292800	Information Technology		M	1	2023-08-20 21:03:11.114683	2023-08-20 21:03:11.114699
\.


--
-- Name: categories_category_id_seq; Type: SEQUENCE SET; Schema: public; Owner: rteguo
--

SELECT pg_catalog.setval('public.categories_category_id_seq', 2, true);


--
-- Name: order_items_order_item_id_seq; Type: SEQUENCE SET; Schema: public; Owner: rteguo
--

SELECT pg_catalog.setval('public.order_items_order_item_id_seq', 1, false);


--
-- Name: orders_order_id_seq; Type: SEQUENCE SET; Schema: public; Owner: rteguo
--

SELECT pg_catalog.setval('public.orders_order_id_seq', 1, false);


--
-- Name: products_product_id_seq; Type: SEQUENCE SET; Schema: public; Owner: rteguo
--

SELECT pg_catalog.setval('public.products_product_id_seq', 4, true);


--
-- Name: profiles_profile_id_seq; Type: SEQUENCE SET; Schema: public; Owner: rteguo
--

SELECT pg_catalog.setval('public.profiles_profile_id_seq', 2, true);


--
-- Name: users_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: rteguo
--

SELECT pg_catalog.setval('public.users_user_id_seq', 3, true);


--
-- Name: categories categories_pkey; Type: CONSTRAINT; Schema: public; Owner: rteguo
--

ALTER TABLE ONLY public.categories
    ADD CONSTRAINT categories_pkey PRIMARY KEY (category_id);


--
-- Name: order_items order_items_pkey; Type: CONSTRAINT; Schema: public; Owner: rteguo
--

ALTER TABLE ONLY public.order_items
    ADD CONSTRAINT order_items_pkey PRIMARY KEY (order_item_id);


--
-- Name: orders orders_pkey; Type: CONSTRAINT; Schema: public; Owner: rteguo
--

ALTER TABLE ONLY public.orders
    ADD CONSTRAINT orders_pkey PRIMARY KEY (order_id);


--
-- Name: products products_pkey; Type: CONSTRAINT; Schema: public; Owner: rteguo
--

ALTER TABLE ONLY public.products
    ADD CONSTRAINT products_pkey PRIMARY KEY (product_id);


--
-- Name: profiles profiles_pkey; Type: CONSTRAINT; Schema: public; Owner: rteguo
--

ALTER TABLE ONLY public.profiles
    ADD CONSTRAINT profiles_pkey PRIMARY KEY (profile_id);


--
-- Name: users users_email_key; Type: CONSTRAINT; Schema: public; Owner: rteguo
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_email_key UNIQUE (email);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: rteguo
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (user_id);


--
-- Name: order_items order_items_order_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: rteguo
--

ALTER TABLE ONLY public.order_items
    ADD CONSTRAINT order_items_order_id_fkey FOREIGN KEY (order_id) REFERENCES public.orders(order_id);


--
-- Name: order_items order_items_product_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: rteguo
--

ALTER TABLE ONLY public.order_items
    ADD CONSTRAINT order_items_product_id_fkey FOREIGN KEY (product_id) REFERENCES public.products(product_id);


--
-- Name: orders orders_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: rteguo
--

ALTER TABLE ONLY public.orders
    ADD CONSTRAINT orders_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(user_id);


--
-- Name: products products_category_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: rteguo
--

ALTER TABLE ONLY public.products
    ADD CONSTRAINT products_category_id_fkey FOREIGN KEY (category_id) REFERENCES public.categories(category_id);


--
-- Name: users users_profile_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: rteguo
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_profile_id_fkey FOREIGN KEY (profile_id) REFERENCES public.profiles(profile_id);


--
-- PostgreSQL database dump complete
--

