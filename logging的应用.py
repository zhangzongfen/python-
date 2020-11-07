import logging

# logging.basicConfig(level=logging.INFO, format='%(asctime)s-%(name)s-%(levelname)s-%(message)s')
#
# logger = logging.getLogger(__name__)
# logger.info("开始：输出Logger日志")
# logger.debug("debug日志")
# logger.warning("warning日志")
# logger.info("结束：输出logging日志")

# 将日志写入文件
# 定义文件
# logfile = logging.FileHandler('logText.txt', 'a', encoding='utf-8')
# # 设置log日志的级别
# fmt = logging.Formatter(fmt='%(asctime)s-%(name)s-%(levelname)s-%(module)s:%(message)s')
#
# logfile.setFormatter(fmt)
# # 定义日志级别
# LoggerMany = logging.Logger('logTest', level=logging.DEBUG)
# LoggerMany.addHandler(logfile)
# # 写入到logging日志
# LoggerMany.critical('info')
# LoggerMany.info("info日志")
# LoggerMany.debug("debug日志")
# LoggerMany.warning("warning日志")
# LoggerMany.info("info日志")

import logging

# 生成日志实例，日志器
logger = logging.getLogger(__name__)
# 基本单元的配置(LEVER)
logger.setLevel(level=logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# 生成管道分支，处理器
handler_1 = logging.FileHandler("log.txt", encoding="utf-8")
handler_2 = logging.StreamHandler()

# 自定义格式，格式器
handler_1.setFormatter(formatter)
handler_2.setFormatter(formatter)

# 对接分支管道与源头，处理器
logger.addHandler(handler_1)
logger.addHandler(handler_2)

# 层级结构，logger的名称是一个以'.'分割的层级结构，每个'.'后面的logger都是'.'前面的logger的children，通常配合过滤器一起使用
# 过滤器


# 开始记录
logger.debug("芹泽多摩雄")
logger.info("真")
logger.warning("男")
logger.error("人")
logger.critical("！")
