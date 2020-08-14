def range_sum(numbers, start, end):
    x = 0
    for i in numbers:
        if i >= start and i <= end:
            x += i
    return x

input_numbers = [int(i) for i in input().split(' ')]

a, b = [int(i) for i in input().split(' ')]
print(range_sum(input_numbers, a, b))
