from subprocess import Popen, PIPE
import re


class AdbModel(object):
    def __init__(self, dev_id):
        self.__dev_id = dev_id
        self.__ip = "0.0.0.0"

    def is_connected(self):
        cmd = "adb devices"
        p = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)

        while True:
            content = p.stdout.readline().decode("utf-8").strip()
            if len(content) == 0:
                break
            elif content == "List of devices attached":
                continue

            r = re.search("(^[\d\w]+)\s+device", content)
            if r:
                if r.group(1) == self.__dev_id:
                    return True

        return False

    def open_tcpip(self, port=5555):
        if not self.is_connected():
            return False

        cmd = "adb tcpip " + str(port)
        p = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
        while True:
            content = p.stdout.readline().decode("utf-8").strip()
            if len(content) == 0:
                break
            r = re.search("restarting in TCP mode port: ([\d]+)", content)
            if r:
                if r.group(1) == str(port):
                    return True

        return False

    def get_ip(self):
        if not self.is_connected():
            return False

        cmd = "adb shell ifconfig"
        pass

    def install_apk(self):
        pass

    def uninstall_apk(self):
        pass

    def list_packages(self):
        pass

    def connect(self):
        pass
