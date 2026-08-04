class Model:

    data = {
        "userName" : "",
        "email" : "",
        "git_is_configured" : "false"
    }

    userName:str = ""
    email:str = ""
    git_is_configured = False

    def getValue(self, key):
        return self.data.get(key)

    def setValue(self, key, value):
        self.data[key] = value