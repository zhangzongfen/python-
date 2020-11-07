import xlrd
import logging, os


class Helper(object):
    def readExceles(self, rows):
        book = xlrd.open_workbook("D:\\PyCharm 2019.1.1\\workspace\\python-selenium\\PO_selenium_demo\\data\\info.xlsx", "r")
        table = book.sheet_by_index(0)
        return table.row_values(rows)

    def readusername(self, rows):
        return str(self.readExceles(rows)[0])

    def readpassword(self, rows):
        return str(self.readExceles(rows)[1])

    def exceptText(self, rows):
        return str(self.readExceles(rows)[2])

    def dirname(self, filename, filepath='D:\\PyCharm 2019.1.1\\workspace\\python-selenium\\PO_selenium_demo\\data'):
        return os.path.join(os.path.dirname(os.path.dirname(__file__)), filepath, filename)

    # H = Helper()
    # print(H.readpassword(1))
    # print(round(float(H.readpassword(1))))

    def makelog(self, log_connect):
        logfile = logging.FileHandler(self.dirname('log.txt'), 'a', encoding='utf-8')
        fmt = logging.Formatter(fmt='%(asctime)s-%(name)s-%(levelname)s-%(module)s:%(message)s')
        logfile.setFormatter(fmt)
        logger1 = logging.Logger('logTest', level=logging.INFO)
        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        logger1.addHandler(logfile)
        logger1.info(log_connect)
        console.setFormatter(fmt)
        logger1.addHandler(console)
        logfile.close()
