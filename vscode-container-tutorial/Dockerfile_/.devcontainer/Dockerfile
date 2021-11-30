FROM mcr.microsoft.com/vscode/devcontainers/typescript-node:0-12
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get install git -y
RUN apt-get install tree -y
# -> tree works