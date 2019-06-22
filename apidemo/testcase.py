import requests
import pytest

ACCESS_TOKEN = 'xRpCWJ8Ez6giqEpojoIbp-Y-urAR2TN04bngTDHSkD4gdnUB2-ZtIhdvruYQOVfaki4foImLz92XoKd_3KL9AXZv3KCHNZZ1RpP1FSFV4cXDzMzsWMynQUDT5PqMrcKXPuu5x8X6EbiV07rsQ1jSFiBZFQ6iDiiJ6lj-cYEGqQQFFj3-wcG1AeJgYYPKvdLqFGwslRSFl7LD6EIvbwdLJw'
s = requests.session()
# @pytest.mark.parametrize("ACCESS_TOKEN",['jc_TD5N37jB4iOkGUvwqK-WGOLvliSVvTwp1jqMKzLsTJTY_1ERbVLsGQ2rdDVHP_foM-1LEaJwLLTBS19Wfe-82GnCVtYQb0eFTCyfEHrEfST5Bhw2W0jGFWCBAa2aEBTpptT4g1TvPnmccQLSJXZmsfq2WlDPCj57cd19uw1ZQ8FPI2Ti_CQ7HUpxJq1zuGWEAoKlnpMPQ1BLZk-SVfg'])
def test_send():
    url = "https://qyapi.weixin.qq.com/cgi-bin/message/send"
    payload = {'access_token':ACCESS_TOKEN}
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
def test_getmediaid():
    files = {'media': ('h.jpeg', open('/Users/h/Downloads/h.jpeg', 'rb'), 'image/jpeg')}
    TYPE = 'image'
    # proxies = {
    #     "http": "127.0.0.1:8888",
    #     "https": "127.0.0.1:8888",
    # }
    s = requests.session()
    url = 'https://qyapi.weixin.qq.com/cgi-bin/media/upload'
    payload = {'access_token': ACCESS_TOKEN,'type':TYPE}
    res = s.post(url, files=files,params=payload,verify=False).json().get('media_id')
    return res
def test_sendimage():
    url = "https://qyapi.weixin.qq.com/cgi-bin/message/send"
    payload = {'access_token':ACCESS_TOKEN}
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




