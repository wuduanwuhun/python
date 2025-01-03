# 1.练习深copy与浅copy
# import copy
#
#
# def use_copy1():
#     num1 = [1, 2, 3, 4, 5]
#     num2 = num1.copy()
#     num2[3] = 18
#     print(num1)
#     print(num2)
#     print(id(num1))
#     print(id(num2))
#
#
# def use_copy2():
#     num1 = [1, 2, 3]
#     num2 = [4, 5, 6]
#     num3 = [num1, num2]
#     num4 = copy.copy(num3)
#     num1[2] = 18
#     print(num3)
#     print(num4)
#     print(id(num3[0]), id(num3[1]))
#     print(id(num4[0]), id(num4[1]))
#
# def use_deepcopy():
#     num1 = [1, 2, 3]
#     num2 = [4, 5, 6]
#     num3 = [num1, num2]
#     num4 = copy.deepcopy(num3)
#     num1[2] = 18
#     print(num3)
#     print(num4)
#     print(id(num3[0]), id(num3[1]))
#     print(id(num4[0]), id(num4[1]))
#
#
# if __name__ == '__main__':
#     use_copy1()
#     use_copy2()
#     use_deepcopy()
import re


# 2.练习上课匹配单个字符，多个字符，匹配分组的正则表达式案例
# import re
#
#
# # 匹配单个字符
# def singler_match():
#     ret = re.match('.', "hello world")
#     print(ret.group())
#
#     ret = re.match('h.l', "hello world")
#     print(ret.group())
#     # 匹配0-9的数字
#     ret = re.match('a[0-9]b', 'a1b a2b a3b acb ayb')
#     print(ret.group())
#
#     #匹配大小写字母
#     ret = re.match('[aA]', 'Ahahaha')
#     print(ret.group())
#
#     #使用\d匹配数字
#     ret = re.match(r"\d连胜", "2连胜, 胜利")
#     print(ret.group())
#
#     # \D匹配非数字
#     ret = re.match(r"\D下无敌", "天下无敌")
#     print(ret.group())
#
#     # \w 匹配字母或数字或下划线
#     ret = re.match(r"\whe", "_hello_world123")
#     print(ret.group())
#
#
# # 匹配多个字符
#
# def mutiple_match():
#     ret = re.match("[A-Z][a-z]*", "Hello world")
#     print(ret.group())
#
#     # 匹配多个单词
#     ret = re.match(r"[1-9]?[0-9]", "88")
#     print(ret.group())
#
#     # 匹配多个数字
#     ret = re.match(r"[1-9]?\d", "123")
#     print(ret.group())
#
#     # 匹配多个字母
#     ret = re.match("[a-zA-Z0-9]{4}", "abcdefghijklmnop")
#     print(ret.group())
#
#     # 匹配多个字母或数字
#     ret = re.match("[a-zA-Z0-9]{4,8}", "abcdefghijklmnop")
#     print(ret.group())
#
#
# # 匹配分组
# DEF_REGEX = r"(?P<name>[a-zA-Z]+)\s+(?P<age>\d+)"
#
#
# def group_match():
#     # 匹配单个分组
#     ret = re.match(r"\w{4,10}@(qq|163)\.com", "abc123@qq.com")
#     print(ret.group())
#
#     ret = re.match(r"\w{4,10}@(qq|163)\.com", "abc123@163.com")
#     print(ret.group())
#
#     ret = re.match(r"([^-]+)-(\d+)", "abc-123")
#     print(ret.group(1), ret.group(2))
#
#     ret = re.match(r"<[a-zA-Z]*>\w*</[a-zA-Z]*>", "<div>hello</div>")
#     print(ret.group())
#
#     ret = re.match(r"<([a-zA-Z]*)>\w*</\1>", "<div>helloworld</div>")
#     print(ret.group())
#
#
# if __name__ == '__main__':
#     singler_match()
#     mutiple_match()
#     group_match()

# 3.练习上课的search，findall,sub等案例
def search_match():
    # search匹配
    ret = re.search(r'\d+', "aabbccddee:777788889999")
    print("search的结果：")
    print(ret.group())


def findall_match():
    ret = re.findall(r'\d+', "aa:9999,bb:1111,c=1000")
    print("findall的结果：")
    print(ret)


def sub_match():
    ret = re.sub(r'\d+',"10086","aaa=997,b:777")
    print("sub的结果：")
    print(ret)


if __name__ == '__main__':
    search_match()
    findall_match()
    sub_match()