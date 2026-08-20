#wap using a function to check prime no.
def prime(a):
    if a < 2:
        return False
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            return False
    return True
n = int(input("enter a number: "))
print(prime(n))
