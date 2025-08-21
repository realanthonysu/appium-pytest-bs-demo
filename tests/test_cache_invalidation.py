# tests/test_cache_invalidation.py
import pytest



class TestCacheInvalidation:
    
    def test_page_object_is_recreated_after_logout(self, user):
        """
        【优化后】
        通过 DSL 验证登出后，PageFactory 会创建新的页面对象实例。
        测试用例的可读性大大增强，完全聚焦于业务行为。
        """
        print("\n--- Test: Cache Invalidation (DSL Version) ---")
        
        # 步骤 1: 用户第一次成功登录
        print("\nStep 1: First login via DSL")
        home_page_instance_1 = user.login_successfully("valid_user", "valid_password")
        instance_1_id = id(home_page_instance_1)
        print(f"HomePage instance 1 created with ID: {instance_1_id}")

        # 步骤 2: 用户登出
        print("\nStep 2: Logging out via DSL")
        user.logs_out()
        # DSL 方法内部已经处理了导航和缓存清理的复杂逻辑

        # 步骤 3: 用户再次成功登录
        print("\nStep 3: Second login via DSL")
        home_page_instance_2 = user.login_successfully("valid_user", "valid_password")
        instance_2_id = id(home_page_instance_2)
        print(f"HomePage instance 2 created with ID: {instance_2_id}")

        # 步骤 4: 断言
        # 验证核心逻辑：两次获取到的 HomePage 对象是不同的实例
        assert instance_1_id != instance_2_id, \
            "PageFactory returned a cached instance after logout, but a new one was expected."
        
        print("\n--- Test Passed: Cache was successfully invalidated using DSL. ---")