
# # UNLIMITED POSITIONAL ARGUMENT
# def add(*args):  #args in tuple
#     total = 0
#     for n in args:
#         total += n
#     print(total)
#     return total
#
# add(1,2,3,4,5)


# Unlimited KEYWORD ARGUMENT

# def calculate(n,**kwargs):  #kwargs in dictionary
#     print(kwargs)
#     # for key,value in kwargs.items():
#     #     # print(key)
#     #     # print(value)
#     #     # print(kwargs["add"])
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)
#
# calculate(2, add = 3, multiply = 5)


class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.colour = kwargs.get("colour")
        self.seat =  kwargs.get("seat")

my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)
