def is_prime(num):


    for i in range (2, num):
        if num % i == 0:
            print ("Not Prime")
            break
    else:
        print("Prime")

        return True

is_prime(1007)