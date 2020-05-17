import pytest

# 给用例自动添加标签(add, sub, mul, div四种)
def pytest_collection_modifyitems(session, config, items:list):
    # print(items)
    # print(type(items))
    # items.reverse()
    for item in items:
        print(item.nodeid)
        if 'add' in item.nodeid:
            item.add_marker(pytest.mark.add)
        if 'sub' in item.nodeid:
            item.add_marker(pytest.mark.sub)
        if 'mul' in item.nodeid:
            item.add_marker(pytest.mark.mul)
        if 'div' in item.nodeid:
            item.add_marker(pytest.mark.div)

# 添加标签，消除运行时的警告，与pytest.ini里的markers功能一样
# def pytest_configure(config):
#     marker_list = ['add', 'sub', 'mul', 'div']
#     for markers in marker_list:
#         config.addinivalue_line('markers', markers)