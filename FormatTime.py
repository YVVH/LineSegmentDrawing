from datetime import datetime


def get_time():
    # 获取当前时间
    now = datetime.now()

    # 按照指定格式输出时间
    formatted_now = now.strftime("%Y_%m_%d_%H_%M_%S")
    return formatted_now