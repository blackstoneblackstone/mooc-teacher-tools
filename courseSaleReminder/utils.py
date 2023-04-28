import smtplib
import re
import env
from email.mime.text import MIMEText
from email.utils import formataddr
from datetime import datetime


def extract_number(string):
    number = re.findall(r'\d+\.?\d*', string)
    if number:
        return float(number[0])
    else:
        return None

def read_saved_learners_num(course_id):
    try:
        with open("/opt/task/mooc-task/daily_learners_num.txt", "r") as f:
            data = f.readlines()
            for line in data:
                saved_course_id, date_str, learners_num = line.strip().split(',')
                if int(saved_course_id) == course_id:
                    return datetime.strptime(date_str, '%Y-%m-%d').date(), int(learners_num)
    except FileNotFoundError:
        return None, None
    return None, None

def save_learners_num(course_id, date, learners_num, name):
    with open("/opt/task/mooc-task/daily_learners_num.txt", "a") as f:
        f.write(f"{course_id},{date.strftime('%Y-%m-%d')},{learners_num},{name}\n")

def send_mail(learners_num):
    smtp_server = 'smtp.sina.com'
    smtp_port = 465

    from_addr = env.get()['from_addr']
    password = env.get()['password']

    to_addr = env.get()['to_addr']

    msg = MIMEText(f'{learners_num}', 'plain', 'utf-8')
    msg['From'] = formataddr(('慕课网课程通知', from_addr))
    msg['To'] = formataddr(('你', to_addr))
    msg['Subject'] = '学习人数通知'

    try:
        server = smtplib.SMTP_SSL(smtp_server, smtp_port)
        server.login(from_addr, password)
        server.sendmail(from_addr, [to_addr], msg.as_string())
        server.quit()
        print('邮件发送成功')
    except Exception as e:
        print('邮件发送失败')
        print(e)

def read_saved_learners_num(course_id):
    try:
        with open("/opt/task/mooc-task/daily_learners_num.txt", "r") as f:
            data = f.readlines()
            for line in data:
                saved_course_id, date_str, learners_num, name = line.strip().split(',')
                if int(saved_course_id) == course_id and datetime.strptime(date_str, '%Y-%m-%d').date() == datetime.now().date():
                    return datetime.strptime(date_str, '%Y-%m-%d').date(), int(learners_num)
    except FileNotFoundError:
        return None, None
    return None, None

def save_learners_num(course_id, date, learners_num, name):
    with open("/opt/task/mooc-task/daily_learners_num.txt", "a") as f:
        f.write(f"{course_id},{date.strftime('%Y-%m-%d')},{learners_num},{name}\n")

def create_email_body(courses_info):
    email_body = "课程信息:\n\n"
    for course_info in courses_info:
        update_status = "" if course_info['update'] == 0 else f"有更新 + {course_info['update']}"
        email_body += f"课程ID：{course_info['id']}\n"
        email_body += f"课程名：{course_info['name']}\n"
        email_body += f"学习人数：{course_info['learners_num']}  {update_status}\n"
        email_body += f"总收益：{format((course_info['learners_num']) * course_info['price'], ',')}\n"
        email_body += '-------------------\n'
    return email_body


def update_learners_num(course_id, today, learners_num, name):
    with open("/opt/task/mooc-task/daily_learners_num.txt", "r") as f:
        lines = f.readlines()

    # 检查是否已存在当天的记录
    exist = False
    for i, line in enumerate(lines):
        cols = line.strip().split(",")
        if cols[0] == str(course_id) and cols[1] == str(today):
            exist = True
            lines[i] = f"{course_id},{today},{learners_num},{name}\n"

    # 如果不存在，则添加一行新的记录
    if not exist:
        lines.append(f"{course_id},{today},{learners_num},{name}\n")

    with open("/opt/task/mooc-task/daily_learners_num.txt", "w") as f:
        f.writelines(lines)