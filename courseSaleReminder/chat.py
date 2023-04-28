from flask import Flask, render_template
from collections import defaultdict
from datetime import datetime
import random

app = Flask(__name__)

@app.route('/')
def index():
    with open("/opt/task/mooc-task/daily_learners_num.txt", "r") as f:
        lines = f.readlines()

    data = defaultdict(list)
    for line in lines:
        course_id, date_str, num_str, name = line.strip().split(",", 3)
        date = datetime.strptime(date_str, "%Y-%m-%d").strftime("%m-%d")
        num = int(num_str)
        data[course_id].append((date, num, name))

    def random_color():
        return f"#{random.randint(0, 0xFFFFFF):06x}"

    chart_data = []
    for course_id, course_data in data.items():
        course_data.sort(key=lambda x: x[0])
        dates, nums, names = zip(*course_data)
        chart_data.append({
            "course_id": course_id,
            "dates": dates,
            "nums": nums,
            "name": names[0],
            "color": random_color()
        })

    return render_template("index.html", data=chart_data)

if __name__ == '__main__':
  app.run(debug=True)