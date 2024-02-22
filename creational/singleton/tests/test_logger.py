from creational.singleton.logger import Logger


def test_logger():
    logger1 = Logger()
    logger2 = Logger()

    assert logger1 is logger2
