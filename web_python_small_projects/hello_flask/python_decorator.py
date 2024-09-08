import time


def decorator_function(function):
    def wrapper():
        time.sleep(3)
        function()
        function()
        print("you didn't notice it twice did you!")

    return wrapper

@decorator_function
def say_hello():
    print("Hello there!")

@decorator_function #one way
def say_bye():
    print("bye bye!")

def say_greetings():
    print("hi , what's going on?")


say_hello()
#2nd way
decorated_function = decorator_function(say_greetings)
decorated_function()



# or this way
print('\n')
current_time = time.time()
print(current_time)

def speed_calc_decorator(function):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = function(*args, **kwargs)
        end_time = time.time()
        print(f"{function.__name__} run speed:{end_time - start_time}s")

        return result

    return wrapper


@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        i * i


fast_function()
slow_function()




