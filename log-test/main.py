from demo.dm import log
import logging.config

logging.config.fileConfig('logging.conf')
if __name__ == '__main__':
    log()