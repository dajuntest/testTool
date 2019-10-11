from loguru import  logger

logger.add('./log/file_{time}.log', encoding='utf-8')


logger.info('这是一条日志')