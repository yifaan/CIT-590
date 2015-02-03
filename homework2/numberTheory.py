import math


def isInt(x):
    return x == int(x)


def solveQuadraic(a, b, c):
    x = (-b + math.sqrt(b * b - 4 * a * c)) / 2 / a
    return x


def isPrime(x):
    if x == 1:
        return False

    for a in range(2, x):
        if x % a == 0:
            return False
    return True


def isComposite(x):
    if x == 1:
        return False
    if isPrime(x):
        return False
    else:
        return True


def isPerfect(x):
    count = 0
    for a in range(1, x):
        if x % a == 0:
            count += a
    if count == x:
        return True
    else:
        return False


def isAbundant(x):
    count = 0
    for a in range(1, x):
        if x % a == 0:
            count += a
    if count > x:
        return True
    else:
        return False


def isTriangular(x):
    a = solveQuadraic(1, 1, -2 * x)
    if isInt(a):
        return True
    else:
        return False


def isPentagonal(x):
    if isTriangular(x * 3):
        return True
    else:
        return False


def isHexagonal(x):
    a = solveQuadraic(2, -1, -x)
    if isInt(a):
        return True
    else:
        return False


def main():
    while True:
        x = input("Input a number between 1 and 10000!\ninput -1 to quit!\n")

        while x < 1 or x > 10000:
            if x == -1:
                return

            print("Sorry! Number should between 1 to 10000!")
            x = input(
                "Input a number between 1 and 10000!\ninput -1 to quit!\n")

        if isPrime(x):
            prime = "is prime,"
        else:
            prime = "is not prime,"

        if isComposite(x):
            composite = "is composite,"
        else:
            composite = "is not composite,"

        if isPerfect(x):
            perfect = "is perfect,"
        else:
            perfect = "is not perfect,"

        if isAbundant(x):
            abundant = "is abundant,"
        else:
            abundant = "is not abundant,"

        if isTriangular(x):
            triangular = "is triangular,"
        else:
            triangular = "is not triangular,"

        if isPentagonal(x):
            pentagonal = "is pentagonal,"
        else:
            pentagonal = "is not pentagonal,"

        if isHexagonal(x):
            hexagonal = "is hexagonal."
        else:
            hexagonal = "is not hexagonal."

        print "\n", x, prime, composite, perfect, "\n", \
            abundant, triangular, pentagonal, hexagonal


if __name__ == "__main__":
    main()
