# exercise-05 Fibonacci sequence for first 50 terms

# Write the code that:
# 1. Calculates and prints the first 50 terms of the fibonacci sequence.
# 2. Print each term and number as follows:
#      term: 0 / number: 0
#      term: 1 / number: 1
#      term: 2 / number: 1
#      term: 3 / number: 2
#      term: 4 / number: 3
#      term: 5 / number: 5
#      etc.

# Hint: The next number is found by adding the two numbers before it

current_term = 0
end_term = 50
n_1 = 0
n_2 = 0
number = 0

print(f'term: {current_term} / number: {number}')

while current_term < end_term:
    if current_term == 0:
        current_term += 1
        number = 1
        n_1 = 0
        n_2 = number 
        print(f'term: {current_term} / number: {number}')
    else: 
        current_term += 1
        number = n_1 + n_2
        n_1 = n_2
        n_2 = number 
        print(f'term: {current_term} / number: {number}')
