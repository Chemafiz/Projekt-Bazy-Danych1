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
    "linia_polaczenie" ADD PRIMARY KEY("id_linia");
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
    "id_przyjazd" BIGINT NOT NULL
);
ALTER TABLE
    "przyjazd_polaczenie" ADD PRIMARY KEY("id_polaczenie");
ALTER TABLE
    "autobus" ADD CONSTRAINT "autobus_id_kierowca_foreign" FOREIGN KEY("id_kierowca") REFERENCES "kierowca"("id_kierowca");
ALTER TABLE
    "polaczenie" ADD CONSTRAINT "polaczenie_id_przystanek_foreign" FOREIGN KEY("id_przystanek") REFERENCES "przystanek"("id_przystanek");
ALTER TABLE
    "autobus" ADD CONSTRAINT "autobus_id_linia_foreign" FOREIGN KEY("id_linia") REFERENCES "linia_polaczenie"("id_linia");
ALTER TABLE
    "przyjazd_polaczenie" ADD CONSTRAINT "przyjazd_polaczenie_id_przyjazd_foreign" FOREIGN KEY("id_przyjazd") REFERENCES "przyjazd"("id_przyjazd");