"""
   json 操作
"""
import json

list1 = [1,2,3,4,5]
print("\n对列表,元祖，字典 进行序列化和反序列化的处理")

print("\n列表未序列化之前的数据类型：",type(list1))

list_str = json.dumps(list1)

print('列表序列化之后的数据：{0}和类型{1}'.format(list_str,type(list_str)))

# 对字符串反序列化处理
str_list = json.loads(list_str)

print('字符串list_str反序列化的内容：{0}和类型：{1}'.format(str_list,type(str_list)))

