import logging
import sys


def setup_logging(verbose: bool = False):
    """
    Configure the logging system.

    Args:
        verbose: If True, show INFO level and above. If False, show WARNING and above.
    """
    # Set the root logger level
    root_logger = logging.getLogger()

    # Clear any existing handlers to avoid duplicate logs
    if root_logger.handlers:
        for handler in root_logger.handlers:
            root_logger.removeHandler(handler)

    # Configure logging level based on verbose flag
    log_level = logging.INFO if verbose else logging.WARNING
    root_logger.setLevel(log_level)

    # Create console handler and set its level
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(log_level)

    # Create formatter and add it to the handler
    if verbose:
        # More detailed format for verbose mode
        log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    else:
        # Simpler format for non-verbose mode
        log_format = "%(levelname)s: %(message)s"

    formatter = logging.Formatter(log_format)
    console_handler.setFormatter(formatter)

    # Add the handler to the root logger
    root_logger.addHandler(console_handler)

    # Log initial message to indicate logging is set up
    if verbose:
        logging.info("Verbose logging enabled")
