"""
•	编写 Calc 这个类add() ，div() 这两个方法的测试用例
•	按照等价类去设计测试用例
以下用例的设计，以办公计算器为例设计的
"""
# 定义TestCalc类
import random
import pytest
import yaml
from python_pytest.python_code.cacl import Calc


class TestCalc:
    def setup_class(self):
        self.calc = Calc()  # 在setupclass方法中实例化类，实例化对象，在整个类中都可以使用，提高运行速度

    def teardownclass(self):
        pass

    # 定义test_add方法——测试有效等价类，用于测试被测代码中的加法方法是否正确，参数传入被测数据
    @pytest.mark.parametrize('a, b, expect', yaml.safe_load(open("calc_add_data.yaml")))
    def test_add(self, a, b, expect):
        # Decimal('0.1') + Decimal('0.2')  # 如需精确计算浮点数，需用Decimal，因为python的浮点数计算不太精确。
        result = self.calc.add(a, b)  # 计算2个数相加，并赋值给result
        print(f"result========={result}")  # 打印result的值
        assert result == expect  # 断言result与预期结果expect的值相等，相等该用例就运行通过，不相等该用例就运行失败

    # 定义test_add_out方法——测试无效等价类，用于测试被测代码中相加结果超过12位，就抛出超过范围的异常
    @pytest.mark.xfail(raises=Exception)
    def test_add_out(self):
        a = random.randint(1, 999999999999)  # 随机生成
        b = 999999999999
        result = self.calc.add(a, b)  # 超出计算器范围，这里是以办公计算器为例
        raise Exception("Out of range")  # 抛出异常描述

    # 定义test_div方法——测试有效等价类，用于测试被测代码中的除法方法是否正确，参数传入被测数据
    @pytest.mark.parametrize('a, b, expect', yaml.safe_load(open("calc_div_data.yaml")))
    def test_div(self, a, b, expect):
        result = self.calc.dev(a, b)  # 计算2个数相除，并赋值给result
        print(f"result========={result}")  # 打印result的值
        assert result == expect  # 断言result与预期结果expect的值相等，相等该用例就运行通过，不相等该用例就运行失败

    # 定义test_div_zero方法——测试无效等价类，用于测试被测代码中被除数为0，就抛出异常
    @pytest.mark.xfail(raises=ZeroDivisionError)  # 标记抛出被除数为0的异常
    def test_div_zero(self):
        a = random.randint(0, 999999999999)  # 随机生成除数
        b = 0  # 被除数为0
        result = self.calc.dev(a, b)  # 被除数为0

if __name__ == '__main__':
    pytest.main(['-v', '-x', 'test_calc.py'])
