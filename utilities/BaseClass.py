import pytest
import inspect
import logging

@pytest.mark.usefixtures("setup")
class BaseClass:

    def get_log(self):
        logname = inspect.stack()[1][3]
        log = logging.getLogger(logname)

        if not log.handlers:
            file_handler = logging.FileHandler(r"C:\Users\gpnam\PycharmProjects\CookieTesting2\reports\logfile.log", encoding="utf-8")
            formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
            file_handler.setFormatter(formatter)
            log.addHandler(file_handler)
            log.setLevel(logging.INFO)

        return log