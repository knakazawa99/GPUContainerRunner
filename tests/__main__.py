import sys
from unittest import TestLoader
from unittest import TextTestRunner


def main(path):
    loader = TestLoader()
    test = loader.discover(path)
    runner = TextTestRunner()
    runner.run(test)


if __name__ == '__main__':
    main('tests')