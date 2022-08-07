import logging

logging.basicConfig(
    format="%(asctime)s %(levelname)s: %(message)s",
    filemode="log.log",
    level=logging.DEBUG,
)


class Logger:
    @staticmethod
    def info(message: str):
        logging.info(message)

    @staticmethod
    def warning(message: str):
        logging.warning(message)
