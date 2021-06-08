'''
A prime number is an integer, or whole number, 
that has only two factors — 1 and itself. Put another way, 
a prime number can be divided evenly only by 1 and by itself. 
Prime numbers also must be greater than 1. For example, 3 is a 
prime number, because 3 cannot be divided evenly by any number 
except for 1 and 3. However, 6 is not a prime number, because it 
can be divided evenly by 2 or 3.
'''
def prime_checker(n):
    is_prime = True
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

prime_checker(523)







