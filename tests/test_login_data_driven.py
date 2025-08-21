# tests/test_login_data_driven.py
import pytest

# 1. 定义驱动测试的数据
# 结构: (username, password, condition, expected_outcome)
login_test_data = [
    # 场景1: 成功登录
    ("valid_user", "valid_password", "success", "Welcome"),
    
    # 场景2: 无效的用户名或密码
    ("invalid_user", "wrong_password", "failure", "Invalid username or password"),
    
    # 场景3: 密码为空
    ("valid_user", "", "failure", "Password cannot be empty"),
    
    # 场景4: 用户名为空
    ("", "valid_password", "failure", "Username cannot be empty"),

    # ... 未来可以轻松在这里添加更多场景，比如被锁定的用户、格式错误的用户等
]

# 2. 为每个测试场景定义一个清晰的 ID
# pytest 将会在测试报告中使用这些 ID，而不是默认的 0, 1, 2...
test_ids = [
    "Success: Valid Credentials",
    "Failure: Invalid Credentials",
    "Failure: Empty Password",
    "Failure: Empty Username",
]

@pytest.mark.usefixtures("driver")
class TestLoginDataDriven:

    # 3. 使用 @pytest.mark.parametrize 装饰器
    # - 第一个参数是一个字符串，定义了参数名，与测试方法的参数一一对应。
    # - 第二个参数是我们的测试数据集。
    # - `ids` 参数使用了我们定义的 test_ids 列表，让报告更具可读性。
    @pytest.mark.parametrize("username, password, condition, expected_outcome", login_test_data, ids=test_ids)
    def test_login_scenarios(self, user, username, password, condition, expected_outcome):
        """
        一个统一的、由数据驱动的登录测试方法。
        它根据传入的 'condition' 参数来决定执行成功或失败的业务逻辑，并进行相应的断言。
        """
        print(f"\n--- Running test for scenario: {condition.upper()} ---")
        print(f"Credentials: user='{username}', password='{'*' * len(password)}'")
        
        # 4. 根据场景类型，执行不同的 DSL 方法和断言
        if condition == "success":
            # 对于成功场景，调用成功的 DSL 方法
            home_page = user.login_successfully(username, password)
            
            # 断言成功后的页面状态
            actual_message = home_page.get_welcome_message()
            assert expected_outcome in actual_message, \
                f"Expected welcome message to contain '{expected_outcome}', but got '{actual_message}'"
            assert home_page.is_logout_button_displayed(), "Logout button should be visible after successful login"
            
        elif condition == "failure":
            # 对于失败场景，调用失败的 DSL 方法
            error_message = user.attempt_login_with_invalid_credentials(username, password)
            
            # 断言错误信息是否符合预期
            assert error_message == expected_outcome, \
                f"Expected error message '{expected_outcome}', but got '{error_message}'"
        
        else:
            # 如果 condition 值不被支持，则测试失败
            pytest.fail(f"Unsupported test condition: '{condition}'")