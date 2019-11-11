from idlelib.multicall import r

from tools.api import request_tool


def test_add_prod(pub_data):
    method = "POST"  # 请求方法，全部大写
    feature = "产品模块"  # allure报告中一级分类
    story = '新增产品接口'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/product/addProd"  # 接口地址
    headers = {"token": pub_data["token"]}
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    json_data = '''
 {
  "brand": "华为",
  "colors": [
    "blue","yellow","black","red"
  ],
  "price": 2000,
  "productCode": "自动生成 字符串 3,8 中文数字字母特殊字符",
  "productName": "mi8k",
  "sizes": [
    "5寸"
  ],
  "type": "手机"
}
    '''
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(headers=headers, method=method, url=uri, pub_data=pub_data, json_data=json_data,
                         status_code=status_code, expect=expect, feature=feature, story=story, title=title)
    pub_data["skuCode"] = r.json()["data"][0]["skuCode"]


def test_change_price(pub_data):
    method = "POST"  # 请求方法，全部大写
    feature = "产品模块"  # allure报告中一级分类
    story = '修改商品价格'  # allure报告中二级分类
    title = "锁定用户_全字段正常流_1"  # allure报告中用例名字
    uri = "/product/changePrice"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    data = {"SKU": pub_data["skuCode"], "price": 3000}
    headers = {"token": pub_data["token"]}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method, url=uri, pub_data=pub_data, data=data, status_code=status_code, expect=expect,
                         feature=feature, story=story, title=title, headers=headers)


def test_post_changkucun(pub_data):
    method = "POST"  # 请求方法，全部大写
    feature = "产品模块"  # allure报告中一级分类
    story = '修改库存'  # allure报告中二级分类
    title = "全字段正常流_3"  # allure报告中用例名字
    uri = "/product/incrementSku"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    data = {"skuCode": "huawei99_blue_5寸", "qty": 100}
    headers = {"token": pub_data["token"]}
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method, url=uri, pub_data=pub_data, data=data, status_code=status_code, expect=expect,
                         feature=feature, story=story, title=title, headers=headers)


def test_post_json(pub_data):
    method = "POST"  # 请求方法，全部大写
    feature = "订单模块"  # allure报告中一级分类
    story = '下单'  # allure报告中二级分类
    title = "全字段正常流_4"  # allure报告中用例名字
    uri = "/order/addOrder"  # 接口地址
    headers = {"token": pub_data["token"]}
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    json_data = '''
   {
  "ordeerPrice": "3000",
  "orderLineList": [
    {
      "qty": 1,
      "skuCode": "huawei99_blue_5寸"
    }
  ],
  "receiver": "xuepl",
  "receiverPhone": "15062525963",
  "receivingAddress": "上海市",
  "sign": "",
  "userName": "xuepl1111"
}
    '''
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method, url=uri, headers=headers, pub_data=pub_data, json_data=json_data,
                         status_code=status_code, expect=expect, feature=feature, story=story, title=title)


'''
自动生成 数字 20,80   #生成20到80之间的数字 例：56
自动生成 字符串 5 中文数字字母特殊字符 xuepl        #生成以xuepl开头加上长度2到5位包含中文数字字母特殊字符的字符串，例子：xuepl我1
自动生成 地址
自动生成 姓名
自动生成 手机号
自动生成 邮箱
自动生成 身份证号
'''

from tools.api import request_tool


def md5_passwds(s, param):
    pass


def test_add_post_json(pub_data):
    method = "POST"  # 请求方法，全部大写
    feature = "订单模块"  # allure报告中一级分类
    story = '签名下单接口'  # allure报告中二级分类
    title = "全字段正常流_4"  # allure报告中用例名字
    uri = "/order/addOrderSignBody"  # 接口地址
    headers = {"token": pub_data["token"]}
    s = "receiver=xuepl&ordeerPrice=3000&receiverPhone=15062525963&key=guoya"
    sign = md5_passwds(s, "")
    pub_data["sign"] = sign
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    json_data = '''
   {
  "ordeerPrice": "3000",
  "orderLineList": [
    {
      "qty": 1,
      "skuCode": "huawei99_blue_5寸"
    }
  ],
  "receiver": "xuepl",
  "receiverPhone": "15062525963",
  "receivingAddress": "上海市",
  "sign": "",
  "userName": "xuepl1111"
}
    '''
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method, url=uri, headers=headers, pub_data=pub_data, json_data=json_data,
                         status_code=status_code, expect=expect, feature=feature, story=story, title=title)
