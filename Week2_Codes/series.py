def print_numbers(n):
    # Fibonacci series of size n
    fib = []
    a, b = 0, 1
    for _ in range(n):
        fib.append(a)
        a, b = b, a + b
    
    print("Fibonacci series:", fib)

    # Count even numbers in Fibonacci series
    even_count = len([x for x in fib if x % 2 == 0])
    print("Even numbers in series:", even_count)

    # Multiplication table of n (1 to 10)
    table = [n * i for i in range(1, 11)]
    print("Multiplication table:", table)

    # Largest multiple 
    largest_multiple = max(table)
    print("Largest multiple in table:", largest_multiple)

    #  Sum of table values
    total_sum = sum(table)
    print("Sum of table values:", total_sum)
    if total_sum > 200:
        print("Sum is greater than 200")
    else:
        print("Sum is less than or equal to 200")
print_numbers(5)