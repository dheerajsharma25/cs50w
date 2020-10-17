def annouce(f):
    def wrapper():
        print("about to run the function ....")
        f()
        print("done with the function.")
    return wrapper()

@annouce
def hello():
    print("hello, world!")

hello()

