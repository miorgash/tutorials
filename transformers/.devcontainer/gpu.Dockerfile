FROM nvidia/cuda:11.3.1-cudnn8-devel-ubuntu20.04
RUN : "essential" && \
    apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install sudo apt-utils vim git -y && \
    : "japanese setting for os" && \
    apt-get install -y language-pack-ja-base language-pack-ja && \
    : "japanese setting for jupyter" && \
    apt-get install -y fonts-ipaexfont
ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Asia
RUN : "python" && \
    apt-get install python3.9 python3.9-venv python3-pip -y && \
    python3.9 -m pip install -U pip && \
    : "required by mecab-python3, Tensorflow etc." && \
    apt install swig -y && \
    python3.9 -m pip install wheel && \
    python3.9 -m pip install -U setuptools && \
    python3.9 -m pip install -U six
ENV LANG=ja_JP.UTF-8
RUN : "tutorial requirements" : && \
    python3.9 -m pip install transformers[sentencepiece] && \
    python3.9 -m pip install torch==1.10.1+cu113 torchvision==0.11.2+cu113 torchaudio==0.10.1+cu113 -f https://download.pytorch.org/whl/cu113/torch_stable.html
COPY ./requirements.txt /var/requirements.txt
WORKDIR /var
RUN : "required for cl-tohoku/bert-base-japanese-v2" && \
    python3.9 -m pip install -r ./requirements.txt
