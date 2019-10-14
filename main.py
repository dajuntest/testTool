#coding=utf-8
from tool_window.tab_logic import WindowCommonFunction
from tool_window.window_run import TestPanel
from loguru import logger

class main(object):

    logger.add('./test/log/tool.log', encoding='utf-8')

    TestPanel(WindowCommonFunction().window)

if __name__ == '__main__':
    main()