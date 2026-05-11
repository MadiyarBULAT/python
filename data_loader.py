import csv

class DataLoader:
    def __init__(self, filename):
        self.filename = filename

    def load_data(self):
        data = []
        try:
            with open(self.filename, newline='', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    # убираем лишние пробелы
                    clean_row = {key.strip(): value.strip() for key, value in row.items()}
                    data.append(clean_row)

            print(f"Loaded {len(data)} rows successfully")

        except FileNotFoundError:
            print("Error: File not found!")
        except Exception as e:
            print("Error while reading file:", e)

        return data
