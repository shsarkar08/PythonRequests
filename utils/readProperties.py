import configparser

config = configparser.RawConfigParser()
config.read('.\\configurations\\config.ini')


class ReadConfig:

    @staticmethod
    def getBaseURI():
        base_uri = config.get('common info', 'BASE_URI')
        return base_uri


