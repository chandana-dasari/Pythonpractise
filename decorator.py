def upper_(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper

@upper_
def greet():
    return "hello world"
