# Create a dictionary of gendered names
# Design a function for gender_detector
# Create a variable to collect the user's name
# Check for the gender of the user with name entered
# Print the result for the user to see
# If the user's name is genderless, prompt a variable that asks for his gender
# Print that the user's gender has been saved for future usage

gendered_names = {
    "Adenike" : "female",
    "Olawumi" : "female",
    "Adewale" : "male",
    "Bunmi"   : "female",
    "Chris"   : "male",
    "Funmi"   : "female",
    "Yusuff"  : "male",
    "Dare"    : "male",
    "Tunde"   : "male",
    "Yetunde" : "female",
    "Ismail"  : "male",
    "Iyabo"   : "female",
    "Akande"  : "male",
    "Asake"   : "female",
    "Ayoka"   : "female",
    "Akanni"  : "male"
}

def gender_detector():
    print("Welcome to Gender Detector Page")
    user_name = input("Enter your name: ")

    for key, value in gendered_names.items():
        if user_name == key:
            print(f"Welcome, {user_name}! You are a {value} 😘💕💖😜😍")


        elif user_name not in gendered_names.keys():
            user_gender = input("Enter your gender: ")

            if user_gender.lower() not in gendered_names.values():
                print(f"Hey, {user_name}! I don't understand your gender. Enter a correct gender")
            else:
                print(f"Thanks, {user_name}. Your gender is {user_gender}")
                return

gender_detector()
