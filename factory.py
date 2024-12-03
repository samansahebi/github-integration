from abc import ABC, abstractmethod


class GithubIntegration(ABC):

    def __str__(self):
        return self.__class__.__name__

    def __int__(self):
        self.user = None
        self.repo_list = None
        self.host = None

    @abstractmethod
    def authenticate_by_user_pass(self, user, password):
        raise NotImplementedError

    @abstractmethod
    def authenticate_by_token(self, access_token):
        raise NotImplementedError

    @abstractmethod
    def get_repo_list(self):
        raise NotImplementedError
