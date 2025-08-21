# pages/home_page.py
from appium.webdriver.common.appiumby import AppiumBy
from core.base_page import BasePage
from core.element_descriptor import ElementDescriptor
# 我们需要导入 LoginPage 来进行类型提示
# from pages.login_page import LoginPage 

class HomePage(BasePage):
    """
    主页的 Page Object。
    """
    welcome_message = ElementDescriptor(AppiumBy.ACCESSIBILITY_ID, "welcome-message")
    logout_button = ElementDescriptor(AppiumBy.ACCESSIBILITY_ID, "logout-button")

    def get_welcome_message(self) -> str:
        """获取欢迎信息"""
        return self.welcome_message.text

    def is_logout_button_displayed(self) -> bool:
        """判断登出按钮是否可见"""
        try:
            return self.logout_button.is_displayed()
        except:
            return False
        
    # --- 新增方法 ---
    def click_logout(self):
        """
        点击登出按钮。
        这个操作会导致应用返回登录页。
        """
        print("Clicking logout button on Home Page.")
        self.logout_button.click()
        # 注意：这里不返回一个新的 LoginPage 实例，
        # 因为导航和页面创建的职责在 Navigator 和 PageFactory 中。
