# json由字典和列表组成
import json
import pprint
#
# data = {
#     "name": ["henry", "mj", "draper"],
#     "age": 33,
#     "gender": "male"
# }
#
# print(type(data))
#
# # 将 Python 对象编码成 JSON 字符串
# data1  = json.dumps(data)
# print(data1)
# # print('直接取JSON中的值',data1['name']) # 不能这样取，会报错
# print(type(data1))
#
# pprint.pprint(data)
#
# # 将已编码的 JSON 字符串解码为 Python 对象
# data2 = json.loads(data1)
# print(type(data2))
# print(data2)
#
# siteid = 10000
# email = "henry@comm100.com"
# request_body = {"m": [{"d": 600, "a":str(siteid), "b": ":0:50-51-53-55-57-59:::True", "c": "7.6:" + email}],
#                 "s": ""}
# request_body2 = {"m": [{"d": 600, "a":siteid, "b": ":0:50-51-53-55-57-59:::True", "c": "7.6:" + email}],
#                 "s": ""}
# print(request_body)
# print(request_body2)
#
# res = {"c":0,"e":"","o":[{"a":600,"b":0,"c":0,"d":"qq6OyhpKAUmciTdS3VOPvw","g":"0","e":{"a":{"a":"67160eed-ab26-4e25-984b-df1863d7e31e","b":"mj livechat3","c":"","d":True,"e":"e7a9f37c-964b-4572-bf42-51a838771048","f":50,"g":True,"h":"bb7e0bb1-dce8-4559-ab41-a51e567859a2","i":50,"j":True,"k":"baa96e2c-2090-43f1-9b46-4e3a1338fe17","l":50,"m":True,"n":"7c1ae822-c480-4cdc-8424-eab0766e0cc1","o":50,"p":True,"q":"a8a60e34-4e02-4f68-9e8c-d07067b690a0","r":50,"s":True,"t":"daa7b295-fded-48c8-85bc-17803b376491","u":50,"v":True,"w":"81c037ab-9a56-40b2-a550-71d0ca112935","x":50,"z":False,"aa":True,"ab":False,"ac":"Dear {!Visitor.Name}, thank you for contacting us! How may I help you?","ad":False,"ae":False,"af":False,"ag":False,"ah":[{"a":1,"b":True,"c":30,"d":""},{"a":29,"b":True,"c":320,"d":""},{"a":18,"b":True,"c":100,"d":""},{"a":10,"b":True,"c":250,"d":""},{"a":12,"b":True,"c":320,"d":""},{"a":7,"b":True,"c":100,"d":""},{"a":9,"b":True,"c":100,"d":""},{"a":8,"b":False,"c":100,"d":""},{"a":5,"b":False,"c":100,"d":""},{"a":6,"b":False,"c":100,"d":""},{"a":13,"b":False,"c":100,"d":""},{"a":14,"b":False,"c":100,"d":""},{"a":17,"b":False,"c":250,"d":""},{"a":15,"b":False,"c":200,"d":""},{"a":16,"b":False,"c":100,"d":""},{"a":19,"b":False,"c":100,"d":""},{"a":11,"b":False,"c":200,"d":""},{"a":20,"b":False,"c":100,"d":""},{"a":21,"b":False,"c":100,"d":""},{"a":22,"b":False,"c":100,"d":""},{"a":23,"b":False,"c":100,"d":""},{"a":24,"b":False,"c":100,"d":""},{"a":25,"b":False,"c":100,"d":""},{"a":26,"b":False,"c":100,"d":""},{"a":27,"b":False,"c":100,"d":""}],"ai":"China Standard Time","aj":0,"ak":False,"al":False,"am":"mj@livechat3.com","an":96438565348,"ao":False,"ap":True,"aq":True,"ar":True,"at":True,"au":True,"av":True,"aw":"yyyy/MM/dd HH:mm:ss","ax":True,"ay":0,"ba":False,"bb":True,"bc":True,"bd":True,"be":True,"bf":0,"bg":0,"bh":1,"bi":"{\"a\":[17,69],\"b\":[17,82],\"c\":False,\"d\":5,\"e\":[17,70],\"f\":False,\"g\":False,\"h\":15,\"i\":True,\"j\":True,\"k\":True,\"l\":1,\"m\":True,\"aa\":True,\"ab\":\"2249e11d-1b74-418d-b913-e08e76e9df19\",\"ac\":50,\"ad\":True,\"cfs\":\"[]\",\"avii\":\"2d27341e-fa48-4b7a-a799-fbe2f7447f42\",\"aviv\":50,\"avip\":True,\"avis\":True,\"avei\":\"d6befd77-ca2e-41c3-9c5d-df323eb6df2a\",\"avev\":50,\"avep\":True,\"aves\":True,\"rcsi\":\"2d27341e-fa48-4b7a-a799-fbe2f7447f42\",\"rcsv\":50,\"rcp\":True,\"rcs\":True,\"cesi\":\"d6befd77-ca2e-41c3-9c5d-df323eb6df2a\",\"cesv\":50,\"cep\":True,\"ces\":True,\"to\":[\"sys_info\",\"sys_contact\",\"sys_wrapup\",\"sys_helpContent\",\"c_dc10420c-3f90-4fc7-9682-059665e6633e\",\"sys_history\",\"sys_nav\",\"c_5cbabc6e-fbf7-4522-9f95-faf042ca2718\"],\"sssi\":\"75db986b-ea61-489f-bb66-cf28b5463b91\",\"sssv\":50,\"ssp\":True,\"sss\":True,\"sesi\":\"8bdf5f84-7d86-4e51-9f68-57b118427bd5\",\"sesv\":50,\"sep\":True,\"ses\":True,\"lcat\":False}","bj":-480.0,"bk":False,"bl":20,"bm":False,"bn":"","bo":"","bq":False,"br":"ffe43fd5-dce9-4d48-a038-82e50b9050d7","bs":50,"bt":False,"bu":False,"isAutoSendMessageWhenAgentNotReplyInXMinutes":False,"minutesForAutoSendMessageWhenAgentNotReply":8,"messageForAutoSendMessageWhenAgentNotReply":"Sorry for keeping you waiting. I'll be with you soon. Appreciate your patience.","isAutoSendMessageWhenVisitorNotReplyInXMinutes":False,"minutesForAutoSendMessageWhenVisitorNotReply":8,"messageForAutoSendMessageWhenVisitorNotReply":"Are you still there with me?","apikey":"2ee3dfac9f90468ab40e28e8edca6a07","botPermission":16383,"adminPermission":104857398,"glanceUserId":"ACewj61VL0ClCT2HAuXCQ","ifAcceptAllocation":True,"versionOffset":{"Guid":"cc65ad4f-71fe-4097-b69d-ec91b7ef4faa","OffSet":0},"loginTime":1690376381753,"lastStatusChangedTime":1690376381753,"ifNotificationIncomingAudioVideoChat":True,"ifNotificationAudioVideoChatEnded":True,"skills":[],"isSuperAgent":False},"l":{"a":10008,"b":True,"c":False,"d":False,"e":True,"f":True,"g":True,"h":False,"i":True,"j":False,"k":True,"l":True,"m":False,"n":False,"o":True,"p":True,"q":True,"r":True,"s":True,"t":True,"u":True,"v":True,"w":True,"x":20,"y":10,"z":False,"aa":True,"ab":True,"ac":True,"ad":True,"ae":True,"af":True,"ag":True,"ah":True,"ai":"https://pciformidc.testing.comm100dev.io","aj":True,"ak":2,"al":"https://livechat3api.testing.comm100dev.io/api/kb","am":"https://livechat3dash.testing.comm100dev.io/kb","an":"https://livechat3api.testing.comm100dev.io/bot","shopifyAppApiUrl":"https://livechat3dash.testing.comm100dev.io/ShopifyApp","company":"cc","ifEnableSegmentation":True,"ifTurnOffNotificationsInHoldQueue":False,"ifDisplaySalesforceAccountInfo":False,"ifDisplaySalesforceContactInfo":False,"ifEnableSFIntegration":False,"ifTurnOffPopupInHoldQueue":False,"ifEnableCustomFilter":True,"ifEnableAutoAllocation":False,"ifEnableAdvancedCategoryMode":False,"ifEnableAudioVideoChat":True,"ifShowBuyNow":True,"ifAllowManuallyAcceptChats":True,"ifEnableSocial":False,"socialAPIUrl":"https://livechat3api.testing.comm100dev.io/socialapi","socialVersion":"1.1.2","ifEnableTicket":True,"ticketAPIUrl":"https://livechat3api.testing.comm100dev.io","ticketVersion":"1.0.13","signalRServerUrl":"https://livechat3dash.testing.comm100dev.io/acpns","globalAPIUrl":"https://livechat3api.testing.comm100dev.io","ifEnableExtensions":True,"ifEnableCobrowse":True,"ifEnableBot":True,"ifEnableTaskBot":True,"ifEnableAgentAssist":False,"ifEnableLiveChatNote":True,"ifEnableSMS":True,"ifEnableLinkCannedMessages":True,"fileServiceAddress":"https://livechat3file.testing.comm100dev.io/fileservice/v1","fileServiceStandbyAddress":"https://livechat3filestandby.testing.comm100dev.io/fileservice/v1","encoding":"base64","ifEnableShift":True,"ifEnableRestrictedWords":False,"ifEnableKB":True,"ifEnableLiveChatTab":True,"serverInstanceTag":"Production-6660a05caa904754b4147d7497174d18","ifEnableCustomViews":True,"ifEnableCustomTags":True,"ifEnableBatchEdit":True,"ifEnableMergeTickets":True,"ifEnableBlockSenders":True,"ifEnableMention":True,"ifEnableAddInternalNote":True,"ifEnableSignature":True,"ifEnableCustomFieldsForMessaging":True,"hostExternalUrl":"commonserviceidc.testing.comm100dev.io","ifEnableVisitorSSO":True,"ifEnableAudioVideoChatRecording":False,"recordingServerUrl":"http://google.com","partnerId":"100002","ifEnableDynamics365Integration":True,"ifEnableVendasta":False,"vendastcenterUrl":"https://livechat3center.testing.comm100dev.io","ifPaid":"Paid","planName":"Co-browsing; Comm100 Queue; Platinum; Gold; Booking; ","profitCenter":"SMB &amp; APAC ENT","ifEnableLogout":False,"ifEnableOutreach":False},"isVisitorLanguageDetermined":False,"siteId":0,"ifCustomizedAway":False}}],"siteId":10008}
#
# agent_session_id = res['o'][0]['d']
# version_offset_guid = res['o'][0]['e']['a']['versionOffset']['Guid']
#
# request_body_logout = {"m": [{"d": 101, "e": 0}], "s": agent_session_id, "l": [],
#                        "operatorOffset": {"Guid": version_offset_guid, "OffSet": 0}}
#
# print(request_body_logout)
res= [
    {
        "type": "batchAction",
        "payload": [
            {
                "type": "checkBan"
            },
            {
                "type": "newVisitor",
                "payload": {
                    "visitorGuid": "cf491e35-887b-4851-92fc-64a1ec67e870",
                    "sessionId": "8da923a6-c57c-43c2-a1d1-aead39e91865",
                    "ifNewVisitor": True,
                    "ifMigrated": False
                }
            },
            {
                "type": "setCustomVariables"
            },
            {
                "type": "pageVisit",
                "payload": {
                    "sessionId": "8da923a6-c57c-43c2-a1d1-aead39e91865",
                    "page": {
                        "title": "",
                        "url": ""
                    },
                    "time": 1690459653396
                }
            },
            {
                "type": "getChatButton",
                "payload": {
                    "color": "#329FD9",
                    "adaptiveButtonRightOffset": 0,
                    "adaptiveButtonBottomOffset": 0,
                    "adaptiveButtonRightOffsetOnMobile": 0,
                    "adaptiveButtonBottomOffsetOnMobile": 0,
                    "isCustomizedAdaptiveButtonUsed": False,
                    "customizedAdaptiveButtonIcon": "/DBResource/DBImage.ashx?campaignId=a29bc45c-826d-4b0b-9e40-eb6571a16dac&imgType=6&ver=5A98FDDF&siteId=10008",
                    "id": "a29bc45c-826d-4b0b-9e40-eb6571a16dac",
                    "type": "adaptive",
                    "isHideOffline": False,
                    "iframeStyle": {
                        "width": 460.0,
                        "height": 620.0
                    },
                    "isEmbeddedWindow": True,
                    "lastUpdateTime": "5A98FDDF",
                    "routeDepartment": "00000001-0000-0000-0000-000000000001",
                    "windowStyle": "classic"
                }
            },
            {
                "type": "checkIfOnline",
                "payload": {
                    "campaignId": "a29bc45c-826d-4b0b-9e40-eb6571a16dac",
                    "ifOnline": False
                }
            },
            {
                "type": "checkManualInvitation"
            },
            {
                "type": "checkAutoInvitation",
                "payload": []
            },
            {
                "type": "getSSORecoverInfo"
            }
        ]
    }
]

print(res[0])
print(res[0]['payload'][1])
print(res[0]['payload'][1]['payload']['ifNewVisitor'])
