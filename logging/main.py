# Main library to work with logging in python.
# Has almost all that you need
import logging

# Setup how many levels you will see
logging.basicConfig(level=logging.DEBUG)

if __name__ == "__main__":
    logging.debug('This is a debug message')
    logging.info('This is an info message')
    logging.warning('This is a warning message')
    logging.error('This is an error message')
    logging.critical('This is a critical message')