import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti


class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_luotu_kassa_on_olemassa(self):
        self.assertNotEqual(self.kassapaate, None)

    def test_rahamaara_alussa_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_myyty_maara_maukkaita_oikein_alussa(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_myyty_maara_edullisia_oikein_alussa(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_kateisosto_toimii_edullisilla_lounailla_maara_kasvaa(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_kateisosto_toimii_edullisilla_lounailla_vaihtoraha_oikein(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(250), 10)

    def test_kateisosto_toimii_edullisilla_lounailla_kassa_muuttuu_oikein(self):
        self.kassapaate.syo_edullisesti_kateisella(240)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000+240)

    def test_kateisosto_toimii_edullisilla_lounailla_ei_riittava_raha_rahat_palautetaan(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(200), 200)

    def test_kateisosto_toimii_edullisilla_lounailla_ei_riittava_raha_kassa_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kateisella(200)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kateisosto_toimii_edullisilla_lounailla_ei_riittava_raha_myyty_maara_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kateisella(200)

        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_kateisosto_toimii_maukkailla_lounailla_maara_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_kateisosto_toimii_maukkailla_lounailla_vaihtoraha_oikein(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500), 100)

    def test_kateisosto_toimii_maukkailla_lounailla_kassa_muuttuu_oikein(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000+400)

    def test_kateisosto_toimii_maukkailla_lounailla_ei_riittava_raha_rahat_palautetaan(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(300), 300)

    def test_kateisosto_toimii_maukkailla_lounailla_ei_riittava_raha_kassa_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kateisella(300)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kateisosto_toimii_maukkailla_lounailla_ei_riittava_raha_myyty_maara_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    # korttimaksut

    def test_korttiosto_toimii_edullisilla_lounailla_maara_kasvaa(self):
        maksukortti = Maksukortti(1000)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_korttiosto_toimii_edullisilla_lounailla_veloitus_palauttaa_true(self):
        maksukortti = Maksukortti(1000)
        self.assertEqual(
            self.kassapaate.syo_edullisesti_kortilla(maksukortti), True)

    def test_korttiosto_toimii_edullisilla_lounailla_ei_riittava_saldo_maara_ei_muutu(self):
        maksukortti = Maksukortti(100)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_korttiosto_toimii_edullisilla_lounailla_ei_riittava_saldo_palautusarvo_oikein(self):
        maksukortti = Maksukortti(100)
        self.assertEqual(
            self.kassapaate.syo_edullisesti_kortilla(maksukortti), False)

    def test_korttiosto_toimii_edullisilla_lounailla_ei_riittava_saldo_kortin_saldo_ei_muutu(self):
        maksukortti = Maksukortti(100)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(maksukortti.saldo, 100)

    def test_korttiosto_toimii_edullisilla_kassa_ei_muutu(self):
        maksukortti = Maksukortti(1000)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_korttiosto_toimii_maukkailla_lounailla_maara_kasvaa(self):
        maksukortti = Maksukortti(1000)
        self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_korttiosto_toimii_maukkailla_lounailla_veloitus_palauttaa_true(self):
        maksukortti = Maksukortti(1000)
        self.assertEqual(
            self.kassapaate.syo_maukkaasti_kortilla(maksukortti), True)

    def test_korttiosto_toimii_maukkailla_lounailla_ei_riittava_saldo_maara_ei_muutu(self):
        maksukortti = Maksukortti(100)
        self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_korttiosto_toimii_maukkailla_lounailla_ei_riittava_saldo_palautusarvo_oikein(self):
        maksukortti = Maksukortti(100)
        self.assertEqual(
            self.kassapaate.syo_maukkaasti_kortilla(maksukortti), False)

    def test_korttiosto_toimii_maukkailla_lounailla_ei_riittava_saldo_kortin_saldo_ei_muutu(self):
        maksukortti = Maksukortti(100)
        self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(maksukortti.saldo, 100)

    def test_korttiosto_toimii_maukkailla_kassa_ei_muutu(self):
        maksukortti = Maksukortti(1000)
        self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    # raportin jälkeen nämä puuttui

    def test_kassassa_rahaa_euroina_toimii(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)

    def test_lataus_toimii_positiivisella_luvulla_kortin_saldo_kasvaa(self):
        maksukortti = Maksukortti(1000)
        self.kassapaate.lataa_rahaa_kortille(maksukortti, 100)
        self.assertEqual(maksukortti.saldo, 1100)

    def test_lataus_toimii_positiivisella_luvulla_kassa_kasvaa(self):
        maksukortti = Maksukortti(1000)
        self.kassapaate.lataa_rahaa_kortille(maksukortti, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100100)

    def test_lataus_ei_toimi_negatiivisella_luvulla_kassa_ei_kasva(self):
        maksukortti = Maksukortti(1000)
        self.kassapaate.lataa_rahaa_kortille(maksukortti, -1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_lataus_ei_toimi_negatiivisella_kortin_saldo_ei_kasva(self):
        maksukortti = Maksukortti(1000)
        self.kassapaate.lataa_rahaa_kortille(maksukortti, -1000)
        self.assertEqual(maksukortti.saldo, 1000)
