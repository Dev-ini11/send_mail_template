from utility import email, my_password, modify, read_file
from build_html import build_birthday_email
from send import send_birthday_email
import os

def mail():
    content = modify(read_file("data/Birthday_Wish_Template.txt"), "Ini", "Prince")
    html = build_birthday_email(name="Ini", body_text=content, sender_name="Prince")
    send_birthday_email("inioluwaayetoro@gmail.com", "Happy Birthday, Ini! 🎉", html, email, my_password)

mail()