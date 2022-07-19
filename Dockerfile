FROM python:3.10-buster

# 如果要阿里源，就用下面这个
# RUN (echo "deb http://mirrors.aliyun.com/debian/ buster main non-free contrib" > /etc/apt/sources.list) 
# 如果要清华源，就用下面这个
RUN (echo "deb https://mirrors.tuna.tsinghua.edu.cn/debian/ buster main contrib non-free" > /etc/apt/sources.list) 
RUN (apt update) && (apt upgrade -y)
# 中文字体
RUN (apt install -y  lsb-release wget ttf-wqy-zenhei xfonts-intl-chinese wqy*)
# 解决僵尸进程
RUN (apt install -y  tini) 

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

ENTRYPOINT ["/usr/bin/tini", "--"]