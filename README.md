# Turtle
### Install:
`cd mmdetection`

`pip install torchvision`

`pip install mmcv-full`

`pip install -r requirements/build.txt`

`pip install -v -e .`

### Convert the images to coco dataset format first

### Train:
`python tools/train.py own_configs/r50.py --no-validate`

### Inference and generate json result (other format please reference mmdetection official tutorial):
`python tools/test.py own_configs/r50.py best_model.pth --format-only --eval-options "jsonfile_prefix=xxx"`
#### The `inference.py` is for visualization.
### All the parameters, including IoU thres, confident thres, you can tune it in the `own_configs/r50.py` `( test_cfg )`

### Dataset:
#### Check `data/make_dataset` to convert the raw images to coco format for inference (get the boxes)
#### First using `image2csv.py` to generate a csv file with fake boxes. (mmdetection read coco format as default, so we can make a random labeled coco format test json, this csv file is a middle procedure.)
#### Then use the `csv2coco.py` to generate the fake test json. You only need to modify the `classname_to_id` at the top, and the `path` at the bottom of the script.
#### If you want to make a training set and a validation set, use the `csv2coco_train_val.py`, the real labeled csv file is required.
#### The scripts may occur type error depending on the image names, it won't be hard to fix.