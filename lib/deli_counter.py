
def line(deli_line=[]):
    if not deli_line:
        print("The line is currently empty.")
    else:
        line_str = "The line is currently:"
        for index, name in enumerate(deli_line, start=1):
            line_str += f" {index}. {name}"
        print(line_str)


def take_a_number(deli_line=[], new_customer=""):
    deli_line.append(new_customer)
    position = len(deli_line)

    print(f"Welcome, {new_customer}. You are number {position} in line.")


def now_serving(deli_line=[]):
    if not deli_line:
        print("There is nobody waiting to be served!")
    else:
        print(f"Currently serving {deli_line[0]}.")
        deli_line.pop(0)
