from appium import webdriver


class Driver:
    # 定义
    app_driver = None
    """定义一个获取driver的类"""

    @classmethod
    def get_app_driver(cls):
        """声明driver"""
        if cls.app_driver is None:
            # server 启动参数
            desired_caps = {
                'platformName': 'Android',
                'platformVersion': '5.1',
                'deviceName': 'sanxing',
                'appPackage': 'com.android.settings',
                'appActivity': '.Settings'
            }

            # 声明我们的driver对象
            cls.app_driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
            return cls.app_driver
        else:
            return cls.app_driver

    @classmethod
    def quit_app_driver(cls):
        """关闭app"""
        if cls.app_driver is None:
            cls.app_driver.quit()
            # 重新将app_driver置为None
            cls.app_driver = None
