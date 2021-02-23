def find_command(com):
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