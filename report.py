class Report:
    def __init__(self, result):
        self.result = result

    def print_report(self):
        print("\n===== GPA ANALYSIS REPORT =====")

        print("Total students:", self.result["total_students"])
        print("Average GPA:", self.result["average_gpa"])
        print("Max GPA:", self.result["max_gpa"])
        print("Min GPA:", self.result["min_gpa"])

        print("\nHigh Performers (GPA > 3.5):")
        for student in self.result["high_performers"][:5]:  # только первые 5
            print(student)
