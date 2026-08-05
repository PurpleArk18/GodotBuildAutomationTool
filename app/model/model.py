class Model:

    data = {
        "userName" : "",
        "email" : "",
        "git_is_configured" : "false"
    }

    _userName:str = ""
    _email:str = ""
    _git_is_configured = False

    def getValue(self, key):
        return self.data.get(key)

    def setValue(self, key, value):
        self.data[key] = value
        
    def setGitConfigured(bIsConfigured:bool) -> None:
        git_is_configured = bIsConfigured
        
    