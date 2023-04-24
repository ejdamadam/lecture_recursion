def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def main():
    i = int(input("Zadej který prvek Fibbonaciho posloupnosti chceš vypsat: "))
    print(f"{i}. prvek Fibbonaciho posloupnosti je {fib(i)}.")
    pass


if __name__ == "__main__":
    main()

