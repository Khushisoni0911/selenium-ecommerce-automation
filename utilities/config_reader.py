import configparser
import os


class ConfigReader:

    # Find the project root directory
    BASE_DIR = os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )

    # Build the path to config.ini
    CONFIG_FILE = os.path.join(
        BASE_DIR,
        "config",
        "config.ini"
    )

    # Create ConfigParser object
    config = configparser.ConfigParser()

    # Read configuration file
    config.read(CONFIG_FILE)


    @classmethod
    def get_base_url(cls):
        """Return application base URL."""
        return cls.config.get(
            "application",
            "base_url"
        )


    @classmethod
    def get_browser(cls):
        """Return configured browser."""
        return cls.config.get(
            "browser",
            "browser"
        )


    @classmethod
    def get_explicit_wait(cls):
        """Return explicit wait timeout."""
        return cls.config.getint(
            "timeouts",
            "explicit_wait"
        )