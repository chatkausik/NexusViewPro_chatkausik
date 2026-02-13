from NexusViewPro-chatkausik.logger import logger
from NexusViewPro-chatkausik.custom_exception import InvalidURLException

try:
    raise InvalidURLException()
except Exception as e:
    logger.error(f"An error occurred: {e}")