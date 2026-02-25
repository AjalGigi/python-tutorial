# Q13. Student Class Implementation

class Student:
    def __init__(self, name, num_scores):
        self.name = name
        self.test_scores = [0] * num_scores

    def getName(self):
        return self.name

    def getScore(self, position):
        return self.test_scores[position - 1]

    def setScore(self, position, value):
        self.test_scores[position - 1] = value

    def getHighestScore(self):
        return max(self.test_scores)

    def getAverageScore(self):
        return sum(self.test_scores) / len(self.test_scores)

    def __str__(self):
        scores_str = ", ".join(str(s) for s in self.test_scores)
        return (f"Student Name  : {self.name}\n"
                f"Test Scores   : [{scores_str}]\n"
                f"Highest Score : {self.getHighestScore()}\n"
                f"Average Score : {self.getAverageScore():.2f}")


def main():
    name = input("Enter student name: ")
    num = int(input("Enter number of test scores: "))

    student = Student(name, num)

    for i in range(1, num + 1):
        score = float(input(f"Enter score {i}: "))
        student.setScore(i, score)

    print("\n--- Student Report ---")
    print(student)

if __name__ == "__main__":
    main()
