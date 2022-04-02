from fastapi import FastAPI, Request
from linebot import WebhookParser
from linebot.models import TextMessage
from aiolinebot import AioLineBotApi

# APIクライアントとパーサをインスタンス化
line_api = AioLineBotApi(channel_access_token="a5tveNiyNC16ld7eMr5hEm2lBv1uvgzZYhjwmO+oXroeJP6STfY3kYSZ18DaSAT4lJngFKrdjmC4VX/bE0JSZLANv8GNeR23bkhEhjBH6jjb2Af7BjY0XGbeiTwMFY5vCknG3sWvuFChMo3njyGNKwdB04t89/1O/w1cDnyilFU=")
parser = WebhookParser(channel_secret="855b9868cfb09f73aa4959f49757ecca")

app = FastAPI()

@app.post("/messaging_api/handle_request")
async def handle_request(request: Request):
    # リクエストをパースしてイベントを取得(署名検証あり)
    events = parser.parse(
        (await request.body()).decode('utf-8'),
        request.hander.get('X-Line_signature', '')
    )

    # 各イベントを処理
    for ev in events:
        await line_api.reply_message_async(
            ev.reply_token,
            TextMessage(text=f'You said: {ev.message.text}')
        )
    
    return "ok"