# whisper_use
 a repository for using whisper

 
## 如何安装
#### FFmpeg安装
在使用这个软件前，我们需要先安装一个叫做FFmpeg的软件，linux用户可以直接运行`sudo pacman -S ffmpeg`或者`sudo apt update && sudo apt install ffmpeg`安装，但是windows用户需要手动设置下环境变量，下面是教程链接
https://blog.csdn.net/Natsuago/article/details/143231558

#### whisper_use包安装
```
pip install git+https://github.com/escapistmost/whisper_use.git
```
or
```
git clone https://github.com/escapistmost/whisper_use.git
cd whisper_use
pip install .
```

## 使用示例

``` python
import whisper_use
print(whisper_use.detect_text('audio1.m4a'))
print(whisper_use.detect_language('audio1.m4a'))
print(whisper_use.detect_text_from_mel('audio1.m4a'))
```
注：这里的音频文件可以是MP3等任意类型，你可以自己随意录音进行展示

## 注意事项
这个库会自动下载模型到你运行这个代码的位置的models文件夹中（没有这个文件夹它也会自动创建一个），但是大家可能会遇到没有魔法（翻不了墙，下半天结果网络错误），位置存储不够等问题，下面是对应的解决方法：

下面是这个模型的链接，你需要自己去把这个文件下载下来并解压到对应的地址，然后使用函数的时候增加一个参数（下面是个例子）：
https://pan.baidu.com/s/1Q1jaVxvxbN0u4CJY4uJ_lg?pwd=2wgr

```
print(whisper_use.detect_text('audio1.m4a', download_root='./my_model'))
```
上面对应的文件夹相对格式是这样的：

    main.py  ——你运行文件时的相对路径
    my_model ——文件夹
        large-v3-turbo.pt ——模型文件