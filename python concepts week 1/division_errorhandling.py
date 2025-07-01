def division():
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        div = a / b
    except ZeroDivisionError:
        print("Are you really dividing by 0")
    except ValueError:
        print("Not a valid integer")
    else:
        print("The answer is", div)
    finally:
        print("The work is done")
division()
