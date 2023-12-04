# Sample data of students (average exam scores and admission scores)
exam_scores = [4.5, 3.8, 4.0, 4.2, 3.5, 4.8, 4.1, 3.9, 4.7, 4.3, 4.6, 3.6, 4.9, 3.7, 4.4, 3.4, 3.2, 4.5, 4.0, 4.8]
admission_scores = [4.8, 4.0, 3.5, 4.0, 3.3, 4.5, 4.2, 4.0, 4.6, 4.4, 4.8, 3.7, 4.9, 3.6, 4.3, 3.2, 3.0, 4.6, 4.2, 4.7]

# Creating a list for the difference between average exam scores and admission scores
score_difference = [abs(exam - admission) for exam, admission in zip(exam_scores, admission_scores)]

# Function to filter students based on score difference
def filter_by_threshold(difference, threshold):
    return [index for index, value in enumerate(difference) if value > threshold]

# Outputting lists of students based on specified thresholds
threshold_1 = 0.5
threshold_2 = 1.0
threshold_3 = 2.0

students_threshold_1 = filter_by_threshold(score_difference, threshold_1)
students_threshold_2 = filter_by_threshold(score_difference, threshold_2)
students_threshold_3 = filter_by_threshold(score_difference, threshold_3)

print("Абитуриенты с разницей более 0.5 балла:", students_threshold_1)
print("Абитуриенты с разницей более 1.0 балла:", students_threshold_2)
print("Абитуриенты с разницей более 2.0 балла:", students_threshold_3)
