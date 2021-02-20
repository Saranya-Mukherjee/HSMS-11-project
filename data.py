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