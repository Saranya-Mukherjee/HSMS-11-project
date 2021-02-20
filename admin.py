# This file provides the interface to the Administrator
import command_admin as command
import data
import grafics

def edit_train():
    final = []
    print("| All Trains: ")
    grafics.show(trains)
    while True:
        tra=[]
        s = grafics.read([{"Enter Source": ""}])[0]["Enter Source"]
        for a in trains:
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
        for a in trains:
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
        grafics.show(data.make_number(trains))
        while True:
            t = int(grafics.read([{"Enter train number": ""}])[0]["Enter train number"])
            if 0 < t <= len(trains):
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
        grafics.show([{"Previous Name": trains[t - 1]["name"]}])
        y = grafics.read([{"Confirm edit(y/n)": ""}])[0]["Confirm edit(y/n)"]
        if y.lower() == "y":
            break
        else:
            break
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
    grafics.show(trains)

trains=[]

def flush():
    c=0
    for a in trains:
        if "Number" in a.keys():
            trains[c].pop("Number")
        c+=1

if __name__ == '__main__':
    trains=data.make_train()
    while True:
        flush()
        grafics.show([{"Welcome": "You are in Administrator Mode"}, {"Need help": "Just Type out your desired command"}])
        com = command.find_command(grafics.read([{"What do you want to do": ""}])[0]["What do you want to do"])
        if com=="listAll":
            print("| Here you go with all Trains.")
            grafics.show(trains)
        elif com=="mod":
            tr,fin=edit_train()
            c=0
            for a in trains:
                if a["name"]==tr:
                    print(trains,c)
                    trains.pop(c)
                    trains[c]["name"]=fin[0]["Name"]
                    trains[c]["cost per ticket"]=fin[0]["Cost per Ticket"]
                    trains[c]["source"]=fin[0]["Source"]
                    trains[c]["destination"]=fin[0]["Destination"]
                    trains[c]["year"]=fin[0]["Year of Origin"]
                    print(trains)
                    break
                c+=1
        elif com=="add":
            fin=add()
            print(fin)
            if len(fin)!=0:
                trains.extend(fin)
                print(trains)
        elif com=="exit":
            exit()