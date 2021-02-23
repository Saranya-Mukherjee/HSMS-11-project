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

trains = []

trains_user = [{"name": "rajdhani kolkata", "cost per ticket": "2000", "source": "kolkata", "destination": "delhi"},
               {"name": "rajdhani patna", "cost per ticket": "2000", "source": "patna", "destination": "delhi"},
               {"name": "rajdhani bombay", "cost per ticket": "2000", "source": "bombay", "destination": "delhi"},
               {"name": "rajdhani bombay", "cost per ticket": "2000", "source": "bombay", "destination": "delhi"},
               {"name": "kolkata shealda", "cost per ticket": "2000", "source": "kolkata", "destination": "ranchi"},
               {"name": "rajdhani bombay", "cost per ticket": "2000", "source": "bombay", "destination": "delhi"},
               {"name": "rajdhani bombay", "cost per ticket": "2000", "source": "bombay", "destination": "delhi"},
               {"name": "rajdhani bombay", "cost per ticket": "2000", "source": "bombay", "destination": "delhi"},
               {"name": "rajdhani bombay", "cost per ticket": "2000", "source": "bombay", "destination": "delhi"},
               {"name": "rajdhani bombay", "cost per ticket": "2000", "source": "bombay", "destination": "delhi"},
               {"name": "rajdhani bombay", "cost per ticket": "2000", "source": "bombay", "destination": "delhi"},
               {"name": "rajdhani bombay", "cost per ticket": "2000", "source": "bombay", "destination": "delhi"},
               {"name": "rajdhani bombay", "cost per ticket": "2000", "source": "bombay", "destination": "delhi"},
               {"name": "rajdhani bombay", "cost per ticket": "2000", "source": "bombay", "destination": "delhi"},
               {"name": "rajdhani bombay", "cost per ticket": "2000", "source": "bombay", "destination": "delhi"},
               {"name": "rajdhani bombay", "cost per ticket": "2000", "source": "bombay", "destination": "delhi"},
               {"name": "rajdhani bombay", "cost per ticket": "2000", "source": "bombay", "destination": "delhi"},
               {"name": "rajdhani bombay", "cost per ticket": "2000", "source": "bombay", "destination": "delhi"},
               ]

def make_number(d):
    n=1
    for a in d:
       d[n-1]["Number"]=str(n)
       n+=1
    return d

def make_train():
    global trains,trains_user
    for n in trains_user:
        t=[]
        n["year"]="2004"
        t.append(n)
        trains.extend(t)
    return trains

def find_command(com):
    if "book" in com:
        return "booking"
    elif "cancel" in com:
        return "canceling"
    elif "show" in com:
        return "listAll"
    elif "list" in com:
        return "listAll"
    elif "details" in com:
        return "listAll"
    elif "exit" in com:
        return "exit"
    elif "end" in com:
        return "exit"
    elif "finish" in com:
        return "exit"
    elif "quit" in com:
        return "exit"
    elif "edit" in com:
        return "mod"
    elif "mod" in com:
        return "mod"
    elif "change" in com:
        return "mod"

def find_command_adm(com):
    if "show" in com:
        return "listAll"
    elif "list" in com:
        return "listAll"
    elif "all" in com:
        return "listAll"
    elif "details" in com:
        return "listAll"
    elif "remove" in com:
        return "remove"
    elif "exit" in com:
        return "exit"
    elif "end" in com:
        return "exit"
    elif "finish" in com:
        return "exit"
    elif "quit" in com:
        return "exit"
    elif "edit" in com:
        return "mod"
    elif "mod" in com:
        return "mod"
    elif "change" in com:
        return "mod"
    elif "remove" in com:
        return "rem"
    elif "del" in com:
        return "rem"
    elif "add" in com:
        return "add"
    elif "new" in com:
        return "add"
    elif "create" in com:
        return "add"

# This file provides the interface to the Administrator
import command_admin as command
import data
import grafics

def edit_train():
    final = []
    print("| All Trains: ")
    grafics.show(Trains)
    while True:
        tra=[]
        s = grafics.read([{"Enter Source": ""}])[0]["Enter Source"]
        for a in Trains:
            if s.lower() in a["source"]:
                tra.append(a)
        if len(tra) == 0:
            print("| No such trains are available")
            return "na", []
        # grafics.show(trains)
        if len(tra) == 1:
            # grafics.show(trains)
            break
        d = grafics.read([{"Enter Destination": ""}])[0]["Enter Destination"]
        tra.clear()
        for a in Trains:
            if d.lower() in a["destination"] and s.lower() in a["source"]:
                tra.append(a)
        if len(tra) != 0:
            break
        elif len(tra) == 0:
            print("| No such trains are available")
            return "na", []
    t = 1
    if len(tra) != 1:
        print("| Please select train:")
        grafics.show(data.make_number(tra))
        while True:
            t = int(grafics.read([{"Enter train number": ""}])[0]["Enter train number"])
            if 0 < t <= len(tra):
                break
            else:
                print("| Not a proper train number:")
    if len(tra) == 1:
        grafics.show(tra)
        while True:
            i = grafics.read([{"Only one available. Choose this one?(y,n)": ""}])[0][
                "Only one available. Choose this one?(y,n)"]
            if i.lower() in "n":
                return "na", []
            else:
                break
    while True:
        detail = []
        for i in range(1):
            print("| Please enter new details of the train.")
            detail.append(
                {"Name": "", "Cost per Ticket": "", "Source": "", "Destination": "", "Year of Origin": ""})
        final += grafics.read(detail)
        grafics.show(final)
        grafics.show([{"Previous Name": tra[t - 1]["name"]}])
        y = grafics.read([{"Confirm edit(y/n)": ""}])[0]["Confirm edit(y/n)"]
        if y.lower() == "y":
            break
        else:
            return "",[]
    return tra[t - 1]["name"], final

def add():
    final = []
    while True:
        detail = []
        for i in range(1):
            print("| Please enter details of the new train.")
            detail.append(
                {"name": "", "cost per ticket": "", "source": "", "destination": "", "year": ""})
        final += grafics.read(detail)
        grafics.show(final)
        y = grafics.read([{"Confirm Addition(y/n)": ""}])[0]["Confirm Addition(y/n)"]
        if y.lower() == "y":
            break
        else:
            return []
    return final

def remove():
    cop=[]
    for a in Trains:
        cop.append(a)
    names=[x["Name"] for x in cop]
    # print(Trains)
    n = 1
    for a in cop:
        cop[n - 1]["Number"] = str(n)
        n += 1
    print("| Which one you want to remove? :")
    # print(Trains)
    grafics.show(Trains)
    t=1
    while True:
        if len(Trains) != 1:
            t = int(grafics.read([{"Enter train number": ""}])[0]["Enter train number"])
        if 0 < t <= len(Trains):
            while True:
                y = grafics.read([{f"| Are you sure you want to remove {names[t - 1]}?(y/n)": ""}])[0][
                    f"| Are you sure you want to remove {names[t - 1]}?(y/n)"]
                if y.lower() == "n":
                    print("| Redirecting you to the home page...")
                    return
                elif y.lower() == "y":
                    Trains.pop(t - 1)
                    print(f"| Removed {names[t - 1]}.")
                    print("| Redirecting you to the home page...")
                    return
                else:
                    print("| Not a valid answer.")
        else:
            print("| Not a valid answer.")

Trains=[]

def flush():
    c=0
    for a in Trains:
        if "Number" in a.keys():
            Trains[c].pop("Number")
        c+=1

def main_a():
    Trains=data.make_train()
    while True:
        flush()
        grafics.show([{"Welcome": "You are in Administrator Mode"}, {"Need help": "Just Type out your desired command"}])
        grafics.show(
            [{"1.": "Edit Trains"}, {"2.": "Add Trains"},{"3.": "Remove Trains"}, {"4.": "See all Trains"}, {"5.": "Exit"}])
        com = command.find_command_adm(grafics.read([{"What do you want to do": ""}])[0]["What do you want to do"])
        if com=="listAll":
            print("| Here you go with all Trains.")
            grafics.show(Trains)
        elif com=="mod":
            tr,fin=edit_train()
            if len(fin)==0:
                continue
            c=0
            for a in Trains:
                if a["name"]==tr:
                    # print(Trains, c,len(Trains),fin)
                    Trains[c]["name"]=fin[0]["Name"]
                    Trains[c]["cost per ticket"]=fin[0]["Cost per Ticket"]
                    Trains[c]["source"]=fin[0]["Source"]
                    Trains[c]["destination"]=fin[0]["Destination"]
                    Trains[c]["year"]=fin[0]["Year of Origin"]
                    # print(Trains)
                    break
                c+=1
        elif com=="add":
            fin=add()
            # print(fin)
            if len(fin)!=0:
                Trains.extend(fin)
                # print(Trains)
        elif com=="remove":
            remove()
            flush()
        elif com=="exit":
            exit()
        else:
            print("| Couldn't find the specified command.")

# This file provides the interface to the common user.
import grafics
import data
import command

details=[]

def booking():
    final=[]
    print("| All Trains: ")
    grafics.show(data.trains_user)
    while True:
        trains = []
        s = grafics.read([{"Enter Source": ""}])[0]["Enter Source"]
        for a in data.trains_user:
            if s.lower() in a["source"]:
                trains.append(a)
        if len(trains) == 0:
            print("| No such trains are available")
            return "na", []
        # grafics.show(trains)
        if len(trains) == 1:
            # grafics.show(trains)
            break
        d = grafics.read([{"Enter Destination": ""}])[0]["Enter Destination"]
        trains.clear()
        for a in data.trains_user:
            if d.lower() in a["destination"] and s.lower() in a["source"]:
                trains.append(a)
        if len(trains) != 0:
            break
        elif len(trains) == 0:
            print("| No such trains are available")
            return "na", []
    t = 1
    if len(trains) != 1:
        print("| Please select train:")
        grafics.show(data.make_number(trains))
        while True:
            t = int(grafics.read([{"Enter train number": ""}])[0]["Enter train number"])
            if 0 < t <= len(trains):
                break
            else:
                print("| Not a proper train number:")
    if len(trains)==1:
        grafics.show(trains)
        while True:
            i = grafics.read([{"Only one available. Choose this one?(y,n)": ""}])[0]["Only one available. Choose this one?(y,n)"]
            if i.lower() in "n":
                return "na",[]
            elif i.lower() in "y":
                break
    n = int(grafics.read([{"Number of People": ""}])[0]["Number of People"])
    date=""
    while True:
        date= grafics.read([{"Enter Date of Journey(DD/MM/YYYY)": ""}])[0]["Enter Date of Journey(DD/MM/YYYY)"]
        if len(date)==10 and date[2]==date[5]=="/":
            if int(date[3:5:])<13:
                if date[3:5:] in "02" and int(date[:2:])<29:
                    break
                elif date[3:5:] in "01 03 05 07 08 10 12" and int(date[:2:])<32:
                    break
                elif date[3:5:] in "04 06 09 11" and int(date[:2:])<31:
                    break
                else:
                    print("| Not a valid date. Please try again.")
            else:
                print("| Not a valid date. Please try again.")
        else:
            print("| Not a valid date. Please try again.")
    while True:
        detail = []
        for i in range(n):
            detail.append(
                {"Name": "", "Age": "", "Gender(M/F)": "", "Aadhar number": "", "Food Preference(veg/non-veg)": "",
                 "Birth Preference(upper/lower/middle)": ""})
        final += grafics.read(detail)
        final[len(final)-1]["Date"]=str(date)
        grafics.show(final)
        grafics.show([{"Train": trains[t - 1]["name"]}])
        y = grafics.read([{"Want to book any more tickets?(y/n)": ""}])[0]["Want to book any more tickets?(y/n)"]
        if y.lower() == "y":
            break
        else:
            n = int(grafics.read([{"Number of People More": ""}])[0]["Number of People More"])
    return trains[t - 1]["name"], final

def canceling():
    if len(details)==0:
        print("| You have booked no tickets yet.")
        y = grafics.read([{"Want to book a ticket?(y/n)": ""}])[0]["Want to book a ticket?(y/n)"]
        if y.lower() == "n":
            print("| Redirecting you to the home page...")
            return
        elif y.lower() == "y":
            tr, det = booking()
            if tr == "na":
                print("| Redirecting you to the home page...")
                return
            for a in det:
                a["Train"] = tr
                details.append(a)
            print("| Redirecting you to the home page...")
            return
    final = []
    cop=[]
    for a in details:
        cop.append(a)
    names=[x["Name"] for x in cop]
    # print(details)
    n = 1
    for a in cop:
        cop[n - 1]["Number"] = str(n)
        n += 1
    print("| Which one you want to cancel? :")
    # print(details)
    grafics.show(details)
    t=1
    while True:
        if len(details) != 1:
            t = int(grafics.read([{"Enter ticket number": ""}])[0]["Enter ticket number"])
        elif len(details) == 1:
            print("| You have booked only one ticket.")
        if 0 < t <= len(details):
            while True:
                y = grafics.read([{f"| Are you sure you want to cancel {names[t - 1]}'s ticket?(y/n) :": ""}])[0][
                    f"| Are you sure you want to cancel {names[t - 1]}'s ticket?(y/n) :"]
                if y.lower() == "n":
                    print("| Redirecting you to the home page...")
                    return
                elif y.lower() == "y":
                    details.pop(t - 1)
                    print(f"| Cancelled {names[t - 1]}'s ticket.")
                    print("| Redirecting you to the home page...")
                    return
                else:
                    print("| Not a valid answer.")
        else:
            print("| Not a valid answer.")

def flush_u():
    c=0
    for a in data.trains_user:
        if "Number" in a.keys():
            data.trains_user[c].pop("Number")
        c+=1

def main_u():
    while True:
        flush_u()
        # Show opening screen
        grafics.show([{"Welcome": "This is MINC"}, {"Need help": "Just Type out your desired command"}])
        print("| Options:")
        grafics.show([{"1.": "Book tickets"}, {"2.": "Cancel tickets"}, {"3.": "See all booked tickets"}, {"4.": "Exit"}])
        com = command.find_command(grafics.read([{"What do you want to do": ""}])[0]["What do you want to do"])
        if com == "booking":
            tr, det = booking()
            if tr == "na":
                print("| Redirecting you to the home page...")
                continue
            for a in det:
                a["Train"] = tr
                details.append(a)
            print("| Redirecting you to the home page...")
        elif com == "listAll":
            if len(details) == 0:
                print("| You have booked no tickets yet.")
                y = grafics.read([{"Want to book a ticket?(y/n)": ""}])[0]["Want to book a ticket?(y/n)"]
                if y.lower() == "n":
                    print("| Redirecting you to the home page...")
                    continue
                elif y.lower() == "y":
                    tr, det = booking()
                    if tr == "na":
                        print("| Redirecting you to the home page...")
                        continue
                    for a in det:
                        a["Train"] = tr
                        details.append(a)
                    print("| Redirecting you to the home page...")
                    continue
            print("| Here you go with all ticket details")
            grafics.show(details)
            continue
        elif com == "canceling":
            canceling()
            det = details.copy()
            details.clear()
            for a in det:
                a.pop("Number")
                details.append(a)
            print("| Here are your left over tickets.")
            grafics.show(details)
        elif com == "exit":
            print("| Thanks for visiting us.\n| May you have a happy journey.")
            exit()
        else:
            print("| Couldn't find the specified command.")

if __name__ == '__main__':
    while True:
        print("| Modes:\n| 1. User\n| 2. Administrator\n")
        mode = int(read([{"Enter Mode(1,2)": ""}])[0]["Enter Mode(1,2)"])
        if mode == 1:
            main_u()
            break
        elif mode == 2:
            print("| Refer to ReadMe.txt for these details.")
            while True:
                uname = read([{"Enter Username": ""}])[0]["Enter Username"]
                if uname == "Admin":
                    while True:
                        upass = read([{"Enter Password": ""}])[0]["Enter Password"]
                        if upass == "c6d9yyacfg":
                            main_a()
                            break
                        else:
                            print("| Invalid Password")
                    break
                else:
                    print("| Invalid Username")
            break
        else:
            print("| Please enter a proper option.")