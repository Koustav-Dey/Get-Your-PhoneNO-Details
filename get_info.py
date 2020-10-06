import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
from phonenumbers import timezone
from time import time
import time


class bcolors:

    WARNING = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    GREEN = '\033[92m'

print(bcolors.BOLD + bcolors.GREEN + bcolors.UNDERLINE +
      "\n\nGet Your PhoneNO Details :" + bcolors.ENDC)

print(bcolors.BOLD + bcolors.WARNING +
      "\n\nWarning: Use This Tool at Your Own Risk" + bcolors.ENDC)
print(bcolors.BOLD + bcolors.WARNING +
      "========================================" + bcolors.ENDC)


while(True):
    inp = input("\nDo You Want to Continue ! (Y/N) : ")
    if inp == "Y" or inp == "y":

        get_no = input("\nEnter Your Phone Number : ")

        phone_number = phonenumbers.parse(get_no)

        timeZone = timezone.time_zones_for_number(phone_number)
        valid = phonenumbers.is_valid_number(phone_number)
        possible = phonenumbers.is_possible_number(phone_number)

        print("\nGet details About :", get_no,"\nPlease Wait ")
        print(bcolors.WARNING + "\nWaiting ", end="")
        list1 = [".", ".", ".", ".", ".", ".", ".", "."]
        for i in (list1):

            print(f"{i}", end="")
            time.sleep(1)
        print(bcolors.ENDC)

        print("\n\nThe Phone no is Valid :", valid)
        print("The Phone no is Possible :", possible)
        print(phone_number)
        print("TimeZone is : ", timeZone)
        print("Country :", geocoder.description_for_number(phone_number, "en"))
        print("Service Provider Name :",
              carrier.name_for_number(phone_number, "en"))
        print("\n\n")

    else:
        exit(0)
