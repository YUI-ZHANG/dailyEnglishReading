import smtplib
from email.mime.text import MIMEText
from google import genai
import datetime
import os


client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# 取得今天的日期
today = datetime.date.today()
today_str = today.strftime("%Y-%m-%d")

response = client.models.generate_content(
    model="gemini-2.5-flash", contents=f"你是英文多益考試教學專家，今天是 {today_str}。請給我一個跟昨天不一樣、各種不同主題、每天花三分鐘練習的簡短閱讀，包含翻譯和重點單字以及文法，不需要練習技巧。"
)
print(response.text)
title =f"每日學英文閱讀 - {today_str}"

my_mail = os.getenv("MY_EMAIL")
gmail_token = os.getenv("GMAIL_TOKEN")


msg = MIMEText(response.text)
msg["Subject"] = title
msg["From"] = my_mail
msg["To"] = my_mail

smtp = smtplib.SMTP("smtp.gmail.com",587)
smtp.ehlo()
smtp.starttls()
smtp.login(my_mail,gmail_token)
smtp.send_message(msg)
smtp.quit()