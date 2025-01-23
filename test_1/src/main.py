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


find_last_char()


