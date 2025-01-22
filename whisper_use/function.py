import whisper
import torch

def detect_text(file_path, download_root='./models', model_name='turbo'):
    """
    从音频中解析文本
    :param file_path: 音频文件路径
    :param download_root: 模型下载路径
    :param model_name: 模型名称
    :return:文本内容，str
    """
    model = whisper.load_model(model_name, download_root=download_root)
    result = model.transcribe(file_path)
    return result["text"]


def detect_language(file_path, download_root='./models', model_name='turbo'):
    """
    从Mel 频谱图中解析音频语言类型
    :param file_path: 音频文件路径
    :param download_root: 模型下载路径
    :param model_name: 模型名称
    :return:检测出的语言类型
    """
    model = whisper.load_model(model_name, download_root=download_root)
    audio = whisper.load_audio(file_path)
    audio = whisper.pad_or_trim(audio)
    mel = whisper.log_mel_spectrogram(audio, n_mels=model.dims.n_mels).to(model.device)
    _, probs = model.detect_language(mel)
    return max(probs, key=probs.get)


def detect_text_from_mel(file_path=None, download_root='./models', model_name='turbo', mel=None):
    """
    从Mel 频谱图中解析音频文本
    :param file_path: 音频文件路径
    :param download_root: 模型下载路径
    :param model_name: 模型名称
    :param mel:  Mel 频谱图，提供者就不去读文件路径了
    :param device: 模型运行在什么设备上
    :return:文本内容，str
    """
    model = whisper.load_model(model_name, download_root=download_root)
    if file_path is None and mel is None:
        raise ValueError("文件和mel频谱图总得有一个")
    if mel is None:
        audio = whisper.load_audio(file_path)
        audio = whisper.pad_or_trim(audio)
        mel = whisper.log_mel_spectrogram(audio, n_mels=model.dims.n_mels).to(model.device)
    options = whisper.DecodingOptions()
    result = whisper.decode(model, mel, options)
    return result.text

