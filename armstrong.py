def is_armstrong(num):
    num_str = str(num)
    num_length = len(num_str)
    armstrong_sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        armstrong_sum += digit ** num_length
        temp //= 10
    return armstrong_sum == num
number = 153
if is_armstrong(number):
    print(number, "is an Armstrong number")
else:
    print(number, "is not an Armstrong number")
