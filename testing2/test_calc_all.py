# 装饰器中不能self，因为装饰器执行时，还没有self生成
"""
补全测试用例【 加减乘除】
使用 fixture 装置完成计算机器实例的初始化
改造 pytest 的运行规则 ,测试用例命名以 calc_ 开始，【加， 减 ，乘，除】分别为 calc_add, calc_sub，…
自动添加标签(add, sub, mul, div四种)，只运行标签为 add 和 div的测试用例。
封装 add, div 测试步骤到 yaml 文件中
"""
from decimal import Decimal
import pytest
import yaml
from python_pytest.python_code.cacl import Calc

class TestCalc:
    def setup_class(self):
        # self.calc = Calc()  # 在setupclass方法中实例化类，实例化对象，在整个类中都可以使用，提高运行速度
        pass

    def teardown_class(self):
        pass

    @pytest.fixture(autouse=True)  # 使用 fixture 装置完成计算机器实例的初始化
    def instantiation_calc(self):
        self.calc = Calc()

    # 读取测试数据文件
    def get_data():
        test_data = yaml.safe_load(open('calc_data.yaml', encoding='UTF-8'))  # 读取测试数据存放到test_data中
        # add_data = test_data['add']  # 读取加法的所有测试数据赋值给add_data
        # sub_data = test_data['sub']  # 读取减法的所有测试数据赋值给sub_data
        # mul_data = test_data['mul']  # 读取乘法的所有测试数据赋值给mul_data
        # div_data = test_data['div']  # 读取除法的所有测试数据赋值给div_data
        return test_data  # 返回test_data

    # 读取add和div的测试步骤文件
    def get_step(self):
        get_step = yaml.safe_load(open('calc_step.yaml'))  # 读取测试步骤存放到get_step中
        return get_step  # 返回get_step

    # 解析获取到的文件中的加法测试步骤
    def any_step_add(self, a, b, expect):
        steps = TestCalc.get_step(self)  # 调用类的get_step方法
        for step in steps:  # 遍历测试步骤
            if 'add' == step:  # 如果step=add，就执行加法
                result = self.calc.add(Decimal(str(a)), Decimal(str(b)))
                assert result == Decimal(str(expect))  # 断言result与预期结果expect的值相等，相等该用例就运行通过，不相等该用例就运行失败
                print(f"result=={result},expect=={expect}")  # 打印result和expect的值

    # 解析获取到的文件中的除法测试步骤
    def any_step_div(self, a, b, expect):
        steps = TestCalc.get_step(self)  # 调用类的get_step方法
        for step in steps:  # 遍历测试步骤
            if 'div' == step:  # 如果step=div，就执行除法
                result = self.calc.div(Decimal(str(a)), Decimal(str(b)))
                assert result == Decimal(str(expect))  # 断言result与预期结果expect的值相等，相等该用例就运行通过，不相等该用例就运行失败
                print(f"result=={result},expect=={expect}")  # 打印result和expect的值

    @pytest.mark.parametrize('a, b, expect', get_data()['add'])  # 参数化时，调用get_data方法，并传入加法相关测试数据
    def calc__add(self, a, b, expect):
        self.any_step_add(a, b, expect)

    @pytest.mark.parametrize('a, b, expect', get_data()['sub'])  # 参数化时，调用get_data方法，并传入减法相关测试数据
    def calc__sub(self, a, b, expect):
        result = self.calc.sub(Decimal(str(a)), Decimal(str(b)))  # 计算2个数相减，并赋值给result
        assert result == Decimal(str(expect))  # 断言result与预期结果expect的值相等，相等该用例就运行通过，不相等该用例就运行失败
        print(f"result=={result},expect=={expect}")  # 打印result和expect的值# 参数化时，调用get_data方法，并传入减法相关测试数据

    @pytest.mark.parametrize('a, b, expect', get_data()['mul'])  # 参数化时，调用get_data方法，并传入乘法相关测试数据
    def calc__mul(self, a, b, expect):
        result = self.calc.mul(Decimal(str(a)), Decimal(str(b)))  # 计算2个数相乘，并赋值给result
        assert result == Decimal(str(expect))  # 断言result与预期结果expect的值相等，相等该用例就运行通过，不相等该用例就运行失败
        print(f"result=={result},expect=={expect}")  # 打印result和expect的值

    @pytest.mark.parametrize('a, b, expect', get_data()['div'])  # 参数化时，调用get_data方法，并传入除法相关测试数据
    def calc__div(self, a, b, expect):
        if b == 0:
            pytest.raises(ZeroDivisionError, self.any_step_div(a, b, expect))  # 如果除数为零就抛出异常
        elif b != 0:
            self.any_step_div(a, b, expect)

if __name__ == '__main__':
    pytest.main(['-v', '-s', 'test_calc_all.py'])

