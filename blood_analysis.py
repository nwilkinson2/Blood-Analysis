# blood_analysis.py

def interface():
    print("My Blood Analysis Calculator")
    keep_running = True # boolean variable- can also use a string
    while keep_running: # block of code will continually be run until option 9
        print("Options")
        print("9-Quit")
        choice = input("Choose an option: ")
        if choice == "9":
            keep_running = False
        
if __name__ == "__main__":
    interface() # calls the function- need to do this in if statement!
    