FROM python:3.10-buster

RUN (echo "deb http://mirrors.aliyun.com/debian/ buster main non-free contrib" > /etc/apt/sources.list) 
RUN (apt-get update) && (apt-get upgrade)
RUN (apt-get install -y  lsb-release wget ttf-wqy-zenhei xfonts-intl-chinese wqy*) 
# RUN (apt-get install -y  lsb-release)
# RUN (apt-get install -y fonts-liberation libasound2 libatk-bridge2.0-0 libatk1.0-0 libatspi2.0-0 fonts-liberation)

WORKDIR /code
RUN mkdir /code/depends
# 下载并安装 chrome, TIPS: dpkg 不会处理依赖，要使用 apt 安装 deb
RUN (wget -P /code/depends https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb) && ( apt install -y /code/depends/google-chrome-stable_current_amd64.deb)


COPY install.py /code/
RUN python install.py

RUN /usr/local/bin/python -m pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple
COPY requirements-prd.txt /code/
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements-prd.txt
COPY config.yaml /code/
COPY . /code/
