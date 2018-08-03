"""Age calculator"""
current_year = 2018 #assigning the variable current_year

def ageCalculator(birth_year):#function ageCalculator that takes an argument of the birth_year
    age = 0
    birth_year = int(birth_year)
    if  birth_year > 1900 and birth_year < current_year:#conditional loop for the expected range of birth_year
        age_value = current_year - birth_year
        age += age_value
        print ("You are %d years old." %age)
    else:
        print ("Please enter your year of birth in the format yyyy.")
        return ('Enter valid year')
    
    return age
#requesting for input from the user.
if __name__ == '__main__':
    birth_year = input("Enter your year of birth: " )
    ageCalculator(birth_year)