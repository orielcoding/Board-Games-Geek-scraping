import logging
import functools


def create_logger():
    # creates a logger object

    log_file = "bgg_scraping.log"
    log_level = logging.INFO
    logging.basicConfig(level=log_level, filename=log_file, filemode="w+",
                        format="%(asctime)-15s %(levelname)-8s %(message)s")
    lg = logging.getLogger("exc_logger")
    return lg


def exception(func):
    """
    A decorator that wraps the passed in info-logger and also logs
    exceptions should one occur
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger = create_logger()
        try:
            result = func(*args, **kwargs)
            logger.info("Executing %s", func.__name__)
            return result
        except ValueError:
            logger.exception("message")
            raise
        except KeyboardInterrupt:
            raise
        except Exception:
            # log the exception
            err = f"There was an exception in {func.__name__}:"
            logger.exception(err)
            # re-raise the exception
            raise
    return wrapper
