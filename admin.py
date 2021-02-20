# This file provides the interface to the Administrator
import command_admin as command
import data
import grafics

def edit_train():
    final = []
    print("| All Trains: ")
    grafics.show(data.trains)
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
    if len(trains) == 1:
        grafics.show(trains)
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
            detail.append(
                {"Name": "", "Cost per Ticket": "", "Source": "", "Destination": "", "Year of Origin": ""})
        final += grafics.read(detail)
        grafics.show(final)
        grafics.show([{"Train": trains[t - 1]["name"]}])
        y = grafics.read([{"Want to edit any more trains?(y/n)": ""}])[0]["Want to edit any more trains?(y/n)"]
        if y.lower() == "y":
            break
        else:
            n = int(grafics.read([{"Number of People More": ""}])[0]["Number of People More"])
    return trains[t - 1]["name"], final

def listAll():
    data.make_train()
    grafics.show(data.trains)

if __name__ == '__main__':
    while True:
        grafics.show([{"Welcome": "This is MINC"}, {"Need help": "Just Type out your desired command"}])
        com = command.find_command(grafics.read([{"What do you want to do": ""}])[0]["What do you want to do"])
        if com=="listAll":
            print("| Here you go with all Trains.")
            listAll()
        elif com=="mod":
            tr,fin=edit_train()
            