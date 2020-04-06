import os
from os.path import join

BASE_PATH = os.environ.get('PYTORCH_DATASET_MIRROR', 'http://pytorch_dataset_mirror.killf.info')

try:
    import torchvision

    DATA_PATH = join(BASE_PATH, 'torchvision', 'mnist')
    torchvision.datasets.mnist.MNIST.resources = [
        (join(DATA_PATH, 'train-images-idx3-ubyte.gz'), "f68b3c2dcbeaaa9fbdd348bbdeb94873"),
        (join(DATA_PATH, 'train-labels-idx1-ubyte.gz'), "d53e105ee54ea40749a09fcbcd1e9432"),
        (join(DATA_PATH, 't10k-images-idx3-ubyte.gz'), "9fb629c4189551a2d022fa330f9573f3"),
        (join(DATA_PATH, 't10k-labels-idx1-ubyte.gz'), "ec29112dd5afa0611ce80d1b7f02629c")
    ]

    DATA_PATH = join(BASE_PATH, 'torchvision', 'fashion-mnist')
    torchvision.datasets.mnist.FashionMNIST.resources = [
        (join(DATA_PATH, 'train-images-idx3-ubyte.gz'), '8d4fb7e6c68d591d4c3dfef9ec88bf0d'),
        (join(DATA_PATH, 'train-labels-idx1-ubyte.gz'), '25c81989df183df01b3e8a0aad5dffbe'),
        (join(DATA_PATH, 't10k-images-idx3-ubyte.gz'), 'bef4ecab320f06d8554ea6380940ec79'),
        (join(DATA_PATH, 't10k-labels-idx1-ubyte.gz'), 'bb300cfdad3c16e7a12a480ee83cd310')
    ]

    DATA_PATH = join(BASE_PATH, 'torchvision', 'kmnist')
    torchvision.datasets.mnist.KMNIST.resources = [
        (join(DATA_PATH, 'train-images-idx3-ubyte.gz'), 'bdb82020997e1d708af4cf47b453dcf7'),
        (join(DATA_PATH, 'train-labels-idx1-ubyte.gz'), 'e144d726b3acfaa3e44228e80efcd344'),
        (join(DATA_PATH, 't10k-images-idx3-ubyte.gz'), '5c965bf0a639b31b8f53240b1b52f4d7'),
        (join(DATA_PATH, 't10k-labels-idx1-ubyte.gz'), '7320c461ea6c1c855c0b718fb2a4b134')
    ]

    DATA_PATH = join(BASE_PATH, 'torchvision', 'emnist')
    torchvision.datasets.mnist.EMNIST.resources = [
        (join(DATA_PATH, 'train-images-idx3-ubyte.gz'), 'f68b3c2dcbeaaa9fbdd348bbdeb94873'),
        (join(DATA_PATH, 'train-labels-idx1-ubyte.gz'), 'd53e105ee54ea40749a09fcbcd1e9432'),
        (join(DATA_PATH, 't10k-images-idx3-ubyte.gz'), '9fb629c4189551a2d022fa330f9573f3'),
        (join(DATA_PATH, 't10k-labels-idx1-ubyte.gz'), 'ec29112dd5afa0611ce80d1b7f02629c')
    ]

    DATA_PATH = join(BASE_PATH, 'torchvision', 'qmnist')
    torchvision.datasets.mnist.QMNIST.resources = {
        'train': [(join(DATA_PATH, 'qmnist-train-images-idx3-ubyte.gz'), 'ed72d4157d28c017586c42bc6afe6370'),
                  (join(DATA_PATH, 'qmnist-train-labels-idx2-int.gz'), '0058f8dd561b90ffdd0f734c6a30e5e4')],
        'test': [(join(DATA_PATH, 'qmnist-test-images-idx3-ubyte.gz'), '1394631089c404de565df7b7aeaf9412'),
                 (join(DATA_PATH, 'qmnist-test-labels-idx2-int.gz'), '5b5b05890a5e13444e108efe57b788aa')],
        'nist': [(join(DATA_PATH, 'xnist-images-idx3-ubyte.xz'), '7f124b3b8ab81486c9d8c2749c17f834'),
                 (join(DATA_PATH, 'xnist-labels-idx2-int.xz'), '5ed0e788978e45d4a8bd4b7caec3d79d')]
    }

    DATA_PATH = join(BASE_PATH, 'torchvision', 'cifar')
    torchvision.datasets.cifar.CIFAR10.url = join(DATA_PATH, 'cifar-10-python.tar.gz'),
    torchvision.datasets.cifar.CIFAR100.url = join(DATA_PATH, 'cifar-100-python.tar.gz'),

    DATA_PATH = join(BASE_PATH, 'torchvision', 'pascal')
    DATASET_YEAR_DICT = {
        '2012': {
            'url': join(DATA_PATH, 'VOCtrainval_11-May-2012.tar'),
            'filename': 'VOCtrainval_11-May-2012.tar',
            'md5': '6cd6e144f989b92b3379bac3b3de84fd',
            'base_dir': os.path.join('VOCdevkit', 'VOC2012')
        },
        '2011': {
            'url': join(DATA_PATH, 'VOCtrainval_25-May-2011.tar'),
            'filename': 'VOCtrainval_25-May-2011.tar',
            'md5': '6c3384ef61512963050cb5d687e5bf1e',
            'base_dir': os.path.join('TrainVal', 'VOCdevkit', 'VOC2011')
        },
        '2010': {
            'url': join(DATA_PATH, 'VOCtrainval_03-May-2010.tar'),
            'filename': 'VOCtrainval_03-May-2010.tar',
            'md5': 'da459979d0c395079b5c75ee67908abb',
            'base_dir': os.path.join('VOCdevkit', 'VOC2010')
        },
        '2009': {
            'url': join(DATA_PATH, 'VOCtrainval_11-May-2009.tar'),
            'filename': 'VOCtrainval_11-May-2009.tar',
            'md5': '59065e4b188729180974ef6572f6a212',
            'base_dir': os.path.join('VOCdevkit', 'VOC2009')
        },
        '2008': {
            'url': join(DATA_PATH, 'VOCtrainval_14-Jul-2008.tar'),
            'filename': 'VOCtrainval_11-May-2012.tar',
            'md5': '2629fa636546599198acfcfbfcf1904a',
            'base_dir': os.path.join('VOCdevkit', 'VOC2008')
        },
        '2007': {
            'url': join(DATA_PATH, 'VOCtrainval_06-Nov-2007.tar'),
            'filename': 'VOCtrainval_06-Nov-2007.tar',
            'md5': 'c52e279531787c972589f7e41ab4ae64',
            'base_dir': os.path.join('VOCdevkit', 'VOC2007')
        }
    }
except ImportError:
    pass

try:
    import torchtext

    DATA_PATH = join(BASE_PATH, 'torchtext', 'text_classification')
    torchtext.datasets.text_classification.URLS = {
        'AG_NEWS': join(DATA_PATH, 'ag_news_csv.tar.gz'),
        'SogouNews': join(DATA_PATH, 'sogou_news_csv.tar.gz'),
        'DBpedia': join(DATA_PATH, 'dbpedia_csv.tar.gz'),
        'YelpReviewPolarity': join(DATA_PATH, 'yelp_review_polarity_csv.tar.gz'),
        'YelpReviewFull': join(DATA_PATH, 'yelp_review_full_csv.tar.gz'),
        'YahooAnswers': join(DATA_PATH, 'yahoo_answers_csv.tar.gz'),
        'AmazonReviewPolarity': join(DATA_PATH, 'amazon_review_polarity_csv.tar.gz'),
        'AmazonReviewFull': join(DATA_PATH, 'amazon_review_full_csv.tar.gz')
    }
except ImportError:
    pass
