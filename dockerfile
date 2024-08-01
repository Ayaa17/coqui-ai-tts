# 使用官方的 Python 镜像作为基础镜像
FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

# 复制项目文件（如有）
# COPY . .

# 安装系统依赖
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    libsndfile1-dev \
    && rm -rf /var/lib/apt/lists/*

# 安装 Python 包依赖
RUN pip install --upgrade pip
RUN pip install TTS soundfile

# 暴露端口（如有需要）
# EXPOSE 5000

# 设置入口点（如果有需要的脚本）
# ENTRYPOINT ["python", "your_script.py"]

# 或者进入交互式环境
# CMD [ "python3" ]
CMD ["bash"]