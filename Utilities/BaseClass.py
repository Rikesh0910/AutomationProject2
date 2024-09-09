import inspect
import logging
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setup")
class BaseClass:

    def get_logger(self):

        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        filehandler = logging.FileHandler("logfile.log")
        format = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        filehandler.setFormatter(format)
        if logger.hasHandlers():
            logger.handlers.clear()
        logger.addHandler(filehandler)
        logger.setLevel(logging.DEBUG)
        return logger

    def select_dropdown(self, obj, value):
        sel = Select(obj)
        sel.select_by_value(value)

    def actionsOnElement(self, drive, val):
        action = ActionChains(drive)
        action.move_to_element(val).perform()
        action.click(val).perform()



