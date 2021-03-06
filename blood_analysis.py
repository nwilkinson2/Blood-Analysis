# blood_analysis.py
import json


def LDL_analysis(LDL_result):
    if LDL_result < 130:
        return "Normal"
    elif 130 <= LDL_result < 160:
        return "Borderline High"
    elif 160 <= LDL_result < 190:
        return "High"
    elif LDL_result >= 190:
        return "Very High"


def HDL_analysis(HDL_result):
    if HDL_result >= 60:
        return "Good"
    elif 40 <= HDL_result < 60:
        return "Borderline"
    else:
        return "Bad"


def verify_entry(HDL_result):
    if HDL_result[0] != "HDL":
        return False
    if not HDL_result[1].isnumeric():
        return False
    return True


def LDL_interface(patient):
    # Input should be LDL=130
    print("LDL Interface")
    print("Please input the result in the following format: ")
    print("  LDL=### is the numeric result")
    LDL_input = input("Result: ")
    LDL_result = LDL_input.split("=")
    LDL_status = LDL_analysis(int(LDL_result[1]))
    print("LDL status is {}".format(LDL_status))
    patient["LDL status"] = LDL_status


def HDL_interface(patient):
    # Input should be HDL=66
    print("HDL Interface")
    print("Please input the result in the following format: ")
    print("  HDL=## where ## is the numeric result")
    HDL_input = input("Result: ")
    HDL_result = HDL_input.split("=")
    if verify_entry(HDL_result):
        HDL_status = HDL_analysis(int(HDL_result[1]))
        print("HDL status is {}". format(HDL_status))
    else:
        print("Bad entry")
    patient["HDL status"] = HDL_status
    pass
# allows a function to be happy with nothing there- pass is a line
# of code that doesn't do anything


def TC_interface(patient):
    print("Total Cholesterol Interface")
    print("Please input the result in the following format: ")
    print("  TC=### where ### is the numeric result")
    TC_input = input("Result: ")
    TC_result = TC_input.split("=")
    TC_status = TC_analysis(int(TC_result[1]))
    print("Total Cholesterol status is {}".format(TC_status))
    patient["TC status"] = TC_status


def TC_analysis(TC_result):
    if TC_result >= 240:
        return "High"
    elif 200 <= TC_result <= 239:
        return "Borderline High"
    else:
        return "Normal"


def interface():
    print("My Blood Analysis Calculator")
    print("Insert Patient Data: ")
    a = input("First Name: ")
    b = input("Last Name: ")
    c = input("Age: ")
    profile = create_profile(a, b, c)
    print(profile)
    keep_running = True  # boolean variable- can also use a string
    while keep_running:  # block of code will continually be run until option 9
        print("\nOptions")
        print("1-HDL Analysis")
        print("2-LDL Analysis")
        print("9-Quit")
        print("3-Total Cholesterol Check")
        choice = input("Choose an option: ")
        if choice == "9":  # number is a string when you input it!
            keep_running = False
        elif choice == "1":
            HDL_interface(profile)
        elif choice == "2":
            LDL_interface(profile)
        elif choice == "3":
            TC_interface(profile)
        print(profile)
    output_json(profile)

def create_profile(a, b, c):
    patient = {"First Name": a, "Last Name": b, "Age": c}
    return patient


def output_json(my_dict):
    filename = "patient.json"
    out_file = open(filename, 'w')
    json.dump(my_dict, out_file)
    out_file.close()


def line_equation(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    m = (y1-y2)/(x1-x2)
    b = y1-m*x1
    return m, b


def newPoint(m, b, x):
    y = m*x+b
    return y


def line_generation(p1, p2, x):
    return newPoint(line_equation(p1, p2)[0], line_equation(p1, p2)[1], x)


def line_check(p1, p2, p3):
    a = line_equation(p1, p2)[0]
    b = line_equation(p2, p3)[0]
    if a == b:
        return True
    else:
        return False


if __name__ == "__main__":
    interface()  # calls the function- need to do this in if statement!

