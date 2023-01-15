
CREATE TABLE "kierowca"(
    "id_kierowca" serial,
    "nazwisko" VARCHAR(255) NOT NULL,
    "imie" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "kierowca" ADD PRIMARY KEY("id_kierowca");
CREATE TABLE "autobus"(
    "id_autobus" serial,
    "typ_autobusu" VARCHAR(255) NULL,
    "liczba_miejsc" BIGINT NULL,
    "id_kierowca" BIGINT NULL,
    "id_linia" BIGINT NULL
);
ALTER TABLE
    "autobus" ADD PRIMARY KEY("id_autobus");
CREATE TABLE "linia"(
    "id_linia" serial,
    "nr_linii" BIGINT NOT NULL
);
ALTER TABLE
    "linia" ADD PRIMARY KEY("id_linia");
CREATE TABLE "linia_polaczenie"(
    "id_linia" BIGINT NOT NULL,
    "id_polaczenie" BIGINT NOT NULL
);
ALTER TABLE
    "linia_polaczenie" ADD PRIMARY KEY("id_polaczenie");
CREATE TABLE "polaczenie"(
    "id_polaczenie" serial,
    "id_przystanek" BIGINT NOT NULL,
    "na_zadanie" BOOLEAN NOT NULL
);
ALTER TABLE
    "polaczenie" ADD PRIMARY KEY("id_polaczenie");
CREATE TABLE "przyjazd"(
    "id_przyjazd" serial,
    "godzina_przyjazd" TIME(0) WITHOUT TIME ZONE NOT NULL,
    "godzina_odjazd" TIME(0) WITHOUT TIME ZONE NOT NULL
);
ALTER TABLE
    "przyjazd" ADD PRIMARY KEY("id_przyjazd");
CREATE TABLE "przystanek"(
    "id_przystanek" serial,
    "nazwa" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "przystanek" ADD PRIMARY KEY("id_przystanek");
CREATE TABLE "przyjazd_polaczenie"(
    "id_polaczenie" BIGINT NOT NULL,
    "id_przyjazd" BIGINT NOT NULL,
    "numer_przejazdu" BIGINT NOT NULL
);
ALTER TABLE
    "przyjazd_polaczenie" ADD PRIMARY KEY("id_przyjazd");
ALTER TABLE
    "autobus" ADD CONSTRAINT "autobus_id_kierowca_foreign" FOREIGN KEY("id_kierowca") REFERENCES "kierowca"("id_kierowca");
ALTER TABLE
    "polaczenie" ADD CONSTRAINT "polaczenie_id_przystanek_foreign" FOREIGN KEY("id_przystanek") REFERENCES "przystanek"("id_przystanek");
ALTER TABLE
    "przyjazd_polaczenie" ADD CONSTRAINT "przyjazd_polaczenie_id_polaczenie_foreign" FOREIGN KEY("id_polaczenie") REFERENCES "polaczenie"("id_polaczenie");
ALTER TABLE
    "linia_polaczenie" ADD CONSTRAINT "linia_polaczenie_id_linia_foreign" FOREIGN KEY("id_linia") REFERENCES "linia"("id_linia");










create view przystanki_info
as
select * from
linia join linia_polaczenie using (id_linia)
join polaczenie using (id_polaczenie)
join przystanek using (id_przystanek)
join przyjazd_polaczenie using (id_polaczenie)
join przyjazd using (id_przyjazd);



CREATE OR REPLACE FUNCTION przystanki_dla_linii( lin int)
returns table (linia bigint, numer bigint,  nazwa_przystanku varchar, zadanie boolean, godzina_przyjazdu time, godzina_odjazdu time) as
$$
BEGIN
  RETURN QUERY
    select nr_linii, numer_przejazdu, nazwa, na_zadanie, godzina_przyjazd, godzina_odjazd from przystanki_info
    where nr_linii = lin
    group by (nr_linii, nazwa, na_zadanie, godzina_przyjazd, godzina_odjazd);
END;
$$
LANGUAGE 'plpgsql';



CREATE OR REPLACE FUNCTION polacz_dane(id_kier int, id_auto int, nr_lin int)
returns void as
$$
BEGIN
    UPDATE autobus
    SET id_kierowca = id_kier,
    id_linia = (select id_linia from linia_polaczenie
    join linia using (id_linia)
    where nr_linii = nr_lin
    group by id_linia)
    WHERE id_autobus = id_auto;
END;
$$
LANGUAGE 'plpgsql';



CREATE OR REPLACE FUNCTION ostatni_numer_przejazdu(nr_lin int)
returns bigint as
$$
BEGIN
    return (SELECT numer_przejazdu from przystanki_info
    where nr_linii = nr_lin
    ORDER BY numer_przejazdu
    ASC LIMIT 1);
END;
$$
LANGUAGE 'plpgsql';


CREATE OR REPLACE FUNCTION get_pierwszy_id_przyjazd(nr_lin int)
returns bigint as
$$
BEGIN
    return (SELECT id_polaczenie from przystanki_info
    where nr_linii = nr_lin
    ORDER BY id_polaczenie
    ASC LIMIT 1);
END;
$$
LANGUAGE 'plpgsql';





INSERT INTO przystanek(nazwa) VALUES
 ('Wawel'),
 ('Wisła'),
 ('Stadion'),
 ('Kawiory'),
 ('Czarnowiejska'),
 ('AGH'),
 ('UJ'),
 ('Dworzec');



