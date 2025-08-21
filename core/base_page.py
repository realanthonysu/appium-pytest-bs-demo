# core/base_page.py
from appium.webdriver.webdriver import WebDriver

class BasePage:
    """
    所有 Page Object 的基类。
    """
    def __init__(self, driver: WebDriver):
        if not isinstance(driver, WebDriver):
            raise TypeError("Driver must be a WebDriver instance.")
        self.driver = driver

    def get_title(self) -> str:
        """获取页面标题 (示例方法)"""
        # 具体的实现取决于应用是原生还是Web
        # 这里仅作示例
        if 'browserName' in self.driver.capabilities:
            return self.driver.title
        else:
            # 对于原生应用，可能需要查找一个特定的标题元素
            # raise NotImplementedError("get_title not implemented for native app")
            return "Native App" # 占位