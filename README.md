### docker_vitis Ai

文件夹里面是安装docker和拉取Vitis Ai gpu版本的脚本
拉取之后运行命令（docker run -it --gpus all --name {name} -v {本地文件夹}Vitis-AI:/workspace fmannan/vitis-ai-gpu:2.5 /bin/bash）启动vitis Ai环境

### KV260

文件夹里面是配置xilinxkv260开发板的流程，包括Ubuntu22.04TLS镜像、烧录镜像、安装pynq。

### SESR

文件夹中放的是SESR超分辨模型已经安装所需包的脚本。

### main

文件夹中包含server文件、Single-Client文件、Doble-Client文件，其中server文件用于与无人机通信，Single-Client文件用于控制无人机飞行与图像显示，Doble-Client文件用于对SR效果进行对比。.txt文件中记录了我们对tello库的更改。

