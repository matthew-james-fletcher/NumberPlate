import logging
import unittest
from AbstractNumberPlateGenerator import AbstractNumberPlateGenerator
from NumberPlateGenerator import NumberPlateGenerator
from NumberPlateGeneratorV2 import NumberPlateGeneratorV2

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class AbstractNumberPlateGeneratorTests:

    def get_generator(self) -> AbstractNumberPlateGenerator:
        raise NotImplementedError

    def setUp(self):
        self.generator = self.get_generator()
        # Reset class-level state so tests are isolated
        type(self.generator).created_plates = {}

    # added this test so you can see the generated plates rather than just accepting the fact that they are unique.

    def test_plates_are_unique_for_same_input(self):
        plates = [self.generator.generate_number_plate("AB", "15/03/2020") for _ in range(50)]
        logger.info("Generated plates for class %s: %s", self.generator.__class__.__name__, plates)
        self.assertEqual(len(plates), len(set(plates)), "Duplicate plates were generated for the same input")

class NumberPlateGeneratorTests(AbstractNumberPlateGeneratorTests, unittest.TestCase):
    def get_generator(self) -> AbstractNumberPlateGenerator:
        return NumberPlateGenerator()


class NumberPlateGeneratorV2Tests(AbstractNumberPlateGeneratorTests, unittest.TestCase):
    def get_generator(self) -> AbstractNumberPlateGenerator:
        return NumberPlateGeneratorV2()


if __name__ == "__main__":
    unittest.main()
