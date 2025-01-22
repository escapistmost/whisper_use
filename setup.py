from setuptools import setup, find_packages

setup(
    name='whisper_use',    # import 什么就命名成什么
    version='0.1',    # 版本号
    packages=find_packages(),
    install_requires=[
        'openai-whisper',
    ],    # 把所有需要安装的包都写在这里
    author='escapist',    # 作者
    description='Photometric Stereo Package',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/escapistmost/whisper_use',    # 请修改为自己的github仓库地址
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)