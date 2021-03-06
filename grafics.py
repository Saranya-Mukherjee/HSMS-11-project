# This file handles all grafics.

def find_needed_space(details):
    spaces=[]
    space=0
    for data in details:
        for line in data:
            if len(line + data[line] + " : ") > space:
                space = len(line + data[line] + " : ")
        spaces.append(space)
    return space


def show(details):
    # Details is the list of dictionaries containing all data that needs to be displayed.
    space = find_needed_space(details) + 5
    number=len(details)
    s,m = "",""
    for a in range(space + 1):
        s += "-"
        m+="="
    print(s)
    cnt=0
    for data in details:
        for line in data:
            s1 = "| " + line + " : " + data[line]
            for a in range(space - len(s1)):
                s1 += " "
            s1 += "|"
            print(s1)
        cnt+=1
        if cnt!=number:
            print(m)
    print(s)


def read(details):
    # Details is the list of dictionaries containing all data that needs input.
    space = find_needed_space(details) + 30
    number = len(details)
    s, m = "", ""
    for a in range(space + 1):
        s += "-"
        m += "="
    print(s)
    cnt = 0
    for data in details:
        for line in data:
            s1 = "| " + line + " : "
            if line.lower() in "cost per ticket year age aadhar number number of people enter train number enter ticket number":
                while True:
                    details[cnt][line] = input(s1).strip()
                    if details[cnt][line].isnumeric():
                        break
                    else:
                        print(f"| Not A Valid {line}. Please Enter Again")
            elif line.lower() in "name":
                while True:
                    details[cnt][line] = input(s1).strip()
                    if " " not in details[cnt][line]:
                        print(f"| Please Enter Your Full {line}.")
                    else:
                        break
            elif line.lower() in "gender(m/f)":
                while True:
                    details[cnt][line] = input(s1).strip().lower()
                    if details[cnt][line] not in "male female":
                        print(f"| Please Enter A Valid {line}.")
                    else:
                        break
            elif line.lower() in "food preference(veg/non-veg)":
                while True:
                    details[cnt][line] = input(s1).strip().lower()
                    if details[cnt][line] not in "veg non-veg":
                        print(f"| Please Enter A Valid {line}.")
                    else:
                        break
            elif line.lower() in "birth preference(upper/lower/middle)":
                while True:
                    details[cnt][line] = input(s1).strip().lower()
                    if details[cnt][line] not in "lower middle upper":
                        print(f"| Please Enter A Valid {line}.")
                    else:
                        break
            elif line.lower() in "is that all?(y/n) only one available. choose this one?(y,n)":
                while True:
                    details[cnt][line] = input(s1).strip().lower()
                    if details[cnt][line] not in "y n":
                        print(f"| Please Enter A Valid {line}.")
                    else:
                        break
            else:
                details[cnt][line] = input(s1).strip()
        cnt+=1
        if cnt!=number:
            print(m)
    print(s)
    return details


# d=read([{"Train Name":"","year":"","cost":""},{"Train Name":"","year":""},{"Train Name":"","year":""}])
# d1=read([{"Name":"","Age":"","Gender":"","Aadhar number":""},{"Name":"","Age":"","Gender":"","Aadhar number":""},{"Name":"","Age":"","Gender":"","Aadhar number":""}])
# show(d1)
