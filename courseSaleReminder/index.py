import requests
from bs4 import BeautifulSoup
from datetime import datetime
import utils

def process_course(course_id):
    # 函数接收课程ID作为输入，然后爬取并处理该课程的相关信息
    url = f'https://coding.imooc.com/class/{course_id}.html'

    headers = {
     'User-Agent': 'Mozilla/5.0 (Windows NT10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    # 获取学习人数
    learners_num_elem = soup.find('span', text='学习人数')
    if learners_num_elem is not None:
        learners_num = int(learners_num_elem.find_next_sibling('span').text.strip())
    else:
        learners_num = '未找到学习人数'

    # 获取课程名称
    name_elem = soup.find('div', class_='title-box')
    if name_elem is not None:
        name = name_elem.find('h1').text.strip()
    else:
        name = '未找到名称'

    # 获取课程价格
    price_elem = soup.find('div', class_='sale-price')
    if price_elem is not None:
        price = int(utils.extract_number(price_elem.text.strip()))
    else:
        price = 0

    # 构建课程信息字典
    course_info = {
        'id': course_id,
        'learners_num': learners_num,
        'name': name,
        'price': price,
        'update': 0,
    }

    return course_info

# 设置要处理的课程ID列表
course_ids = [643, 645, 646]
courses_info = []
email_needed = False

# 遍历课程ID列表，处理每个课程
for course_id in course_ids:
    course_info = process_course(course_id)
    today = datetime.now().date()

    # 从文件中读取已保存的学习人数
    saved_date, saved_learners_num = utils.read_saved_learners_num(course_id)
    courses_info.append(course_info)
    # 如果当天已经记录过，更新学习人数
    if saved_date is not None and saved_date == today: 
        if saved_learners_num != course_info['learners_num']:
            utils.update_learners_num(course_id, today, course_info['learners_num'], course_info['name'])
            course_info['update'] = course_info['learners_num'] - saved_learners_num
            email_needed = True
    # 如果当天没有记录，新增一行
    else:
        utils.save_learners_num(course_id, today, course_info['learners_num'], course_info['name'])
        email_needed = True

# 如果至少有一个课程的学习人数发生了变化，则发送电子邮件
if email_needed: 
   email_body = utils.create_email_body(courses_info)
   utils.send_mail(email_body)
