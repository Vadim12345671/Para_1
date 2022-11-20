def checker(function):
    def checker(*args, **kwargs):
        try:
            result = function(*args, **kwargs)
        except Exception as exc:
            print(f"We have problem {exc}")
        else:
            print(f"Result - {result}")
    return checker


try:
    a = int(input("Введіть перше число:"))
    b = int(input("Введіть друге число: "))
except ValueError:
    print("A and B must be int")

c = input("Укажіть операцію: ")


@checker
def calculate(expression):
    return eval(expression)


if c == "+":
    calculate("a+b")
elif c == "-":
    calculate("a-b")
elif c == "*":
    calculate("a*b")
elif c == "/":
    calculate("a/b")
elif c == "**":
    calculate("a**b")
elif c == "//":
    calculate("a//b")
elif c == "%":
    calculate("a%b")
else:
    print("You can only use '+' '-' '*' '/' '**' '//' '%'")