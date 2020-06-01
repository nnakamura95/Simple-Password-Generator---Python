import random
import string


let = string.ascii_letters
num = string.digits
pun = string.punctuation

def get_passcode_lenght():
    length = input("How long do you want your password? ")
    return int(length)

def passcode_generator(length,cbl):
    showpass = user_choice_combo(cbl)
    showpass = list(showpass)
    random.shuffle(showpass)

    random_passcode = random.choices(showpass, k=length)
    random_passcode = ''.join(random_passcode)
    return random_passcode

def passcode_combo_choice():
                
    digits = (input("Do you want digits? | Yes or No: ")).lower()
    letters = (input("Do you want letters? | Yes or No: ")).lower()
    puncts = (input("Do you want punctuations? | Yes or No: ")).lower()
    Yes = True
    No = False

    try:
        digits = eval(digits.title())
        letters = eval(letters.title())
        puncts = eval(puncts.title())
        return [digits, letters, puncts]
    except NameError:
        print("Invalid value. Use either Yes or No")
        print("Invalidity returns a default, try again to regenerate")
        return [Yes, Yes, Yes]

def user_choice_combo(choices):
    string_constant = ''
    string_constant += num if choices[0] else ''
    string_constant += let if choices[1] else ''
    string_constant += pun if choices[2] else ''
    return string_constant


while True:
    name = str(input('Enter Yes to initiate | type END to exit: ').lower())
    length = get_passcode_lenght()
    choice_list = passcode_combo_choice()
    password = passcode_generator(length,choice_list)

    if name == 'end':
        print('Thanks!')
        break

    else:
        if name == 'yes':
            print(password)



if __name__ == '__main__':
    length = get_passcode_lenght()
    choice_list = passcode_combo_choice()
    password = passcode_generator(choice_list, length)
    print(password)
