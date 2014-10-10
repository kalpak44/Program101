"""
importing
from filename import func1,funcc2....
"""

#N-th Fibonacci

def nth_fibonacci(n):
    if n == 0 or n  == 1:
        return 1
    else:
        return (nth_fibonacci(n-1) + nth_fibonacci(n-2))


#print (nth_fibonacci(4))

#Sum all digits of a number

def sum_of_digits(n):
    if n > 0:
        sum = 0
        while n > 0:
            sum = n % 10 + sum
            n = n / 10;
        return sum
    else:
        n = abs(n)
        sum = 0
        while n > 0:
            sum = n % 10 + sum
            n = n / 10;
        return sum


#print (sum_of_digits(-15))

#Sum all divisors of an integer
def sum_of_divisors(n):
    n = abs(n)
    if n > 1:
        sum = n + 1;
        for i in range(2,n):
            if n % i == 0:
                sum = sum + i
        return sum
    else:
        return 1

#print (sum_of_divisors(4))

#Check if integer is prime
def is_prime(n):
    n = abs(n)
    if n < 2:
        return False
    i = 2
    while i*i <= n:
        i = i + 1
        return False
    return True


#print (is_prime(1))

#Check if a number has a prime number of divisors
def prime_number_of_divisors(n):
    n = abs(n)
    if n > 1:
        num = 2;
        for i in range(2,n):
            if n % i == 0:
                num = num + 1
        return is_prime(num)
    else:
        return False
#print (prime_number_of_divisors(9))



#Are there n sevens in a row?
def sevens_in_a_row(arr, n):
    j = 0
    for i in range(0,len(arr)):
        print arr[i]
        if arr[i] == 7:
            j = j + 1;
            if j == 3: print ""
        else:
            j = 0




arr = [10, 8, 7, 6, 7, 7, 7, 20, -7]
n = 3
sevens_in_a_row(arr, n)