n = input("Set number for calculate N!: ")
try:
    val = int(n)
    if val < 0:
        print('Value must be greater or equal 0')
    else:
        factorial = 1
        while val > 1:
            factorial *= val
            val -= 1
        print(factorial)
except ValueError:
    try:
        val = float(n)
        print("Input is not a int. It's a float")
    except ValueError:
        print("Input is not a int. It's a string")
