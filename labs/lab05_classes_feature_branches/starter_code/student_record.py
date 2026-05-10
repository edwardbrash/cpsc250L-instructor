# Lab 5: Classes, Objects, and Feature Branches
#
# Complete the StudentRecord class.


class StudentRecord:
    def __init__(self, name, student_id):
        """
        Create a new student record.

        Parameters:
            name: student name as a string
            student_id: student ID as a string
        """
        self.name = name
        self.student_id = student_id
        self.scores = []

    def add_score(self, score):
        """
        Add one quiz score to this student's list of scores.

        Only add scores between 0 and 100.
        """
        if 0 <= score <= 100:
            self.scores.append(score)


    def calculate_average(self):
        """
        Return the average quiz score.

        If the student has no scores, return None.
        """
        if len(self.scores) == 0:
            return None
        else:
            total = sum(self.scores)
            average = total / len(self.scores)
            return average

    def highest_score(self):
        """
        Return the highest quiz score.

        If the student has no scores, return None.
        """
        if len(self.scores) == 0:
            return None
        else:
            return max(self.scores)

    def lowest_score(self):
        """
        Return the lowest quiz score.

        If the student has no scores, return None.
        """
        if len(self.scores) == 0:
            return None
        else:
            return min(self.scores)

    def letter_grade(self):
        """
        Return a letter grade based on the student's average.

        Suggested scale:
            A: average >= 87
            B: average >= 77
            C: average >= 67
            D: average >= 57
            F: otherwise
        """
        average = self.calculate_average()
        if average is None:
            return "N/A"
        elif average >= 87:
            return "A"
        elif average >= 77:
            return "B"
        elif average >= 67:
            return "C"
        elif average >= 57:
            return "D"
        else:
            return "F"

    def __str__(self):
        """
        Return a readable string representation of the student record.
        """
        average = self.calculate_average()
        if average is not None:
            average_str = f"{average:.1f}"
        else:
            average_str = "N/A"
        grade = self.letter_grade()
        return f"Student: {self.name} (ID: {self.student_id})\n" \
               f"Scores: {self.scores}\n" \
               f"Average: {average_str}\n" \
               f"Grade: {grade}"
