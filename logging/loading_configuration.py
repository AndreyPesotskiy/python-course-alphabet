import logging
import logging.config
import yaml


def setup_logging():
    with open('config.yaml', 'r') as f:
        config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)


def create_random_list():
    import random
    res = [random.randint(1, 5) for _ in range(10)]
    logger.info(res)
    return res


def log_error(message):
    logger.error(message)


def log_info(message):
    logger.info(message)


if __name__ == "__main__":
    setup_logging()
    logger = logging.getLogger("sampleLogger")
    log_info("Say hello")
    log_error("Lets see our error")
    res = create_random_list()
