import time

from base.box import TestSuite, TestRunner, CsvHelper, Email
from case.baidu.baidu_search_test import BaiduSearchTest
from case.ranzhi.add_user_test import AddUserTest


class RanzhiRunner(object):
    def run_test(self):

        """
        运行测试
        :return:
        """

        suite = TestSuite()

        csv_data = CsvHelper().read_data_as_dict("runner/data/ranzhi_runner.csv")

        test_time = time.strftime("%Y%m%d_%H%M%S", time.localtime())

        logger_file = "./runner/log/ranzhi_automate_log_%s.log" % test_time

        for row in csv_data:

            test_class = row["class"]
            test_method = row["test"]
            test_count = int(row["count"])

            for i in range(test_count):

                # 增加测试用例，这里要增加
                if test_class == "AddUserTest":
                    suite.add_test(AddUserTest(test_method, logger_file))
                if test_class == "BaiduSearchTest":
                    suite.add_test(BaiduSearchTest(test_method, logger_file))

        # 测试报告的文件

        report_file = "./runner/report/ranzhi_automate_report_%s.html" % test_time

        runner = TestRunner(file_name=report_file,
                            verbosity=2,
                            title="然之系统自动化测试报告",
                            description="具体测试报告内容如下: ")
        runner.run(suite)

        # 发送测试报告到指定邮箱

        Email().email_attachment(report_file)

