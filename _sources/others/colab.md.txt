# Colab 训练

## 安装 Nightly 构建

因为您将使用 PyTorch 的实验部件，所以建议安装最新版本的 ``torch`` 和 ``torchvision``。您可以找到关于[本地安装的最新说明](https://pytorch.org/get-started/locally/)。例如，在没有 GPU 支持的情况下安装：

```shell
pip install numpy
pip install --pre torch torchvision -f https://download.pytorch.org/whl/nightly/cpu/torch_nightly.html
# 对于 CUDA 支持使用 https://download.pytorch.org/whl/nightly/cu101/torch_nightly.html
```

或者：

```shell
!yes y | pip uninstall torch torchvision
!yes y | pip install --pre torch torchvision -f https://download.pytorch.org/whl/nightly/cu101/torch_nightly.html
```

## 下载数据

```python
import requests
from pathlib import Path
import zipfile


def download(file_name, data_url):
    root = Path('data')
    if not Path(file_name).is_file():
        print("下载数据...")
        root.mkdir(exist_ok=True)
        with requests.get(data_url) as req:
            with open(file_name, 'wb') as f:
                f.write(req.content)
        if 200 <= req.status_code < 300:
            print("下载完成！")
        else:
            print("下载失败！")
    else:
        print(file_name, "已经存在，跳过下载...")

    with zipfile.ZipFile(file_name, 'r') as zip_ref:
        print("解压...")
        zip_ref.extractall('data')


if __name__ == '__main__':
    data_url = 'https://download.pytorch.org/tutorial/hymenoptera_data.zip'
    data_path = Path('data')
    file_name = data_path / 'hymenoptera_data.zip'
    data_path = data_path / 'hymenoptera_data'
    download(file_name, data_url)
```