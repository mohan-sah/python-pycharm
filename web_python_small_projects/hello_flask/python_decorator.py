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

#advance python decorator functions

class User:
    def __init__(self,name):
        self.name = name
        self.is_logged_in = False

def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            function(args[0])
    return wrapper

@is_authenticated_decorator
def create_a_blog_post(user):
    print(f"this is {user.name}'s blog post.")

user = User(name="mohan")
user.is_logged_in=True
create_a_blog_post(user)


# a logging decorator exercise :
def logging_decorator(func):
    def wrapper(*args):
        print(f"You called {func.__name__}{args}")
        result = func(*args)
        print(f"It returned: {result}")
        return result

    return wrapper


@logging_decorator
def a_function(*args):
    return sum(args)


a_function(1, 2, 3)







