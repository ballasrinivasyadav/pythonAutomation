import logging

def test_logging():
    logger = logging.getLogger(__name__)
    fileHandler = logging.FileHandler('logfile.log')
    formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)
    logger.setLevel(logging.WARNING)
    logger.debug("A debug statement is executed")
    logger.info("Information statement")
    logger.warning("something in warning mode")
    logger.critical("it is in critical mode")
