def check(func):
    def inside(a, b):
        if b == 0:
            print("Not possible")
            return
        func(a, b)

    return inside


@check
def div(a, b):
    return a / b


print(div(10, 0))
