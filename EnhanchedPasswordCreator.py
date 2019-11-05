import fileinput

#repeating
def repeat_password(s):

    string = s.strip()

    string1 = string * 2
    string2 = string * 3

    final = string1 + '\n' + string2

    return final



#reverse
def reverse(s):
  str = ""
  for i in s:
    str = i + str
  return str


#quick adjustments
def quick_adjustments(s):
    str = s.strip()

    final = ""

    str_cap = str.capitalize()

    final += str_cap + '\n'

    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

    for symbol in symbols:
        final += str + symbol + '\n' + str_cap + symbol + '\n'

    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    for number in numbers:
        final += str + number + '\n' + str_cap + number + '\n'

    return final




#insert symbols
def insert_symbols(s):
    str = s.strip()

    final = ""

    for letter in str:

        if letter == 'a':
            strnew = str.replace('a','@')
            final += strnew + '\n'

        if letter == 'i':
            strnew = str.replace('i','!')
            final += strnew + '\n'

        if letter == 's' or 'S':
            strnew = str.replace('s' or 'S','5')
            final += strnew + '\n'


        if letter == 'o' or 'O':
            strnew = str.replace('o' or 'O','0')
            final += strnew + '\n'

        if letter == 'b':
            strnew = str.replace('b','6')
            final += strnew + '\n'

        if letter == 'z':
            strnew = str.replace('z','2')
            final += strnew + '\n'

        if letter == 'e' or 'E':
            strnew = str.replace('e' or 'E','3')
            final += strnew + '\n'

    return final

#any of the above



def enhanched_password_list_creator(password_list):

    passwords = open("enhancedPasswordList.txt", "a")
    final = ""

    for password in password_list:

        #print(password)

        # repeated
        repeated_password = repeat_password(password)
        final += repeated_password + '\n'

        #reversed
        reversed = reverse(password)
        final += reversed + '\n'

        #quick adjustments
        quick = quick_adjustments(password)
        final += quick + '\n'

        #insert symbols
        inserted = insert_symbols(password)
        final += inserted + '\n'

    passwords.write(final)
    passwords.close()







if __name__ == '__main__':

    password_list = open(r"enhancedPasswordList.txt", "r+")
    enhanched_password_list_creator(password_list)
    password_list.close()

    password_list = open(r"enhancedPasswordList.txt", "r+")
    for password in password_list:
        print(password)
    password_list.close()




