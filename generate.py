
import json
import random


def varname():
    with open("data.json", "r") as f:
        names = json.load(f)
    names = names["var"]["name"]
    for _ in range(5000):
        num = random.randint(0, 3)
        name = ""
        if num == 0:
            for _ in range(random.randint(2, 15)):
                name += chr(random.randint(65, 90))
        if num == 1:
            for _ in range(random.randint(2, 15)):
                name += chr(random.randint(97, 122))
        if num == 2:
            for _ in range(random.randint(2, 15)):
                tmp = random.randint(0, 1)
                if tmp == 0:
                    name += chr(random.randint(97, 122))
                else:
                    name += chr(random.randint(65, 90))
        if num == 3:
            for _ in range(random.randint(2, 15)):
                tmp = random.randint(0, 1)
                if tmp == 0:
                    name += chr(random.randint(97, 122))
                else:
                    name += chr(random.randint(65, 90))
            name = list(name)
            tmp = random.randint(0, 1)
            if tmp == 1:
                name.insert(random.randint(0, len(name)), "-")
            else:
                name.insert(random.randint(0, len(name)), "_")
            name = "".join(name)
        names.append(name)
    with open("./variables/names.txt", "a") as f:
        for i in names:
            f.write(i + "\n")


def varvalue():
    names = []
    for _ in range(5000):
        num = random.randint(0, 5)
        name = ""
        if num == 0:
            for _ in range(random.randint(2, 15)):
                name += chr(random.randint(65, 90))
        if num == 1:
            for _ in range(random.randint(2, 15)):
                name += chr(random.randint(97, 122))
        if num == 2:
            for _ in range(random.randint(2, 15)):
                tmp = random.randint(0, 1)
                if tmp == 0:
                    name += chr(random.randint(97, 122))
                else:
                    name += chr(random.randint(65, 90))
        if num == 3:
            name = str(random.randint(2, 100000000))
        if num == 4:
            name = random.choice(["False","false","true","True"])
        if num == 5:
            name = str(random.uniform(2, 100000000))
            name = truncate(name,random.randint(1,7))
        if num in [0,1,2]:
            tmp = random.randint(0,1)
            if tmp == 0:
                name = "'" + name + "'"
            else:
                name = '"' + name + '"'
        names.append(name)
    with open("./variables/values.txt", "a") as f:
        for i in names:
            f.write(i + "\n")


def make_var_files():
    with open("data.json", "r") as f:
        data = json.load(f)
    templates = data["var"]["templates"]
    with open("./variables/names.txt","r") as f:
        names = f.read().split("\n")
    with open("./variables/values.txt","r") as f:
        values = f.read().split("\n")
    for n in range(10):
        fname = str(n).zfill(6)
        ctemp = random.choice(templates)
        cname = random.choice(names)
        cvalue = random.choice(values)
        with open(f"./Alter/Alter-train/variables/{fname}","w") as f:
            f.write(fit_var_template(ctemp,cname,cvalue))

 
def fit_var_template(template, name, value):
    template = template.replace("{var}",name)
    template = template.replace("{value}",value)
    return template


def truncate(f, n):
    '''Truncates/pads a float f to n decimal places without rounding'''
    s = '{}'.format(f)
    if 'e' in s or 'E' in s:
        return '{0:.{1}f}'.format(f, n)
    i, p, d = s.partition('.')
    return '.'.join([i, (d+'0'*n)[:n]])

varname()
varvalue()
make_var_files()
