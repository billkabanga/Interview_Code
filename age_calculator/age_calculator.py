"""Age calculator"""
current_year = 2018

def ageCalculator(birth_year):
    age = 0
    birth_year = int(birth_year)
    if  birth_year > 1900:
        age_value = current_year - birth_year
        age += age_value
        print ("You are %d years old." %age)
    else:
        print ("Please enter your year of birth in the format yyyy.")
    return age

if __name__ == '__main__':
    birth_year = input("Enter your year of birth: " )
    ageCalculator(birth_year)