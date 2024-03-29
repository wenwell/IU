from tools.api import request_tool


def md5_passwds(s, param):
    pass


def test_add_post_json(pub_data):
    method = "POST"  # 请求方法，全部大写
    feature = "订单模块"  # allure报告中一级分类
    story = '签名下单接口'  # allure报告中二级分类
    title = "全字段正常流_4"  # allure报告中用例名字
    uri = "/order/addOrderSignBody"  # 接口地址
    headers = {"token": "${token}"}
    s = "receiver=XX&ordeerPrice=XX&receiverPhone=XX&key=guoya"
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
