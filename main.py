from time_logger import logger_decorator_factory


@logger_decorator_factory('log.txt')
def add(a,b):
    return a+b


print(add(4,5))
