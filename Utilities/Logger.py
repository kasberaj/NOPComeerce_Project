import inspect
import logging


class LogGenerator:

    @staticmethod
    def loggen():
        name = inspect.stack()[1][3]
        logger = logging.getLogger(name)
        logfile = logging.FileHandler("C:\\Users\\Raj\\PycharmProjects\\NOPCOM\\LOGS\\NOP.log")
        formats = logging.Formatter("%(asctime)s | %(levelname)s | %(lineno)d | %(funcName)s | %(message)s")
        logfile.setFormatter(formats)
        logger.addHandler(logfile)
        logger.setLevel(logging.INFO)
        return logger
