import logging
import os


class Logger:

    @staticmethod
    def get_logger(name):

        # Create logs directory
        log_directory = "logs"
        os.makedirs(log_directory, exist_ok=True)

        # Create logger
        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)

        # Prevent duplicate handlers
        if not logger.handlers:

            # Log format
            formatter = logging.Formatter(
                "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
            )

            # Save logs to file
            file_handler = logging.FileHandler(
                os.path.join(log_directory, "automation.log")
            )
            file_handler.setFormatter(formatter)

            # Display logs in terminal
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)

            logger.addHandler(file_handler)
            logger.addHandler(console_handler)

        return logger