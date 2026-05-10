# Lab 6: Collections of Objects

from student_record import StudentRecord


def clean_score(score_text):
    """
    Convert score text to an integer.

    Return None if the score is missing or invalid.
    """
    try:
        score = int(score_text)
        if 0 <= score <= 100:
            return score
        else:
            return None
    except ValueError:
        pass
    return None


def read_student_records(filename):
    """
    Read the CSV file and return a list of StudentRecord objects.
    """
    import csv
    f = open(filename)
    reader = csv.reader(f)
    next(reader)  # Skip header row
    students = []
    for row in reader:
        id = row[0]
        name = row[1]
        scores = [clean_score(score) for score in row[2:] if clean_score(score) is not None]
        student = StudentRecord(name, id, scores)
        students.append(student)
    f.close()
    return students


def class_average(students):
    """
    Return the average of all student averages.

    Ignore students with no valid scores.
    """
    total_average = 0
    count = 0
    for student in students:
        average = student.calculate_average()
        if average is not None:
            total_average += average
            count += 1
    return total_average / count if count > 0 else None


def find_highest_average_student(students):
    """
    Return the StudentRecord object with the highest average.
    """



def find_lowest_average_student(students):
    """
    Return the StudentRecord object with the lowest average.
    """
    pass


def print_class_report(students):
    """
    Print all student records and a class summary.
    """
    print("Student records:")
    for student in students:
        print(student)


def main():
    students = read_student_records("../data/student_scores.csv")
    print_class_report(students)


if __name__ == "__main__":
    main()
