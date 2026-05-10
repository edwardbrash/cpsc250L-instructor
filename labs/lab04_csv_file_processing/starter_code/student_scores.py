# Lab 4: File I/O and CSV Data Processing
#
# Complete this program so that it reads quiz score data from a CSV file,
# cleans the data, computes student averages, and prints a report.


def clean_score(score_text):
    """
    Convert a score string into an integer.

    If the score is missing or invalid, return None.
    """
    try:
        score = int(score_text)
        if 0 <= score <= 100:
            return score
        else:
            return None
    except ValueError:
        return None



def calculate_average(scores):
    """
    Calculate the average of a list of numeric scores.

    If the list is empty, return None.
    """
    total = 0
    count = 0
    for score in scores:
        if score is not None:
            total += score
            count += 1
    if count > 0:
        return total / count
    else:
        return None


def read_scores(filename):
    """
    Read student quiz scores from a CSV file.

    Return a list of dictionaries.

    Each dictionary should contain:
        "name": student name
        "scores": list of valid numeric quiz scores
        "average": student average
    """
    # You can use the csv module to read the file, but you will need to clean
    # the scores and calculate the average for each student.
    import csv
    f = open(filename,"r")
    reader = csv.reader(f)
    header = next(reader)  # Skip the header row
    records = []
    for row in reader:
        name = row[0]
        score_texts = row[1:]
        scores = [clean_score(score) for score in score_texts]
        average = calculate_average(scores)
        record = {
            "name": name,
            "scores": scores,
            "average": average,
            "grade": letter_grade(average)
        }
        records.append(record)
    f.close()

    return records


def letter_grade(average):
    """
    Return a simple letter grade based on the average.

    Suggested scale:
        A: average >= 87
        B: average >= 77
        C: average >= 67
        D: average >= 57
        F: otherwise

    If the average is None, return "N/A".
    """
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


def print_student_report(records):
    """
    Print one line of output for each student.
    """
    print("Student Quiz Report")
    print("-------------------")
    for record in records:
        name = record["name"]
        average = record["average"]
        grade = record["grade"]
        print(f"{name}: average = {average:.1f}, grade = {grade}")

def print_class_summary(records):
    """
    Print a summary for the whole class.

    Include:
        number of students
        class average
        highest average
        lowest average
    """
    num_students = len(records)
    averages = [record["average"] for record in records if record["average"] is not None]
    if averages:
        class_average = sum(averages) / len(averages)
        highest_average = max(averages)
        lowest_average = min(averages)
    else:
        class_average = None
        highest_average = None
        lowest_average = None

    print("Class Summary")
    print("-------------")
    print(f"Number of students: {num_students}")
    if class_average is not None:
        print(f"Class average: {class_average:.1f}")
        print(f"Highest average: {highest_average:.1f}")
        print(f"Lowest average: {lowest_average:.1f}")
    else:
        print("No valid scores to calculate class summary.")


def main():
    filename = "../data/quiz_scores.csv"

    records = read_scores(filename)
    #print(records)

    print_student_report(records)
    print()
    print_class_summary(records)


if __name__ == "__main__":
    main()
