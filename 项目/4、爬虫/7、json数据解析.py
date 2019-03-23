import json
'''
概念：一种保存数据的格式
作用：可以保存本地的json文件，也可以将json串进行传输
通常将json称为轻量级的传输方式

json文件组成
{}：代表对象（字典）
[]：代表列表
: ：代表键值对
, ：分隔两个部分

'''

jsonStr = '''{
  "breakfast_menu" : {
    "food" : [
      {
        "calories" : "650",
        "description" : "two of our famous Belgian Waffles with plenty of real maple syrup",
        "name" : "Belgian Waffles",
        "price" : "$5.95"
      },
      {
        "calories" : "900",
        "description" : "light Belgian waffles covered with strawberries and whipped cream",
        "name" : "Strawberry Belgian Waffles",
        "price" : "$7.95"
      },
      {
        "calories" : "900",
        "description" : "light Belgian waffles covered with an assortment of fresh berries and whipped cream",
        "name" : "Berry-Berry Belgian Waffles",
        "price" : "$8.95"
      },
      {
        "calories" : "600",
        "description" : "thick slices made from our homemade sourdough bread",
        "name" : "French Toast",
        "price" : "$4.50"
      },
      {
        "calories" : "950",
        "description" : "two eggs, bacon or sausage, toast, and our ever-popular hash browns",
        "name" : "Homestyle Breakfast",
        "price" : "$6.95"
      }
    ]
  }
}'''
# 将json格式的字符串转成Python数据类型
# print(type(jsonStr))
jsonData = json.loads(jsonStr)
# print(jsonData)
# print(type(jsonData))
# print(jsonData["breakfast_menu"]["food"])

# 将pythonData格式的字符串转成json数据类型
pythonStr = {'breakfast_menu': {'food': [{'calories': '650', 'description': 'two of our famous Belgian Waffles with plenty of real maple syrup', 'name': 'Belgian Waffles', 'price': '$5.95'}, {'calories': '900', 'description': 'light Belgian waffles covered with strawberries and whipped cream', 'name': 'Strawberry Belgian Waffles', 'price': '$7.95'}, {'calories': '900', 'description': 'light Belgian waffles covered with an assortment of fresh berries and whipped cream', 'name': 'Berry-Berry Belgian Waffles', 'price': '$8.95'}, {'calories': '600', 'description': 'thick slices made from our homemade sourdough bread', 'name': 'French Toast', 'price': '$4.50'}, {'calories': '950', 'description': 'two eggs, bacon or sausage, toast, and our ever-popular hash browns', 'name': 'Homestyle Breakfast', 'price': '$6.95'}]}}
pythonData = json.dumps(pythonStr)
# print(pythonData)
# print(type(pythonData))

# 读取本地的json文件
path1 = r"C:\学习\扣丁学堂Python语言基础\18、爬虫简介与json\Json\caidanJson.json"
with open(path1, "rb") as f:
    data = json.load(f)
    # print(data)
    # print(type(data))

# 写本地json
path2 = r"C:\学习\TempFile\jsonFile.json"
jsonFile = {'breakfast_menu': {'food': [{'calories': '650', 'description': 'two of our famous Belgian Waffles with plenty of real maple syrup', 'name': 'Belgian Waffles', 'price': '$5.95'}, {'calories': '900', 'description': 'light Belgian waffles covered with strawberries and whipped cream', 'name': 'Strawberry Belgian Waffles', 'price': '$7.95'}, {'calories': '900', 'description': 'light Belgian waffles covered with an assortment of fresh berries and whipped cream', 'name': 'Berry-Berry Belgian Waffles', 'price': '$8.95'}, {'calories': '600', 'description': 'thick slices made from our homemade sourdough bread', 'name': 'French Toast', 'price': '$4.50'}, {'calories': '950', 'description': 'two eggs, bacon or sausage, toast, and our ever-popular hash browns', 'name': 'Homestyle Breakfast', 'price': '$6.95'}]}}
with open(path2, "w") as f:
    json.dump(jsonFile, f)
