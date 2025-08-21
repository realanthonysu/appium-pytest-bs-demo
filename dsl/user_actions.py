# dsl/user_actions.py
from core.navigator import Navigator
from loguru import logger

class UserActions:
    """
    定义用户业务场景的 DSL。
    """
    def __init__(self, navigator: Navigator):
        self.navigator = navigator

    def attempt_login_with_invalid_credentials(self, username, password):
        """
        DSL 方法：尝试使用无效凭据登录。
        """
        login_page = self.navigator.navigate_to_login()
        login_page.login(username, password)
        return login_page.get_error_message()

    def login_successfully(self, username, password):
        """
        DSL 方法：成功登录。
        """
        # 记录业务流程的开始，使用 INFO 级别
        logger.info(f"User Action: Attempting to log in as '{username}'.")
        home_page = self.navigator.login_to_home(username, password)
        logger.info("User Action: Login successful.")
        return home_page
    
    # --- 新增的 DSL 方法 ---
    def logs_out(self):
        """
        DSL 方法：执行登出操作。
        假设用户已经登录并且在一个可以登出的页面。
        登出后返回登录页面对象。
        """
        print("DSL: User is logging out.")
        # 调用 navigator 中对应的导航方法
        return self.navigator.logout_from_home()
