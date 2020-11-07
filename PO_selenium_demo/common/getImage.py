import time, os


def SaveImage(driver, errorImage):
    """case失败截图"""
    Rawpath = os.path.join(os.path.dirname(os.path.dirname(__file__)), "Image")
    NewPicture = Rawpath + "\\" + time.strftime("%Y_%y_%d_%H_%M_%S") + "_" + errorImage
    driver.get_screenshot_as_file(NewPicture)


