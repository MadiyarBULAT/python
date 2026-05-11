from analytics import FileManager, DataLoader, ResultSaver, Report
from analytics.analyser import GpaAnalyser

def main():
    file = "students.csv"

    fm = FileManager(file)
    if not fm.file_exists():
        print("File not found!")
        return

    loader = DataLoader(file)
    data = loader.load_data()

    analyser = GpaAnalyser(data)
    analyser.analyse()

    report = Report(analyser.result)
    report.print_report()

    saver = ResultSaver("result.json")
    saver.save(analyser.result)


if __name__ == "__main__":
    main()
