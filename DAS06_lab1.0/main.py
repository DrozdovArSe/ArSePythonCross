def main():
    try:
        a = int(input("Введите А: "))
        b = int(input("Введите B: "))
        x = int(input("Введите X: "))
        try:
            if x>6:
                y = ((6 * x * x) - (a * b)) / (2 * x * x)
            else:
                y = 4 * (x + a * a + b * b)
            print("y = %.1f" % y)
        except ArithmeticError:
            print("Неправильно введённые данные")
    except ValueError:
        print("Неправильно введённые данные")

if __name__ == '__main__':
    main()
