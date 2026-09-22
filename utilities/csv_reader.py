import csv


class CSVReader:

    @staticmethod
    def read_column(file_path, column_name):
        """Read all values from a specific CSV column."""

        data = []

        with open(file_path, mode="r", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                data.append(row[column_name])

        return data