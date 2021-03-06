def trace_call(func):
    def inner(*args, **kwargs):
        print(
            "Function executed: {} args: {}".format(func.__name__, args)
        )
        return func(*args, **kwargs)
    return inner

@trace_call
def add(x, y):
    return x + y
