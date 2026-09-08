
from dataclasses import dataclass


@dataclass
class Model:

    _debug:bool = False
    _userName:str = ""
    _email:str = ""
    _git_is_configured = False
    _use_github:bool = False
    _github_is_configured:bool = False
    _current_branch:str = ""
    _repo_path:str = ""
    _scons_is_configured:bool = False

    def get_is_debug(self) -> bool:
        return self._debug

    def set_debug(self, bIsDebug:bool) -> None:
        _debug = bIsDebug

    def get_git_configured(self) -> bool:
        return self._git_is_configured

    def set_git_configured(self, bIsConfigured:bool) -> None:
        self.git_is_configured = bIsConfigured

    def get_user_name(self) -> str :
        return self._userName

    def set_user_name(self, userName:str) -> None:
        self._userName = userName

    def get_email(self) -> str:
        return self._email

    def set_email(self, email:str) -> None:
        self._email = email

    def get_use_github(self) -> bool:
        return self._use_github

    def set_use_github(self, useGithub:bool) -> None:
        self._use_github = useGithub

    def set_current_branch(self, newBranch:str) -> None:
        self.current_branch = newBranch

    def get_current_branch(self) -> str:
        return self.current_branch

    def get_repo_path(self) -> str:
        return self._repo_path

    def set_repo_path(self, path:str) -> None:
        self._repo_path = path
