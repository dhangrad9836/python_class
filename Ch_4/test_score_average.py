# This program averages test scores. It asks the user for the
# number of students and the number of test scores per student.

# Get the number of students.
num_sudents = int(input('How many students do you have? '))

# Get the number of test scores per student.
num_test_scores = int(input('How many test scores per student? '))

# Determine each student's average test score.
for student in range(num_sudents):
    # Initialize an accumulator for test score.
    total = 0.0
    # Get a student's test scores.
    # reminder that we add 1 to student b/c the iteration starts at 0
    # and we want it to start at 1
    print('Student number', student + 1)
    print('----------------')
    for test_num in range(num_test_scores):
        print('Test number', test_num + 1, end='')
        score = float(input(': '))
        # Add the score to the accumulator.
        total += score

    # Calculate the average test score for this student
    average = total / num_test_scores

    # Display the average.
    print('The average for student number', student + 1,
          'is:', average)

    print()