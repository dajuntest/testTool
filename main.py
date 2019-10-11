#coding=utf-8

from tool_window.window_run import test_panel
from loguru import logger

class main(object):

    logger.add('./test/log/tool.log', encoding='utf-8')

    test_panel()

if __name__ == '__main__':
    main()