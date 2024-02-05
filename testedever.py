for n in range(100, 1000):
    next_Number = n // 10
    sum = 0
    original_Number = n
    while next_Number > 0:
        last_Digit = n % 10
        sum += (last_Digit**3)
        next_Number = n // 10
        n = next_Number
    if original_Number == sum:
        print(original_Number, 'is an Armstrong number')



