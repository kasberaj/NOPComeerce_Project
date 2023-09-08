import configparser


config = configparser.RawConfigParser()
file = "C:\\Users\Raj\PycharmProjects\\NOPCOM\\Configurations\\config.ini"
config.read(file)

class ReadConfig:
    @staticmethod
    def get_username():
        username = config.get('common data', 'Username')
        return username


    @staticmethod
    def get_password():
        password = config.get('common data', 'Password')
        return password
