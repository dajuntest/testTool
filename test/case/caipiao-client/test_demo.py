#coding=utf-8

import pytest
from loguru import logger
from selenium import webdriver

@pytest.fixture()
def chrom():
    driver = webdriver.Chrome()
    yield driver
    driver.close()

@pytest.fixture()
def baidu(chrom):
    logger.info('打开百度页面')
    yield chrom.get('https://www.baidu.com')


class TestDemo():

    # @logger.catch()
    @pytest.mark.flaky(reruns=5, reruns_delay=2)
    def test_demo(self, baidu):
        logger.info('输入xxx')
        1 / 0
        assert 1 == 1

if __name__ == '__main__':
    pytest.main(['./case/caipiao-client/test_demo.py'])