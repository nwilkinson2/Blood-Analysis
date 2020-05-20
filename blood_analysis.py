# blood_analysis.py

def LDL_analysis(LDL_result):
    if LDL_result < 130:
        return "Normal"
    elif 130 <= LDL_result < 160:
        return "Borderline High"
    elif 160 <= LDL_result < 190:
        return "High"
    elif LDL_result >=190:
       return "Very High"

def HDL_analysis(HDL_result):
    if HDL_result >= 60:
        return "Good"
    elif 40<= HDL_result <60:
        return "Borderline"
    else:
        return "Bad"
        
def LDL_interface():
    # Input should be LDL=130
    print("LDL Interface")
    print("Please input the result in the following format: ")
    print("  LDL=### is the numeric result")
    LDL_input = input("Result: ")
    LDL_result = LDL_input.split("=")
    LDL_status = LDL_analysis(int(LDL_result[1]))
    print("LDL status is {}".format(LDL_status))

def HDL_interface():
    # Input should be HDL=66
    print("HDL Interface")
    print("Please input the result in the following format: ")
    print("  HDL=## where ## is the numeric result")
    HDL_input = input("Result: ")
    HDL_result = HDL_input.split("=") 
    HDL_status = HDL_analysis(int(HDL_result[1]))
    print("HDL status is {}". format(HDL_status))
    pass # allows a function to be happy with nothing there- pass is a line of code that doesn't do anything

def TC_interface():
    print("Total Cholesterol Interface")
    print("Please input the result in the following format: ")
    print("  TC=### where ### is the numeric result")
    TC_input = input("Result: ")

    
def interface():
    print("My Blood Analysis Calculator")
    keep_running = True # boolean variable- can also use a string
    while keep_running: # block of code will continually be run until option 9
        print("\nOptions")
        print("1-HDL Analysis")
        print("2-LDL Analysis")
        print("9-Quit")
        print("3-Total Cholesterol Check")
        choice = input("Choose an option: ")
        if choice == "9": # number is a string when you input it!
            keep_running = False
        elif choice == "1":
            HDL_interface()
        elif choice == "2":
            LDL_interface()
        elif choice == "3":
            TC_interface()
        
        
if __name__ == "__main__":
    interface() # calls the function- need to do this in if statement!
    