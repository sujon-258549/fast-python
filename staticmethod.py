

class School:
    school_name = "Sujon School"

    @staticmethod
    def greetCalculate(marks):
        if marks >= 90:
            return "Excellent"
        elif marks >= 80:
            return "Very Good"
        elif marks >= 75:
            return "Good"
        elif marks >= 60:
            return "Average"
        else:
            return "Needs Improvement"
        
print(School.greetCalculate(85))  # Output: Good
        