from typing import MutableMapping, Text

from qbittorrentapi.definitions import ClientCache
from qbittorrentapi.definitions import Dictionary
from qbittorrentapi.request import Request

class ApplicationPreferencesDictionary(Dictionary): ...
class BuildInfoDictionary(Dictionary): ...

class Application(ClientCache):
    @property
    def version(self) -> Text: ...
    @property
    def web_api_version(self) -> Text: ...
    webapiVersion = web_api_version
    @property
    def build_info(self) -> BuildInfoDictionary: ...
    buildInfo = build_info
    def shutdown(self) -> None: ...
    @property
    def preferences(self) -> ApplicationPreferencesDictionary: ...
    @preferences.setter
    def preferences(self, value: MutableMapping) -> None: ...
    def set_preferences(self, prefs: MutableMapping = None, **kwargs) -> None: ...
    setPreferences = set_preferences
    @property
    def default_save_path(self, **kwargs) -> Text: ...
    defaultSavePath = default_save_path

class AppAPIMixIn(Request):
    @property
    def app(self) -> Application: ...
    application: Application = app
    def app_version(self, **kwargs) -> Text: ...
    def app_web_api_version(self, **kwargs) -> Text: ...
    app_webapiVersion = app_web_api_version
    def app_build_info(self, **kwargs) -> BuildInfoDictionary: ...
    app_buildInfo = app_build_info
    def app_shutdown(self, **kwargs) -> None: ...
    def app_preferences(self, **kwargs) -> ApplicationPreferencesDictionary: ...
    def app_set_preferences(self, prefs: MutableMapping = None, **kwargs) -> None: ...
    app_setPreferences = app_set_preferences
    def app_default_save_path(self, **kwargs) -> Text: ...
    app_defaultSavePath = app_default_save_path
