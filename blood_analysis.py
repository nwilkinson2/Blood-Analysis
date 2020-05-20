# blood_analysis.py

def HDL_interface():
    print("HDL Interface")
    pass # allows a function to be happy with nothing there- pass is a line of code that doesn't do anything
    
    
def interface():
    print("My Blood Analysis Calculator")
    keep_running = True # boolean variable- can also use a string
    while keep_running: # block of code will continually be run until option 9
        print("Options")
        print("1-HDL Analysis")
        print("9-Quit")
        choice = input("Choose an option: ")
        if choice == "9": # number is a string when you input it!
            keep_running = False
        elif choice == "1":
            HDL_interface()
        
        
if __name__ == "__main__":
    interface() # calls the function- need to do this in if statement!
    