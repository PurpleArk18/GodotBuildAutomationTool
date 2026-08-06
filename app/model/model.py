
from dataclasses import dataclass


@dataclass
class Model:

    _debug:bool = False
    _userName:str = ""
    _email:str = ""
    _git_is_configured = False

    def get_git_configured(self) -> bool:
        return self._git_is_configured

    def set_git_configured(self, bIsConfigured:bool) -> None:
        git_is_configured = bIsConfigured
        
    def get_is_debug(self) -> bool:
        return self._debug

    def set_debug(self, bIsDebug:bool) -> None:
        _debug = bIsDebug

    def get_user_name(self) -> str :
        return self._userName

    def set_user_name(self, userName:str) -> None:
        self._userName = userName

    def get_email(self) -> str:
        return self._email

    def set_email(self, email:str) -> None:
        self._email = email