import random
import datetime
from AbstractNumberPlateGenerator import AbstractNumberPlateGenerator

USABLE_LETTERS = "ABCDEFGHJKLMNOPRSTUVWXY"
POSSIBLE_SEQUENCE_LENGTH = USABLE_LETTERS.__len__() ** 3


class NumberPlateGenerator(AbstractNumberPlateGenerator):
    created_plates = {}
    def generate_number_plate(self, dvla: str, created_date: str) -> str:
        if dvla.__len__() != 2:
            raise ValueError("DVLA code must be 2 characters long")
        if dvla[0] not in USABLE_LETTERS or dvla[1] not in USABLE_LETTERS:
            raise ValueError("DVLA code must only contain letters from the usable letters set: " + USABLE_LETTERS)
        number_plate_prefix = dvla
        try: 
            created_date_obj = datetime.datetime.strptime(created_date, "%d/%m/%Y")
        except ValueError:
            raise ValueError("Invalid date format. Please use dd/mm/yyyy.")
        if created_date_obj > datetime.datetime.now():
            raise ValueError("Created date cannot be in the future")
        month = created_date_obj.month
        year = created_date_obj.year
        if month <= 2 or month >= 9:
            year += 50
        number_plate_prefix += str(year)[-2:]
        
        return f"{number_plate_prefix} {self.create_random_letters(number_plate_prefix)}"
    
    def create_random_letters(self, number_plate_prefix: str) -> str:
        seed = self._generate_seed(number_plate_prefix)
        random_sequence = self.generate_random_sequence(seed, POSSIBLE_SEQUENCE_LENGTH)
        
        number_plate_random_number = 0
        if number_plate_prefix in self.created_plates:
            if self.created_plates[number_plate_prefix] >= POSSIBLE_SEQUENCE_LENGTH - 1:
                raise ValueError("All possible number plates for this prefix have been generated")
            number_plate_random_number = random_sequence[self.created_plates[number_plate_prefix]]
            self.created_plates[number_plate_prefix] += 1
        else:
            number_plate_random_number = random_sequence[0]
            self.created_plates[number_plate_prefix] = 1
        return self.convert_random_number_to_letters(number_plate_random_number)
    
    @staticmethod
    def generate_random_sequence(seed : int, n : int) -> list:
        random.seed(seed)
        return random.sample(range(n), n)
    
    @staticmethod
    def convert_random_number_to_letters(n : int) -> str:
        letters = ""
        for i in range(3):
            letters = USABLE_LETTERS[n % USABLE_LETTERS.__len__()] + letters
            n //= USABLE_LETTERS.__len__()
        return letters
    
    @staticmethod
    def _generate_seed(number_plate_prefix: str) -> int:
        letter1 = USABLE_LETTERS.index(number_plate_prefix[0])
        letter2 = USABLE_LETTERS.index(number_plate_prefix[1])
        number = int(number_plate_prefix[2:])
        return (letter1 * len(USABLE_LETTERS) + letter2) * 100 + number
    