# Ohjelmistotekniikka, harjoitustyö

Tässä harjoitustyössä kehitetään **yksinkertainen kuntosalitreenien seurantasovellus**, jonka toiminnallisuuksia on esimerkiksi *omien liikkeiden lisääminen, omien treenien kirjaaminen, graafien piirtäminen omasta kehityksestä ja omien ennätysten seuraaminen*.

## Linkki vaatimusmäärittelyyn
- [Vaatimusmäärittely](/dokumentaatio/vaatimusmaarittely.md)


## Linkki työaikakirjanpitoon
- [Työaikakirjanpito](/dokumentaatio/tuntikirjanpito.md)

## Linkki changelogiin
- [Changelog](/dokumentaatio/changelog.md)


## Asennus

1. Asenna ensin riippuvuudet:

```bash
poetry install
```

2. Suorita alustustoimenpiteet:

```bash
poetry run invoke build
```

3. Käynnistä sovellus:

```bash
poetry run invoke start
```


## Komennot komentorivillä

- Suorittaminen:

```bash
poetry run invoke start
```

- Testien ajaminen

```bash
poetry run invoke test
```

- Testikattavuusraportin luominen

```bash
poetry run invoke coverage-report
```