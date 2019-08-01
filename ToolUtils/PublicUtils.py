import json
import logging
from configparser import ConfigParser

__Config__DIC__ = {}

def GetDebugMode():
    cfg=ConfigParser()
    cfg.read("config.ini")
    return cfg.getboolean("App", "Debug")

if GetDebugMode():
    logging.basicConfig(format='[%(asctime)s - %(levelname)s] - %(message)s', datefmt='%Y-%b-%d %H:%M:%S',
                        level=logging.DEBUG)
else:
    logging.basicConfig(format='[%(asctime)s - %(levelname)s] - %(message)s', datefmt='%Y-%b-%d %H:%M:%S',
                        level=logging.INFO)

class LOG(object):
    @staticmethod
    def success(value):
        logging.info(value)

    @staticmethod
    def warn(value):
        logging.warning(value)

    @staticmethod
    def debug(value):
        logging.debug(value)

    @staticmethod
    def error(value):
        logging.error(value)

class ProjectConfig():
    @staticmethod
    def INIT(ConfigFileName="config.ini"):
        cfg = ConfigParser()
        cfg.read(ConfigFileName)

        __Config__DIC__["DEBUG_MODE"] = cfg.get("App", "Debug")
        __Config__DIC__["NETINTERFACE"] = cfg.get("App","NetInterfaceName").split(";")

    @staticmethod
    def GetLoggerMode():
        return __Config__DIC__["DEBUG_MODE"]

    @staticmethod
    def GetNetInterface():
        return __Config__DIC__["NETINTERFACE"]

class JsonParser(object):
    @staticmethod
    def JsonToObj(jsonvalue):
        return json.loads(jsonvalue)

    @staticmethod
    def BeautifulOutput(obj):
        LOG.debug(json.dumps(obj,indent=4))

    @staticmethod
    def DicToJson(DIC):
        return json.dumps(DIC)