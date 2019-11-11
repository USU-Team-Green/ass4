import random
import json



personlInfoo = {'First Name': 'Jon', 'Last Name': 'Doe', 'DOB': '10/09/1992', 'Phone':'208-123-456', 'Address': {'Street Name': '2660 Main st', 'Apartment Number': '20', 'City': 'Logan', 'State': 'UT', 'Zip': '84321'}, 'Email ID': 'JonDoe@gmail.com'}

#FirstName
def fName_password(s):
    return s

#LastName
def lName_password(s):
    return s

#First Part of Date of birth includinga all
def firstPartDateOfBirth_password(s):
    string = s.replace('/', '')
    firstPart = string[:random.randint(2, len(string)+1)]
    return firstPart

#Second part of date of birth
def secondPartDateOfirth_password(s):
    string = s.replace('/', '')
    secondPart = string[random.randint(2,len(string)-1):]
    return secondPart

#First part of phone including all digits
def firstPartPhone_password(s):
    digits = s.replace('-', '')
    firstPart = digits[:random.randint(2,len(digits)+1)]
    return firstPart

#Second part of phone
def secondPartPhone_password(s):
    digits = s.replace('-', '')
    secondPart = digits[random.randint(2, len(digits)-1):]
    return secondPart

#Street number
def streetNumber_password(s):
    string = s.split(" ", 1)[0]
    return string

#Street Name
def streetName_password(s):
    string = s.split(" ", 1)[1]
    return string

#Apartment Number
def apartment_password(s):
    if s:
        return s
    else:
        return

#city
def city_password(s):
    return s

#state
def state_password(s):
    return s

#zip code
def zip_password(s):
    return s

#Email id
def emailId_password(s):
    email = s.spilt("@")[0]
    string = email[:random.randint(2, len(email))+1]
    return string

#list creator
def enhanced_password_list_creator2():
    with open('personaInfo.jsona') as personalFile:
        personalInfo = json.load(personalfile)
    passwords = open("enhancedPasswordList2.txt", "a")
    final = ""

    #Name
    firstName = fName_password(personalInfo['First Name'])
    final += firstName + '\n'

    lastName = lName_password(personalInfo['Last Name'])
    final += lastName + '\n'
    #Date of birth
    firstPartofDateOfBirth = firstPartDateOfBirth_password(personalInfo['DOB'])
    final += firstPartOfDateOfBirth + '\n'

    secondPartDateOfBirth = secondPartDateOfBirth_password(personalInfo['DOB'])
    final += secondPartDateOfBirth + '\n'
    #Phone
    firstPartPhone = firstPartPhone_password(personalInfo['Phone'])
    final += firstPartPhone + '\n'

    secondPartPhone = secondPartPhone_password(personalInfo['Phone'])
    final += secondPartPhone + '\n'
    #Address
    address = personalInfo['Address']
    streetNumber = streeNumber_password(address['Street Name'])
    final += streetNumber + '\n'

    streetName = streetName_password(address['Street Name'])
    final += streetName + '\n'

    apartment = apartment_password(address['Apartment Number'])
    final += apartment + '\n'
    
    city = city_password(address['City'])
    final += city + '\n'

    state = state_password(address['State'])
    final += State + '\n'
    
    zipCode = zip_password(address['Zip'])
    final += zipCode + '\n'
    #email Id
    emailId = emailId_password(personalInfo['Email ID'])
    final += emailId + '\n'

    passwords.write(final)
    passwords.close





    


        
