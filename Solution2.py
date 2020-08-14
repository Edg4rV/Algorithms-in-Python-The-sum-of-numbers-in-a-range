def range_sum(numbers, start, end):
    new_list = [x for x in numbers if start <= x <= end]
    return sum(new_list)

input_numbers =  input().split()
input_numbers = [int(x) for x in input_numbers]
r =  input().split()
a = int(r[0])
b = int(r[1])
print(range_sum(input_numbers, a, b))
