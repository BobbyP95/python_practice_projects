# suggest a band name using city and pet names
def suggest_band():
    user_name = input("Hi Dear, May I know your name\n")
    user_city = input(user_name + ", what City are you from?\n")
    user_pet = input(user_name + ", please tell me the name of your pet\n")
    user_brand = "The_"+user_city +"_"+ user_pet+"s"
    print("Hahaaaa!!!\n Your brand is " + user_brand)

# finding the last character of a string
def find_last_char():
    word = input("Enter the word\n: ")
    length = len(word)
    last_char_index = length - 1
    print("The last char of "+word +" is " + word[last_char_index])



# Break 2 digit number and add it
def break_2_digit():
    two_digit = input("Enter the two digit number\n: ")
    if len(two_digit) > 2:
        print("please enter only 2 digits")
        return
    if len(two_digit) < 2:
        print("please enter up to 2 digits")
        return  
    number1 = int(two_digit[0])
    number2 = int(two_digit[1])
    print(number1 + number2)
    return
# Body Mass Index 
def bmi_Calculator():
    height = input("Please enter the height in meters\n: ")
    weight = input("Please enter the weight in kg\n: ")
    result = float(weight) / (float(height)**2)
    print("Your BMI is : "+ str(result))

bmi_Calculator()