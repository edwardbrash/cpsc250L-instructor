# Lab 6: Collections of Objects
#
# Complete this class. You may reuse ideas from Lab 5.


class StudentRecord:
    def __init__(self, name, student_id, scores=None):
        self.name = name
        self.student_id = student_id
        self.scores = scores if scores is not None else []

    def add_score(self, score):
        # Add a score to the student's record. Score should be an integer between 0 and 100.
        if isinstance(score, int) and 0 <= score <= 100:
            self.scores.append(score)

    def calculate_average(self):
        # Return the average score, or None if there are no scores.
        if self.scores:
            return sum(self.scores) / len(self.scores)
        return None

    def highest_score(self):
        # Return the highest score, or None if there are no scores.
        if self.scores:
            return max(self.scores)
        return None

    def lowest_score(self):
        # Return the lowest score, or None if there are no scores.
        if self.scores:
            return min(self.scores)
        return None

    def letter_grade(self):
        # Return the letter grade based on the average score.
        average = self.calculate_average()
        if average is None:
            return None
        elif average >= 90:
            return 'A'
        elif average >= 80:
            return 'B'
        elif average >= 70:
            return 'C'
        elif average >= 60:
            return 'D'
        else:
            return 'F'

    def __str__(self):
        # Return a string representation of the student record.
        average = self.calculate_average()
        average_str = f"{average:.2f}" if average is not None else "N/A"
        return f"Student: {self.name}, ID: {self.student_id}, Average Score: {average_str}"
