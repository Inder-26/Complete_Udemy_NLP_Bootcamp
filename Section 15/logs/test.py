from logger import logging

def add(a, b):
    logging.debug('The addition operation is taking place')
    return a + b

logging.debug('Addition function is called')
result = add(10, 15)

def sub(a, b):
    logging.debug('The substraction operation is taking place')
    return a - b

logging.debug('Substraction function is called')
result = sub(10, 15)