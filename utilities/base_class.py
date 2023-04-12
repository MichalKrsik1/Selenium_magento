import inspect
import pytest
import logging


@pytest.mark.usefigtures("setup, setup_nolog")
class Base:

    def get_logger(self):
        self.driver.implicitly_wait(2)
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)

        file_handler = logging.FileHandler("log.log")
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

        logger.setLevel(logging.INFO)
        return logger

