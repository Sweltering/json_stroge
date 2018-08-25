# json文件处理
# JSON是一种轻量级的数据交换格式，采用完全独立于编程语言的文本格式；来存储和表示数据，它的层次结构简洁清晰，易于阅读和
# 编写，易于解析，有效提升网络传输效率。


# JSON支持的数据格式：
# 1、对象（字典）
# 2、列表（数组）
# 3、整形、浮点型、布尔类型、null类型
# 4、字符串类型（必须使用双引号，不能使用单引号）
# 多个数据之间使用逗号来分开


# 1、将python的字典和列表转成json
import json

# persons = [
#     {
#         'username': 'wj',
#         'age': 22,
#         'country': '张掖'
#     },
#     {
#         'username': 'tom',
#         'age': 21,
#         'country': '北京'
#     }
# ]

# json_str = json.dumps(persons)  # 将persons列表对象转为json字符串
# print(type(json_str))
# print(json_str)

# dump  将json数据存在文件中
# json编码之后存在文件中
# with open('person.json', 'w') as f:
#     json.dump(persons, f)

# json不编码，直接将中文存在文件中
# with open('person2.json', 'w', encoding='utf-8') as f:
#     json.dump(persons, f, ensure_ascii=False)


# 2、将一个json字符串load成python对象
# json_str = '[{"username": "wj", "age": 22, "country": "\u5f20\u6396"}, {"username": "tom", "age": 21, "country": "\u5317\u4eac"}]'
# persons = json.loads(json_str)
# print(type(persons))
# for person in persons:
#     print(person)

# 从文件中load数据
with open('person.json', 'r') as f:
    persons = json.load(f)
    print(type(persons))
    for person in persons:
        print(person)
