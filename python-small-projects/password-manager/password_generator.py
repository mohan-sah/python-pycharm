# Password Generator Project
import random


class PasswordGenerator(object):
    def __init__(self):
        self.letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                        't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                        'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

        # print("Welcome to the PyPassword Generator!")
        self.nr_letters = random.randint(8, 10)
        self.nr_symbols = random.randint(2, 4)
        self.nr_numbers = random.randint(2, 4)
        self.password_list = None

    # Eazy Level - Order not randomised:
    # e.g. 4 letter, 2 symbol, 2 number = JduE&!91
    # password = ""
    # for letter in range(0,nr_letters):
    #   password += random.choice(letters)
    # for symbol in range(0,nr_symbols):
    #   password += random.choice(symbols)
    # for number in range(0,nr_numbers):
    #   password += random.choice(numbers)
    # password = ''.join(random.sample(password,len(password)))

    # print(f"Your password is {password}")
    # random_list = [random_letters,random_numbers,random_symbols]
    # length_random_list = len(random_list) -1

    # Hard Level - Order of characters randomised:
    # e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

    def generate(self):
        password_list = []
        password_list  = [random.choice(self.letters) for letter in range(0,self.nr_letters)]
        # for letter in range(0, self.nr_letters):
        #     password_list += random.choice(self.letters)
        password_list += [random.choice(self.symbols) for symbol in range(0,self.nr_symbols)]
        # for symbol in range(0, self.nr_symbols):
        #     password_list += random.choice(self.symbols)
        password_list += [random.choice(self.numbers) for number in range(0, self.nr_numbers)]
        print(f"Your password is {password_list}")
        random.shuffle(password_list)
        self.password_list = ''.join(password_list)
        return self.password_list
