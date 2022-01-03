FROM nvidia/cuda:11.1.1-cudnn8-devel-ubuntu18.04
RUN : "essential" && \
    apt update -y && \
    apt upgrade -y && \
    apt install sudo apt-utils vim git -y && \
    : "japanese setting for os" && \
    apt-get install -y language-pack-ja-base language-pack-ja && \
    : "japanese setting for jupyter" && \
    sudo apt-get install -y fonts-ipaexfont && \
    : "python" && \
    apt install python3.7 python3.7-dev python3-pip python3.7-venv -y && \
    python3.7 -m pip install -U pip && \
    : "required by mecab-python3, Tensorflow etc." && \
    apt install swig -y && \
    python3.7 -m pip install wheel && \
    python3.7 -m pip install -U setuptools && \
    python3.7 -m pip install -U six
ENV LANG=ja_JP.UTF-8
COPY ./requirements.txt /var/requirements.txt
RUN : "Default kernel" && \
    pip install -U pip && \
    pip install torch==1.8.1+cu111 torchvision==0.9.1+cu111 torchaudio==0.8.1 -f https://download.pytorch.org/whl/torch_stable.html
RUN pip install -r /var/requirements.txt
RUN : "create dir" && \
    mkdir -p /data/
