

def is_prime_number(number) -> bool:
    return True


if __name__ == '__main__':

    if not is_prime_number(43):
        print("error, 43 is a prime")

    if is_prime_number(33):
        print("error, 33 is not a prime")
