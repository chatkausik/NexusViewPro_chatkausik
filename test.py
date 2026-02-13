from NexusViewPro_chatkausik.logger import logger
from NexusViewPro_chatkausik.custom_exception import InvalidURLException

try:
    raise InvalidURLException()
except Exception as e:
    logger.error(f"An error occurred: {e}")