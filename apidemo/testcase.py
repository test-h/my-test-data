import requests
import pytest
import allure

s = requests.session()
def get_accesstoken():
    paylod = {'corpid':'ww010715afc5b7d56f',
              'corpsecret':'vJs_goMe2pvsiumCFGMloe3jCSfjtW-DKrbTtnEuU-I'}
    url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
    ACCESS_TOKEN = s.get(url=url,params=paylod,verify = False).json().get("access_token")
    return ACCESS_TOKEN
@allure.story("发送消息")
def test_send():
    url = "https://qyapi.weixin.qq.com/cgi-bin/message/send"
    payload = {'access_token':get_accesstoken()}
    send_json = {
   "touser" : "HeYing",
   # "toparty" : "PartyID1|PartyID2",
   # "totag" : "TagID1 | TagID2",
   "msgtype" : "text",
   "agentid" : 1000002,
   "text" : {
       "content" : "上课上课上课"
        },
   "safe":0
    }

    res = s.post(url,json=send_json,params=payload)
    assert res.json().get('errmsg') == 'ok'
@allure.story("获取media_id")
def test_getmediaid():
    files = {'media': ('h.jpeg', open('/Users/h/Downloads/h.jpeg', 'rb'), 'image/jpeg')}
    TYPE = 'image'
    # proxies = {
    #     "http": "127.0.0.1:8888",
    #     "https": "127.0.0.1:8888",
    # }
    s = requests.session()
    url = 'https://qyapi.weixin.qq.com/cgi-bin/media/upload'
    payload = {'access_token':get_accesstoken(),'type':TYPE}
    res = s.post(url, files=files,params=payload,verify=False).json().get('media_id')
    return res
@allure.story("发送图片")
def test_sendimage():
    url = "https://qyapi.weixin.qq.com/cgi-bin/message/send"
    payload = {'access_token':get_accesstoken()}
    send_json = {
        "touser": "HeYing",
        # "toparty": "PartyID1|PartyID2",
        # "totag": "TagID1 | TagID2",
        "msgtype" : "image",
        "agentid" : 1000002,
        "image" : {
            "media_id" : test_getmediaid()
            },
        "safe":0
    }
    send = s.post(url, json=send_json,params=payload,verify=False)
    assert send.json().get('invaliduser') == ''




