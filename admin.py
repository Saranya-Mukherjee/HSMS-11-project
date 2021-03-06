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
                print("| Not a proper train number.")
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

def listAll():
    grafics.show(Trains)

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

def main():
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