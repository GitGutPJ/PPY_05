def prime(*numbers):
    for i in numbers:
        if i < 2:
            print(i, " is not prime")
        if i == 2:
            print(i, " is prime number")
        for j in range(2,i):
            if (i % j) == 0:
                print(i, " is not prime")
                break
            else:
                print(i, " is prime number")
                break

prime(0, 1, 2, 3,4,5)