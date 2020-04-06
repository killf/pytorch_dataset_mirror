import os
from os.path import join

BASE_PATH = os.environ.get('PYTORCH_MODEL_MIRROR', 'http://pytorch_mirror.killf.info')

try:
    import torchvision
    import torchvision.models.detection.faster_rcnn
    import torchvision.models.detection.mask_rcnn
    import torchvision.models.detection.keypoint_rcnn

    MODEL_PATH = join(BASE_PATH, 'models')
    torchvision.models.detection.faster_rcnn.model_urls = {
        'fasterrcnn_resnet50_fpn_coco': join(MODEL_PATH, 'fasterrcnn_resnet50_fpn_coco-258fb6c6.pth'),
    }
    torchvision.models.detection.mask_rcnn.model_urls = {
        'maskrcnn_resnet50_fpn_coco': join(MODEL_PATH, 'maskrcnn_resnet50_fpn_coco-bf2d0c1e.pth'),
    }
    torchvision.models.detection.keypoint_rcnn.model_urls = {
        'keypointrcnn_resnet50_fpn_coco_legacy': join(MODEL_PATH, 'keypointrcnn_resnet50_fpn_coco-9f466800.pth'),
        'keypointrcnn_resnet50_fpn_coco': join(MODEL_PATH, 'keypointrcnn_resnet50_fpn_coco-fc266e95.pth'),
    }

    from torchvision.models.alexnet import model_urls as alexnet_model_urls
    from torchvision.models.densenet import model_urls as densenet_model_urls
    from torchvision.models.googlenet import model_urls as googlenet_model_urls
    from torchvision.models.inception import model_urls as inception_model_urls
    from torchvision.models.mnasnet import model_urls as mnasnet_model_urls
    from torchvision.models.mobilenet import model_urls as mobilenet_model_urls
    from torchvision.models.resnet import model_urls as resnet_model_urls
    from torchvision.models.shufflenetv2 import model_urls as shufflenetv2_model_urls
    from torchvision.models.squeezenet import model_urls as squeezenet_model_urls
    from torchvision.models.vgg import model_urls as vgg_model_urls

    alexnet_model_urls["alexnet"] = join(MODEL_PATH, 'alexnet-owt-4df8aa71.pth')

    densenet_model_urls["densenet121"] = join(MODEL_PATH, 'densenet121-a639ec97.pth')
    densenet_model_urls["densenet169"] = join(MODEL_PATH, 'densenet169-b2777c0a.pth')
    densenet_model_urls["densenet201"] = join(MODEL_PATH, 'densenet201-c1103571.pth')
    densenet_model_urls["densenet161"] = join(MODEL_PATH, 'densenet161-8d451a50.pth')

    googlenet_model_urls["googlenet"] = join(MODEL_PATH, 'googlenet-1378be20.pth')

    inception_model_urls["inception_v3_google"] = join(MODEL_PATH, 'inception_v3_google-1a9a5a14.pth')

    mnasnet_model_urls["mnasnet0_5"] = join(MODEL_PATH, 'mnasnet0.5_top1_67.823-3ffadce67e.pth')
    mnasnet_model_urls["mnasnet1_0"] = join(MODEL_PATH, 'mnasnet1.0_top1_73.512-f206786ef8.pth')

    mobilenet_model_urls["mobilenet_v2"] = join(MODEL_PATH, 'mobilenet_v2-b0353104.pth')

    resnet_model_urls["resnet18"] = join(MODEL_PATH, 'resnet18-5c106cde.pth')
    resnet_model_urls["resnet34"] = join(MODEL_PATH, 'resnet34-333f7ec4.pth')
    resnet_model_urls["resnet50"] = join(MODEL_PATH, 'resnet50-19c8e357.pth')
    resnet_model_urls["resnet101"] = join(MODEL_PATH, 'resnet101-5d3b4d8f.pth')
    resnet_model_urls["resnet152"] = join(MODEL_PATH, 'resnet152-b121ed2d.pth')
    resnet_model_urls["resnext50_32x4d"] = join(MODEL_PATH, 'resnext50_32x4d-7cdf4587.pth')
    resnet_model_urls["resnext101_32x8d"] = join(MODEL_PATH, 'resnext101_32x8d-8ba56ff5.pth')
    resnet_model_urls["wide_resnet50_2"] = join(MODEL_PATH, 'wide_resnet50_2-95faca4d.pth')
    resnet_model_urls["wide_resnet101_2"] = join(MODEL_PATH, 'wide_resnet101_2-32ee1156.pth')

    shufflenetv2_model_urls["shufflenetv2_x0.5"] = join(MODEL_PATH, 'shufflenetv2_x0.5-f707e7126e.pth')
    shufflenetv2_model_urls["shufflenetv2_x1.0"] = join(MODEL_PATH, 'shufflenetv2_x1-5666bf0f80.pth')

    squeezenet_model_urls["squeezenet1_0"] = join(MODEL_PATH, 'squeezenet1_0-a815701f.pth')
    squeezenet_model_urls["squeezenet1_1"] = join(MODEL_PATH, 'squeezenet1_1-f364aa15.pth')

    vgg_model_urls["vgg11"] = join(MODEL_PATH, 'vgg11-bbd30ac9.pth')
    vgg_model_urls["vgg13"] = join(MODEL_PATH, 'vgg13-c768596a.pth')
    vgg_model_urls["vgg16"] = join(MODEL_PATH, 'vgg16-397923af.pth')
    vgg_model_urls["vgg19"] = join(MODEL_PATH, 'vgg19-dcbb9e9d.pth')
    vgg_model_urls["vgg11_bn"] = join(MODEL_PATH, 'vgg11_bn-6002323d.pth')
    vgg_model_urls["vgg13_bn"] = join(MODEL_PATH, 'vgg13_bn-abd245e5.pth')
    vgg_model_urls["vgg16_bn"] = join(MODEL_PATH, 'vgg16_bn-6c64b313.pth')
    vgg_model_urls["vgg19_bn"] = join(MODEL_PATH, 'vgg19_bn-c79401a0.pth')

    from torchvision.models.quantization.googlenet import model_urls as googlenet_model_urls
    from torchvision.models.quantization.inception import model_urls as inception_model_urls
    from torchvision.models.quantization.mobilenet import model_urls as mobilenet_model_urls
    from torchvision.models.quantization.resnet import model_urls as resnet_model_urls
    from torchvision.models.quantization.shufflenetv2 import model_urls as shufflenetv2_model_urls

    googlenet_model_urls["googlenet_fbgemm"] = join(MODEL_PATH, 'googlenet_fbgemm-c00238cf.pth')

    inception_model_urls["inception_v3_google_fbgemm"] = join(MODEL_PATH, 'inception_v3_google_fbgemm-4f6e4894.pth')

    mobilenet_model_urls["mobilenet_v2_qnnpack"] = join(MODEL_PATH, 'mobilenet_v2_qnnpack_37f702c5.pth')

    resnet_model_urls["resnet18_fbgemm"] = join(MODEL_PATH, 'resnet18_fbgemm_16fa66dd.pth')
    resnet_model_urls["resnet50_fbgemm"] = join(MODEL_PATH, 'resnet50_fbgemm_bf931d71.pth')
    resnet_model_urls["resnext101_32x8d_fbgemm"] = join(MODEL_PATH, 'resnext101_32x8_fbgemm_09835ccf.pth')

    shufflenetv2_model_urls["shufflenetv2_x1.0_fbgemm"] = join(MODEL_PATH, 'shufflenetv2_x1_fbgemm-db332c57.pth')

    from torchvision.models.segmentation.segmentation import model_urls as segmentation_model_urls

    segmentation_model_urls["fcn_resnet101_coco"] = join(MODEL_PATH, 'fcn_resnet101_coco-7ecb50ca.pth')
    segmentation_model_urls["deeplabv3_resnet101_coco"] = join(MODEL_PATH, 'deeplabv3_resnet101_coco-586e9e4e.pth')

    from torchvision.models.video.resnet import model_urls as resnet_model_urls

    resnet_model_urls["r3d_18"] = join(MODEL_PATH, 'r3d_18-b3b3357e.pth')
    resnet_model_urls["mc3_18"] = join(MODEL_PATH, 'mc3_18-a90a0ba3.pth')
    resnet_model_urls["r2plus1d_18"] = join(MODEL_PATH, 'r2plus1d_18-91a641e6.pth')
except ImportError:
    pass
