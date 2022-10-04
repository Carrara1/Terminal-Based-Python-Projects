import os
def main(): 
    print("Main Menu")
if __name__ == '__main__':
    main()
#---File Locations  ##TODO make a system to go back to main menu after ending each file.
from location import location
#---This function will access the files.
def run_file(path):
    return exec(open(path).read());
#----------------------------------------------------------------
print("Welcome to the Main Menu.\n" "\nList of programs:\n" "[1] To run password generator; [2] To run bmi calculator; [3] to run rock paper scissors; [4] To run pizza delivery; [5] To run tip calculator; [6] To run band name generator; [7] To run leap year checker; [8] To run treasure RPG; [9] To run treasure map.\n")
selection = input("Select which program you want to run:\n")
#---Extremely simple else/if statement to run the files. 
if selection == "1":
    run_file(location[1])
elif selection == "2":
    run_file(location[2])
elif selection == "3":
    run_file(location[3])
elif selection == "4":
    run_file(location[4])
elif selection == "5":
    run_file(location[5])
elif selection == "6":
    run_file(location[6])
elif selection == "7":
    run_file(location[7])
elif selection == "8":
    run_file(location[8])
elif selection == "9":
    run_file(location[9])
elif selection == "10":
    run_file(location[10])
elif selection == "11":
    run_file(location[11])
else:
    print("Wrong option. Try again. \n")
#------------------------------------------------------------------------------

