import unittest
from maksukortti import Maksukortti


class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)

    def test_rahan_lataaminen_toimii(self):
        self.maksukortti.lataa_rahaa(1000)

        self.assertEqual(self.maksukortti.saldo_euroina(), 20.0)

    def test_saldo_vahenee_oikein_rahaa_tarpeeksi(self):
        self.maksukortti.ota_rahaa(500)
        self.assertEqual(self.maksukortti.saldo_euroina(), 5.0)

    def test_saldo_ei_vahene_kun_rahaa_ei_tarpeeksi(self):
        self.maksukortti.ota_rahaa(1500)
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)

    def test_ota_rahaa_palauttaa_true_jos_rahat_riittaa(self):
        self.assertEqual(self.maksukortti.ota_rahaa(500), True)

    def test_ota_rahaa_palauttaa_false_jos_rahat_ei_riita(self):
        self.assertEqual(self.maksukortti.ota_rahaa(2500), False)

    def test_tulostus_toimii_oikein(self):
        self.assertEqual(str(self.maksukortti),
                         "Kortilla on rahaa 10.00 euroa")
