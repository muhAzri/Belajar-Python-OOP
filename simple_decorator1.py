def info(func):
    def wrapper():
        print("*" * 10)
        func()
        print("#" * 10)

    return wrapper

def say_hello():
    print("Hello World")

say_hello()
say_hello = info(say_hello)
say_hello()