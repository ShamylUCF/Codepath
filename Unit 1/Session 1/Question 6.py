# question 6

def squared(numbers):
    for i in range(len(numbers)):
        numbers[i] = pow(numbers[i],2)
    return numbers

numbers = [1, 2, 3]
print(squared(numbers))