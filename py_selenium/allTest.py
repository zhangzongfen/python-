import os, time, unittest
import HTMLTestReportCN


def getAllcases():
    """
    获取testcase 下的所有测试模块
    :return:
    """
    Testsuite = unittest.defaultTestLoader.discover(
        start_dir=os.path.join(os.path.dirname(__file__), "TestCases"),
        pattern="test*.py"
    )
    return Testsuite


def RunMain():
    """
    生成测试报告，写入指定的reports目录
    :return:
    """
    fp = open(os.path.join(os.path.dirname(__file__), "Reports",
                           time.strftime("%Y-%m-%d-%H-%M-%S") + "report.html"), "wb")
    print(os.path.join(os.path.dirname(__file__), "Reports",
                           time.strftime("%Y-%m-%d-%H-%M-%S") + "report.html"))
    HTMLTestReportCN.HTMLTestRunner(stream=fp, title="python+selenium 自动化测试", description="UI自动化测试").run(getAllcases())


if __name__ == '__main__':
    RunMain()
