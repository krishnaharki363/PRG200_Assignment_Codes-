def analyze_numbers(n):
    #Sum of numbers from 1 to n 
    total_sum = sum (range(1, n+1))
    #Count of even numbers from 1 to n
    even_count = len([i for i in range(1, n+1) if i % 2 ==0])
    #Largest Number from 1 to n divisible by 3
    largest_div_3 = None
    for i in range(n, 0, -1):
        if i % 3 == 0:
            largest_div_3 = i 
            break
    return total_sum, even_count, largest_div_3    

result = analyze_numbers(10)

print("Sum", result[0])
print("Even count: ", result[1])
print("Largest divisble by 3: ", result[2])