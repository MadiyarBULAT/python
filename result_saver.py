import json

class ResultSaver:
    def __init__(self, filename):
        self.filename = filename

    def save(self, result):
        with open(self.filename, "w") as f:
            json.dump(result, f, indent=4)
