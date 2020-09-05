from loguru import logger

def echo_start_end(func):
    def wrapper(*args,**kwargs):
        logger.info('[start]')
        func(*args,**kwargs)
        logger.info('[end]')
    return wrapper
