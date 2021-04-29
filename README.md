# Turtle
### Install:
`cd mmdetection`

`pip install torchvision`

`pip install mmcv-full`

`pip install -r requirements/build.txt`

`pip install -v -e .`

###Convert the images to coco dataset format first

### Train:
`python tools/train.py own_configs/r50.py --no-validate`

### Inference and generate json result (other format please reference mmdetection official tutorial):
`python tools/test.py own_configs/r50.py best_model.pth --format-only --eval-options "jsonfile_prefix=xxx"`
#### The `inference.py` is for visualization.
### All the parameters, including IoU thres, confident thres, you can tune it in the `own_configs/r50.py` `( test_cfg )`
