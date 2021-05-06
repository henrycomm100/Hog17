FROM python:3.9-alpine
LABEL author="Henry.MJ"

#工作路径设定为 /code
WORKDIR /code

# 创建环境变量给Flask使用
ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0


# 复制 app.py 到容器内 /code目录
COPY app.py /code

# 安装gcc工具，python的依赖
RUN pip install flask && pip install redis

# 映射端口, 要注意EXPOSE和 docker run -p <宿主端口>:<容器端口> 区分开来
EXPOSE 5000

# The STOPSIGNAL instruction sets the system call signal that will be sent to the container to exit.
STOPSIGNAL SIGTERM

# 为容器设置默认启动命令
CMD ["flask", "run"]

