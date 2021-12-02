from typing import Text

from qbittorrentapi.definitions import ClientCache
from qbittorrentapi.request import Request

class Authorization(ClientCache):
    @property
    def is_logged_in(self) -> bool: ...
    def log_in(self, username: Text = None, password: Text = None, **kwargs): ...
    def log_out(self, **kwargs) -> None: ...

class AuthAPIMixIn(Request):
    @property
    def auth(self) -> Authorization: ...
    authorization: Authorization = auth
    @property
    def is_logged_in(self) -> bool: ...
    def auth_log_in(
        self, username: Text = None, password: Text = None, **kwargs
    ) -> None: ...
    @property
    def _SID(self) -> Text | None: ...
    def auth_log_out(self, **kwargs) -> None: ...
