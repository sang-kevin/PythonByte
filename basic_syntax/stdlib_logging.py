import os
import platform
import logging

# print(platform.platform())
# print(os.getenv('HOMEDRIVE'))
# print(os.getenv('HOMEPATH'))
if platform.platform().startswith('Windows'):
    logging_file = os.path.join(os.getenv('HOMEDRIVE'), os.getenv('HOMEPATH'), 'test.log')
else:
    logging_file = os.path.join(os.getenv('HOME'), 'test.log')
print("Logging to", logging_file)

# 配置 logging 模块
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s ：%(levelname)s : %(message)s',
    filename=logging_file,
    filemode='w',
)

logging.debug("Start of the program")
logging.info("Doing something")
logging.warning("Dying now")