import json, csv, cv2

json_f = open('xxx.bbox.json', 'r')
f = json.load(json_f)
img_path = 'data/IMAGES_1024/'
res = csv.writer(open('submission.csv', 'w'))
res.writerow(['Image_ID', 'x', 'y', 'w', 'h'])
for i in f:
    img = cv2.imread(img_path + i['image_id'] + '.JPG')
    print(img.shape)
    W = img.shape[1]
    H = img.shape[0]
    x1 = i['bbox'][0] / W
    y1 = i['bbox'][1] / H
    w = i['bbox'][2] / W
    h = i['bbox'][3] / H
    res.writerow([i['image_id'], x1, y1, w, h])