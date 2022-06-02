import logging

logging.basicConfig(
    format='%(asctime)s %(levelname)s: %(message)s',
    filemode='log.log',
    level=logging.DEBUG
)


class Logger:
    @staticmethod
    def debug(message: str):
        logging.debug(message)

    @staticmethod
    def info(message: str):
        logging.info(message)

    @staticmethod
    def warning(message: str):
        logging.warning(message)

    @staticmethod
    def error(message: str):
        logging.error(message)

    @staticmethod
    def critical(message: str):
        logging.critical(message)
