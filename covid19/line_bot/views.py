from django.shortcuts import render

# Create your views here.
from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextSendMessage

from line_bot.models import *

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)
from line_bot import views
from linebot.models.send_messages import ImageSendMessage

#nlp
#-*- coding:utf-8 -*-
import nltk
import jieba.analyse

import re 

a="發燒"
b="咳嗽"
c="鼻塞"
d="流鼻水"
e="疲勞"
f="全身無力"
g="肌肉痠痛"
h="頭痛"

@csrf_exempt
def callback(request):
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')

        try:
            events = parser.parse(body, signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        
        
         
        for event in events:
            # if isinstance(event, MessageEvent):
            #     if event.message.text == '嗨':
            #         mtext = a
            #         #print('b')
            #     # mtext=event.message.text
            #     message=[]
            #     message.append(TextSendMessage(text=mtext))
            #     line_bot_api.reply_message(event.reply_token,message)
           
            if isinstance(event, MessageEvent):

                # if event.message.text == '確診sop':
                #     message=[]
                #     message.append(TextSendMessage(text = '目前還沒有此功能¯\_(ツ)_/¯'))
                #     line_bot_api.reply_message(event.reply_token,message)
                
                if event.message.text == '確診sop':
                    image_message = ImageSendMessage(
                    original_content_url='https://www.cdc.gov.tw/assets/Covid19/images/0817%E5%BF%AB%E7%AF%A9%E9%99%BD%E6%80%A7%E7%A2%BA%E8%A8%BA.png',
                    preview_image_url='https://www.cdc.gov.tw/assets/Covid19/images/0817%E5%BF%AB%E7%AF%A9%E9%99%BD%E6%80%A7%E7%A2%BA%E8%A8%BA.png'
                    )
                    line_bot_api.reply_message(event.reply_token, image_message)
                
                elif event.message.text == '聊天':
                    message=[]
                    message.append(TextSendMessage(text = '目前還沒有此功能¯\_(ツ)_/¯'))
                    line_bot_api.reply_message(event.reply_token,message)

                #症狀
                elif event.message.text == '症狀':
                    message=[]
                    message.append(TextSendMessage(text = '請問你有出現下列何種症狀?'))
                    message.append(TextSendMessage(text = '發燒=5\n咳嗽=5\n鼻塞=3\n流鼻水=3\n疲勞=1\n全身無力=1\n肌肉痠痛=1\n頭痛=1\n(將以上症狀所得分數加總)    \n(0-20,請不要輸超過!)  '))
                    line_bot_api.reply_message(event.reply_token,message)

                if event.message.text=='0':
                    message=[]
                    message.append(TextSendMessage(text='確診機率極低'))
                    line_bot_api.reply_message(event.reply_token,message)
                elif event.message.text=='1':
                    message=[]
                    message.append(TextSendMessage(text='確診機率極低'))
                    line_bot_api.reply_message(event.reply_token,message)
                elif event.message.text=='2':
                    message=[]
                    message.append(TextSendMessage(text='確診機率極低'))
                    line_bot_api.reply_message(event.reply_token,message)
                elif event.message.text=='3':
                    message=[]
                    message.append(TextSendMessage(text='確診機率極低'))
                    line_bot_api.reply_message(event.reply_token,message)
                elif event.message.text=='4':
                    message=[]
                    message.append(TextSendMessage(text='確診機率極低'))
                    line_bot_api.reply_message(event.reply_token,message)
                elif event.message.text=='5':
                    message=[]
                    message.append(TextSendMessage(text='確診機率較低'))
                    line_bot_api.reply_message(event.reply_token,message)
                elif event.message.text=='6':
                    message=[]
                    message.append(TextSendMessage(text='確診機率較低'))
                    line_bot_api.reply_message(event.reply_token,message)
                elif event.message.text=='7':
                    message=[]
                    message.append(TextSendMessage(text='確診機率較低'))
                    line_bot_api.reply_message(event.reply_token,message)
                elif event.message.text=='8':
                    message=[]
                    message.append(TextSendMessage(text='確診機率較低'))
                    line_bot_api.reply_message(event.reply_token,message)
                elif event.message.text=='9':
                    message=[]
                    message.append(TextSendMessage(text='確診機率較低'))
                    line_bot_api.reply_message(event.reply_token,message)
                elif event.message.text=='10':
                    message=[]
                    message.append(TextSendMessage(text='確診機率較高'))
                    line_bot_api.reply_message(event.reply_token,message)
                elif event.message.text=='11':
                    message=[]
                    message.append(TextSendMessage(text='確診機率較高'))
                    line_bot_api.reply_message(event.reply_token,message)
                elif event.message.text=='12':
                    message=[]
                    message.append(TextSendMessage(text='確診機率較高'))
                    line_bot_api.reply_message(event.reply_token,message)
                elif event.message.text=='13':
                    message=[]
                    message.append(TextSendMessage(text='確診機率較高'))
                    line_bot_api.reply_message(event.reply_token,message)
                elif event.message.text=='14':
                    message=[]
                    message.append(TextSendMessage(text='確診機率較高'))
                    line_bot_api.reply_message(event.reply_token,message)
                elif event.message.text=='15':
                    message=[]
                    message.append(TextSendMessage(text='確診機率極高'))
                    line_bot_api.reply_message(event.reply_token,message)
                elif event.message.text=='16':
                    message=[]
                    message.append(TextSendMessage(text='確診機率極高'))
                    line_bot_api.reply_message(event.reply_token,message)
                elif event.message.text=='17':
                    message=[]
                    message.append(TextSendMessage(text='確診機率極高'))
                    line_bot_api.reply_message(event.reply_token,message)
                elif event.message.text=='18':
                    message=[]
                    message.append(TextSendMessage(text='確診機率極高'))
                    line_bot_api.reply_message(event.reply_token,message)
                elif event.message.text=='19':
                    message=[]
                    message.append(TextSendMessage(text='確診機率極高'))
                    line_bot_api.reply_message(event.reply_token,message)
                elif event.message.text=='20':
                    message=[]
                    message.append(TextSendMessage(text='確診機率極高'))
                    line_bot_api.reply_message(event.reply_token,message)               
                
                #解決問題
                elif event.message.text == '解答疑問':
                    message=[]
                    message.append(TextSendMessage(text='請問你是想詢問哪方面的問題呢'))
                    message.append(TextSendMessage(text='A.思維遲緩\nB.何種情況必須緊急就醫\nC.可以使用何種藥物緩解情況     \nD.請假之政府規定'))
                    line_bot_api.reply_message(event.reply_token,message) 
                elif event.message.text == 'A':
                    message=[]
                    message.append(TextSendMessage(text='\t7招改善腦霧\n1.睡眠充足\n2.多喝水\n3.健康飲食\nTip:鮭魚、沙丁魚、秋刀魚有豐富的Omega 3。另外堅果也都含有能抗發炎的好油脂\n維生素C:維生素C也是能抗氧化的營養素,且能維持免疫力,柑橘類水果、蔬菜、奇異果、莓果類等等都能減緩記憶力衰退、注意力不集中等問題\n益生菌:香港中文大學的研究發現,染疫後腸道菌相會失衡,導致腦霧、疲憊等等後遺症,因此痊癒後補充益生菌,吃蔬果和全穀類食物等益生元對腦霧也有幫助\n咖啡、茶類:兩者都含有咖啡因,能使注意力集中、振作精神,同時他們也有豐富的抗氧化物質,例如綠原酸\n不過要注意,每天咖啡因攝取量不能超過300毫克,大約等於超商大杯冰美式咖啡\n4.規律運動\n5.多參與社交活動\n6.多做有益身心的運動\n7.避免酒精和抽菸'))
                    line_bot_api.reply_message(event.reply_token,message)
                elif event.message.text == 'B':
                    message=[]
                    message.append(TextSendMessage(text='出現以下情況請盡快就醫\n1.氣喘或呼吸困難\n2.持續胸痛、胸悶\n3.意識不清\n4.皮膚、或嘴唇、或指甲床發青\n5.無發燒 (體溫 < 38℃)之情形下,心跳 > 100次/分鐘\n6.無法進食、喝水或服藥\n7.過去24小時無尿或尿量顯著減少'))
                    line_bot_api.reply_message(event.reply_token,message)
                elif event.message.text == 'C':
                    message=[]
                    message.append(TextSendMessage(text='1.消炎止痛藥 \n\t如:普拿疼(成人一次一錠(500毫克),兒童使用含普拿疼之藥水依體重建議劑量服用,每四到六小時服用一次),可緩解發燒、頭痛、牙齒痛、經痛、肌肉痠痛、關節痛\n2.抗過敏藥物:\n\t舒緩打噴嚏、流鼻水、眼鼻皮膚過敏。常見嗜睡、頭暈口乾等副作用;年長者使用要預防跌倒發生。新一代的抗組織胺則改善了嗜睡、疲倦、注意力下降等副作用\n3.腸胃藥物:\n\t如:胃藥、止瀉藥\n\t可舒緩腹痛、腹瀉。腹瀉個案請補充水分和電解質,可以使用運動飲料加入開水稀釋,以及稀飯,土司,香蕉等清淡飲食\n4.止咳藥物:\n\t減緩咳嗽症狀、袪痰'))
                    line_bot_api.reply_message(event.reply_token,message)  
                elif event.message.text == 'D':
                    message=[]
                    message.append(TextSendMessage(text='由於勞工需配合衛生主管機關「居家隔離」、「居家檢疫」、「集中隔離」或「集中檢疫」之要求,不得外出,如因此無法出勤,依嚴重特殊傳染性肺炎防治及紓困振興特別條例第3條第3項規定,勞工得請「防疫隔離假」,雇主應給假,且不得視為曠工、強迫勞工以事假或其他假別處理,亦不得扣發全勤獎金、解僱或為其他不利之處分\n勞工配合防疫措施而無法出勤工作,因為不可歸責於勞工,特別條例明定雇主不得有不利的對待,但因「防疫隔離假」也不可歸責於雇主,所以並未強制雇主應給付薪資\n若雇主不依特別條例規定給予防疫隔離假或對請防疫隔離假勞工有不利對待者,將處新臺幣5萬元以上100萬元以下罰鍰。'))
                    line_bot_api.reply_message(event.reply_token,message) 
                elif event.message.text > '20':
                    message=[]
                    message.append(TextSendMessage(text='你輸超出數量囉 若是加錯 建議前往\n<解決問題>尋求幫助\n(思維遲緩區)'))
                    line_bot_api.reply_message(event.reply_token,message)              

        return HttpResponse()
    else:
        return HttpResponseBadRequest()
        
# @csrf_exempt
# def callback(request):
#     if request.method == 'POST':

#         message = []
#         FollowEvent = []
#         UnfollowEvent = []
#         PostbackEvent = []

#         signature = request.META['HTTP_X_LINE_SIGNATURE']
#         body = request.body.decode('utf-8')

#         message.append(TextSendMessage(text=str(body)))

#         try:
#             events = parser.parse(body, signature)
#         except InvalidSignatureError:
#             return HttpResponseForbidden()
#         except LineBotApiError:
#             return HttpResponseBadRequest()

#         for event in events:
#             #如果事件為訊息 
#             if isinstance(event, MessageEvent):
#                 print(event.message.type)
#                 if event.message.type=='text':
#                     # message.append(TextSendMessage(text='文字訊息'))
#                     # line_bot_api.reply_message(event.reply_token,message)
#                     message = TextSendMessage(text='你想問甚麼')
#                     line_bot_api.reply_message(event.reply_token,message)

#                 elif event.message.type=='image':
#                     message.append(TextSendMessage(text='圖片訊息'))
#                     line_bot_api.reply_message(event.reply_token,message)

#                 elif event.message.type=='location':
#                     message.append(TextSendMessage(text='位置訊息'))
#                     line_bot_api.reply_message(event.reply_token,message)

#                 elif event.message.type=='video':
#                     message.append(TextSendMessage(text='影片訊息'))
#                     line_bot_api.reply_message(event.reply_token,message)


#                 elif event.message.type=='sticker':
#                     message.append(TextSendMessage(text='貼圖訊息'))
#                     line_bot_api.reply_message(event.reply_token,message)

#                 elif event.message.type=='audio':
#                     message.append(TextSendMessage(text='聲音訊息'))
#                     line_bot_api.reply_message(event.reply_token,message)

#                 elif event.message.type=='file':
#                     message.append(TextSendMessage(text='檔案訊息'))
#                     line_bot_api.reply_message(event.reply_token,message)

#             elif isinstance(event, FollowEvent):
#                 print('加入好友')
#                 line_bot_api.reply_message(event.reply_token,message)

#             elif isinstance(event, UnfollowEvent):
#                 print('取消好友')

#             elif isinstance(event, PostbackEvent):
#                 print('PostbackEvent')  
             

#         return HttpResponse()
#     else:
#         return HttpResponseBadRequest()


