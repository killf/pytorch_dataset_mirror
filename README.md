# PyTorch模型、数据集国内镜像

### 一、使用方法

只需要在使用模型或数据集之前导入`torchmirror.dataset`或`torchmirror.model`模块即可，如下：

```python
import torch
import torchvision.datasets.mnist as mnist
from torchmirror import dataset, model

train_dataset = mnist.MNIST("./data", train=True, download=True)
test_dataset = mnist.MNIST("./data", train=False, download=True)
```

### 二、使用其他镜像

要使用其他镜像，只需要修改`PYTORCH_MODEL_MIRROR`或`PYTORCH_DATASET_MIRROR`环境变量即可，如下：

```bash
export PYTORCH_MODEL_MIRROR=http://192.168.0.100:8080
export PYTORCH_DATASET_MIRROR=http://192.168.0.100:8080
```