

num = int (input("enter the number: "))
def prime_check(num):
	for i in range(2 , int(num**0.5)+1):
		if (num % i == 0):
			return False
	return True


if prime_check(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")