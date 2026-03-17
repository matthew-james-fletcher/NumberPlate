import unittest
from AbstractNumberPlateGenerator import AbstractNumberPlateGenerator
from NumberPlateGenerator import NumberPlateGenerator
from NumberPlateGeneratorV2 import NumberPlateGeneratorV2


class AbstractNumberPlateGeneratorTests:

    def get_generator(self) -> AbstractNumberPlateGenerator:
        raise NotImplementedError

    def setUp(self):
        self.generator = self.get_generator()
        # Reset class-level state so tests are isolated
        type(self.generator).created_plates = {}

    # --- Uniqueness ---

    def test_plates_are_unique_for_same_input(self):
        plates = [self.generator.generate_number_plate("AB", "15/03/2020") for _ in range(50)]
        self.assertEqual(len(plates), len(set(plates)), "Duplicate plates were generated for the same input")

    # --- Invalid letters ---

    def test_letter_I_in_dvla_raises_error(self):
        with self.assertRaises(ValueError):
            self.generator.generate_number_plate("IA", "15/03/2020")

    def test_letter_Q_in_dvla_raises_error(self):
        with self.assertRaises(ValueError):
            self.generator.generate_number_plate("QA", "15/03/2020")

    def test_letter_Z_in_dvla_raises_error(self):
        with self.assertRaises(ValueError):
            self.generator.generate_number_plate("ZA", "15/03/2020")

    def test_invalid_letter_in_second_dvla_position_raises_error(self):
        with self.assertRaises(ValueError):
            self.generator.generate_number_plate("AI", "15/03/2020")

    # --- DVLA length ---

    def test_dvla_longer_than_two_characters_raises_error(self):
        with self.assertRaises(ValueError):
            self.generator.generate_number_plate("ABC", "15/03/2020")

    def test_dvla_shorter_than_two_characters_raises_error(self):
        with self.assertRaises(ValueError):
            self.generator.generate_number_plate("A", "15/03/2020")

    # --- Date format ---

    def test_iso_date_format_raises_error(self):
        with self.assertRaises(ValueError):
            self.generator.generate_number_plate("AB", "2020-03-15")

    def test_invalid_date_string_raises_error(self):
        with self.assertRaises(ValueError):
            self.generator.generate_number_plate("AB", "not-a-date")

    # --- Plate structure ---

    def test_first_two_characters_match_dvla_tag(self):
        plate = self.generator.generate_number_plate("AB", "15/03/2020")
        self.assertEqual(plate[:2], "AB")

    def test_different_dvla_tag_appears_in_plate(self):
        plate = self.generator.generate_number_plate("CD", "15/03/2020")
        self.assertEqual(plate[:2], "CD")

    # --- Year digits: March–August → last two digits of year ---

    def test_march_gives_last_two_digits_of_year(self):
        plate = self.generator.generate_number_plate("AB", "15/03/2002")
        self.assertEqual(plate[2:4], "02")

    def test_august_gives_last_two_digits_of_year(self):
        plate = self.generator.generate_number_plate("AB", "15/08/2002")
        self.assertEqual(plate[2:4], "02")

    def test_march_to_august_millennium_year(self):
        plate = self.generator.generate_number_plate("AB", "15/05/2015")
        self.assertEqual(plate[2:4], "15")

    # --- Year digits: September–February → last two digits of year + 50 ---

    def test_september_gives_year_plus_50(self):
        plate = self.generator.generate_number_plate("AB", "15/09/2002")
        self.assertEqual(plate[2:4], "52")

    def test_december_gives_year_plus_50(self):
        plate = self.generator.generate_number_plate("AB", "15/12/2002")
        self.assertEqual(plate[2:4], "52")

    def test_september_to_february_millennium_year(self):
        plate = self.generator.generate_number_plate("AB", "15/11/2015")
        self.assertEqual(plate[2:4], "65")

    # January and February belong to the *previous* year's September group
    # e.g. Feb 2015 is in the "Sep 2014" half-year → 14 + 50 = 64

    def test_january_uses_previous_year_plus_50(self):
        plate = self.generator.generate_number_plate("AB", "15/01/2015")
        self.assertEqual(plate[2:4], "64")

    def test_february_uses_previous_year_plus_50(self):
        plate = self.generator.generate_number_plate("AB", "15/02/2015")
        self.assertEqual(plate[2:4], "64")


class NumberPlateGeneratorTests(AbstractNumberPlateGeneratorTests, unittest.TestCase):
    def get_generator(self) -> AbstractNumberPlateGenerator:
        return NumberPlateGenerator()


class NumberPlateGeneratorV2Tests(AbstractNumberPlateGeneratorTests, unittest.TestCase):
    def get_generator(self) -> AbstractNumberPlateGenerator:
        return NumberPlateGeneratorV2()


if __name__ == "__main__":
    unittest.main()
