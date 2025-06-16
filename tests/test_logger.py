from tinnyloggy import Logger

def test_logger_info_enabled():
    log = Logger(enabled=True)
    log.info("Test info message")
    assert True  
