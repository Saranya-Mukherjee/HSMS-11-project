# This file provides the interface to the common user.
import command
import data
import grafics

details = []


def booking():
    final = []
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
                print("| Not a proper train number.")
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

def main():
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