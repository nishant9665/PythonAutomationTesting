import configparser

config = configparser.RawConfigParser()
config.read(r"C:\\Nishant_Study\\nopcommerce\\nopcommerceAdmin\\Configurations\\config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('common info','baseurl')
        return url

    @staticmethod
    def getUserName():
        userName = config.get('common info', 'username')
        return userName

    @staticmethod
    def getPassword():
        userpassword = config.get('common info', 'password')
        return userpassword