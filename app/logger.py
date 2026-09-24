import logging

# Create our application logger
logger = logging.getLogger("production_ai_api")

# Show INFO level and above
logger.setLevel(logging.INFO)

# Print logs in the terminal
handler = logging.StreamHandler()

# Format every log message
formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(message)s"
)

handler.setFormatter(formatter)

logger.addHandler(handler)