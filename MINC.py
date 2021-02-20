# This is the file you should be running to start up the entire system
import admin
import user
import grafics

while True:
    print("| Modes:\n| 1. User\n| 2. Administrator\n")
    mode = int(grafics.read([{"Enter Mode(1,2)": ""}])[0]["Enter Mode(1,2)"])
    if mode == 1:
        user.main()
        break
    elif mode == 2:
        print("| Refer to ReadMe.txt for these details.")
        while True:
            uname = grafics.read([{"Enter Username": ""}])[0]["Enter Username"]
            if uname=="Admin":
                while True:
                    upass = grafics.read([{"Enter Password": ""}])[0]["Enter Password"]
                    if upass=="c6d9yyacfg":
                        admin.main()
                        break
                    else:
                        print("| Invalid Password")
                break
            else:
                print("| Invalid Username")
        break
    else:
        print("| Please enter a proper option.")