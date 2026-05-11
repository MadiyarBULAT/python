class DataAnalyser:  #Наследование
    def __init__(self, data):
        self.data = data
        self.result = {}

    def analyse(self):
        raise NotImplementedError


class GpaAnalyser(DataAnalyser):
    def analyse(self):
        gpas = []

        for d in self.data:
            try:
                gpas.append(float(d["GPA"]))
            except:
                continue

        if not gpas:
            self.result = {}
            return

        self.result["total_students"] = len(gpas)
        self.result["average_gpa"] = round(sum(gpas) / len(gpas), 2)
        self.result["max_gpa"] = max(gpas)
        self.result["min_gpa"] = min(gpas)

        self.result["high_performers"] = [
            d for d in self.data
            if "GPA" in d and float(d["GPA"]) > 3.5
        ]
