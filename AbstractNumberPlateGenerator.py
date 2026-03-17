class AbstractNumberPlateGenerator:
    def generate_number_plate(self, dvla: str, created_date: str) -> str:
        raise NotImplementedError("Subclasses must implement this method")
