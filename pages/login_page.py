# pages/login_page.py
from appium.webdriver.common.appiumby import AppiumBy
from core.base_page import BasePage
from core.element_descriptor import ElementDescriptor


class LoginPage(BasePage):
    """
    登录页面的 Page Object。
    使用 ElementDescriptor 定义元素。
    """
    # 使用描述符来定义元素定位符
    # 只有当 self.username_input 被访问时，元素才会被查找
    username_input = ElementDescriptor(AppiumBy.ACCESSIBILITY_ID, "username-input")
    password_input = ElementDescriptor(AppiumBy.ACCESSIBILITY_ID, "password-input")
    login_button = ElementDescriptor(AppiumBy.ACCESSIBILITY_ID, "login-button")
    error_message = ElementDescriptor(AppiumBy.ACCESSIBILITY_ID, "error-message")

    def enter_username(self, username: str):
        """输入用户名"""
        print(f"Entering username: {username}")
        self.username_input.clear()
        self.username_input.send_keys(username)

    def enter_password(self, password: str):
        """输入密码"""
        print(f"Entering password: {'*' * len(password)}")
        self.password_input.clear()
        self.password_input.send_keys(password)

    def click_login(self):
        """点击登录按钮"""
        print("Clicking login button")
        self.login_button.click()

    def login(self, username, password):
        """封装的登录操作"""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_error_message(self) -> str:
        """获取错误提示信息"""
        return self.error_message.text
