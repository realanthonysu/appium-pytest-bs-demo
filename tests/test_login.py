# tests/test_login.py
import pytest


class TestLogin:
    
    def test_login_with_valid_credentials(self, user):
        """
        测试用例：使用有效的凭据成功登录。
        
        这个测试用例的可读性非常高，因为它直接描述了业务场景。
        底层的页面交互、元素定位等复杂性都被封装起来了。
        """
        # DSL 调用
        home_page = user.login_successfully("valid_user", "valid_password")
        
        # 断言
        assert "Welcome" in home_page.get_welcome_message()
        assert home_page.is_logout_button_displayed()

    def test_login_with_invalid_credentials(self, user):
        """
        测试用例：使用无效的凭据登录失败。
        """
        # DSL 调用
        error_msg = user.attempt_login_with_invalid_credentials("invalid_user", "wrong_password")
        
        # 断言
        assert error_msg == "Invalid username or password"