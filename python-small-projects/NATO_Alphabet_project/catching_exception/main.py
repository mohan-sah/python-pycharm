#FileNotFoundError:
# with open("a_file.txt", 'r') as file:
#     file.read()


#keyError
# a_dictionary = {'key' : 'value'}
# value =  a_dictionary['non-exiting_key']

#IndexError
# fruit_list = ["apple" , "orange" , " Pear"]
# fruit = fruit_list[3]

#TypeError
# text = "abc"
# print(text + 4)

### to fail more gracefully
# try:
# except:
# else:
# finally:

#FileNotFoundError:
# try:
#     file = open("a_file.txt")
#     a_dictionary = {'key' : 'value'}
#     value =  a_dictionary['key']
# except FileNotFoundError:
#     print("there was an error, do something else instead")
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"{error_message} key does not exist")
#
# else:#if all try passed
#     content = file.read()
#     print(content)
#
# finally:# no matter what happened , this will get executed
#     file.close()
#     print("file was closed.")
#     # raise KeyError # purposefully raise madeup error
#     # raise TypeError("this is my made-up error")


### bmi calculation
height = float(input("height: "))
weight  = int(input("weight: "))

if height > 3:
    raise ValueError("Human height is usually does not go over 3m")
bmi = weight / height ** 2
print(bmi)



