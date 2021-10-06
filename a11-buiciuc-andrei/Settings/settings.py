from jproperties import Properties


class Settings:
    def __init__(self):
        self._configs = Properties()
        self._file_name = 'settings.properties'

        settings_file = open(self._file_name, 'rb')
        self._configs.load(settings_file)

        try:
            self._strategy = self._configs.get("strategy").data
            self._ui = self._configs.get("interface").data
        except KeyError:
            exit(0)

    @property
    def ui(self):
        return self._ui

    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    def strategy(self, value):
        self._strategy = value