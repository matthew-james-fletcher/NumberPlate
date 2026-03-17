import random
import datetime
from AbstractNumberPlateGenerator import AbstractNumberPlateGenerator

USABLE_LETTERS = "ABCDEFGHJKLMNOPRSTUVWXY"
POSSIBLE_SEQUENCE_LENGTH = USABLE_LETTERS.__len__() ** 3


class NumberPlateGeneratorV2 (AbstractNumberPlateGenerator):
    created_plates = {}
    def generate_number_plate(self, dvla: str, created_date: str) -> str:
        if dvla.__len__() != 2:
            raise ValueError("DVLA code must be 2 characters long")
        if dvla[0] not in USABLE_LETTERS or dvla[1] not in USABLE_LETTERS:
            raise ValueError("DVLA code must only contain letters from the usable letters set: " + USABLE_LETTERS)
        number_plate_prefix = dvla
        created_date_obj = datetime.datetime.strptime(created_date, "%d/%m/%Y")
        if created_date_obj > datetime.datetime.now():
            raise ValueError("Created date cannot be in the future")
        month = created_date_obj.month
        year = created_date_obj.year
        if month <= 2 or month >= 9:
            year += 50
        number_plate_prefix += str(year)[-2:]
        return f"{number_plate_prefix} {self.create_random_letters(number_plate_prefix)}"
    
    def create_random_letters(self, number_plate_prefix: str) -> str:
        if number_plate_prefix in self.created_plates and self.created_plates[number_plate_prefix].__len__() >= POSSIBLE_SEQUENCE_LENGTH - 1:
            raise ValueError("All possible number plates for this prefix have been generated")
        if number_plate_prefix not in self.created_plates:
            self.created_plates[number_plate_prefix] = set()
        if len(self.created_plates[number_plate_prefix]) >= POSSIBLE_SEQUENCE_LENGTH:
            raise ValueError("All possible number plates for this prefix have been generated")
        while True:
            random_number = random.randint(0, POSSIBLE_SEQUENCE_LENGTH - 1)
            if random_number in self.created_plates[number_plate_prefix]:
                continue
            self.created_plates[number_plate_prefix].add(random_number)
            return self.convert_random_number_to_letters(random_number)
    

    
    @staticmethod
    def convert_random_number_to_letters(n : int) -> str:
        letters = ""
        for i in range(3):
            letters = USABLE_LETTERS[n % USABLE_LETTERS.__len__()] + letters
            n //= USABLE_LETTERS.__len__()
        return letters
