data = {
    "userName" : "",
    "email" : ""
}

def getValue(key):
    return data.get(key)

def setValue(key, value):
    data[key] = value