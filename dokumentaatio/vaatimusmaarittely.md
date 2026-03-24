# Vaatimusmäärittely

## Sovelluksen tarkoitus
Sovelluksen avulla käyttäjä voi pitää kirjaa kuntosaliharjoittelustaan. Käyttäjä voi kirjata treenisessioita, lisätä liikkeitä, sarjoja ja painoja, ja seurata kehitystään ajan myötä.

## Käyttöliittymäluonnos
Sovellus koostuu kahdesta näkymästä.

Sovellus aukeaa päänäkymään, jossa näkyy treenihistoria päivämäärittäin ryhmiteltynä. Päänäkymästä pääsee kirjausnäkymään, jossa voi lisätä uusia treenejä.

## Perusversion tarjoama toiminnallisuus

### Päänäkymä
- Käyttäjä näkee aiemmat treenisessiot listattuna järjestyksessä päivämäärän mukaan
- Käyttäjä voi aloittaa uuden treenisession, jolloin sovellus siirtyy kirjausnäkymään
- Käyttäjä voi poistaa kirjatun sarjan

### Kirjausnäkymä
- Käyttäjä voi valita liikkeen ennalta määritellystä listasta
- Käyttäjä voi kirjata sarjan syöttämällä painon ja toistomäärän
- Kirjatut sarjat näkyvät näkymässä lisäyksen jälkeen
- Käyttäjä voi palata päänäkymään

## Tietokantarakenne
Sovellus käyttää kolmea tietokantataulua:
- **Exercise** – liikkeet (nimi, lihasryhmä)
- **Workout** – treenisessiot (päivämäärä)
- **WorkoutSet** – sarjat (viittaus sessioon ja liikkeeseen, paino, toistot)

WorkoutSet yhdistää Workout- ja Exercise-taulut.

## Jatkokehitysideoita
Perusversion jälkeen järjestelmää täydennetään ajan salliessa esim. seuraavilla toiminnallisuuksilla:
- Edellisen treenin sarjat näytetään vertailua varten kirjausnäkymässä
- Kehityskaaviot: paino tai toistot kaaviona näyttämään kehityskäyrä
- Mahdollisuus lisätä omia liikkeitä ennalta määritellyn listan lisäksi
- Treeniohjelmien luominen ja tallentaminen pohjiksi