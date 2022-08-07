def intake(func, *args, **kwargs):
    def newfunc():
        return func(*args, **kwargs)

    return newfunc

if __name__ == "__main__":
    def my_annoying_func(message):
        print(message)

    x = intake(my_annoying_func, message="hello world")
    print(x())