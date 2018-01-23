from utils import location
from utils.readINI import Readini


class ServerCodeXpath(object):
    def __init__(self, ser_code):
        if isinstance(ser_code, str):
            self.code = ser_code
        else:
            self.code = str(ser_code)

    def getCodeXpath(self):
        codexpath = []
        for i in self.code:
            if i == '0':
                codexpath.append("//android.widget.RelativeLayout[contains(@index,'10')]")
            elif i == '1':
                codexpath.append("//android.widget.TextView[contains(@text,'1')]")
            else:
                codexpath.append("//android.widget.RelativeLayout[contains(@index,'" + str(int(i) - 1) + "')]")
        return codexpath


if __name__ == "__main__":
    server_code = Readini(location.CONF_INI_PATH).ini_data().get('server', 'code')
    print(ServerCodeXpath(server_code).getCodeXpath())
