def add_student():
    name = input("Enter student name: ")
    score1 = int(input("Enter score 1: "))
    score2 = int(input("Enter score 2: "))
    score3 = int(input("Enter score 3: "))
    return {
        "name": name,
        "scores": [score1, score2, score3]
    }

def calculate_result(scores):
    total = sum(scores)
    average = total / len(scores)
    return total, average

def display_result(student, total, average):
    print("\n--- Student Result ---")
    print("Name:", student["name"])
    print("Scores:", student["scores"])
    print("Total:", total)
    print("Average:", average)

student = add_student()
total, average = calculate_result(student["scores"])
display_result(student, total, average)