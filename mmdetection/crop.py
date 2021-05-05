import cv2
import os
import json

img_path = './img/'
with open('xxx.bbox.json', 'r') as f:
    json_f = json.load(f)
img_list = os.listdir(img_path)
print(len(img_list))
for fname in img_list:
    n = 0
    img = cv2.imread(img_path + fname)
    print(img_path + fname)
    for ann in json_f:
        if ann['image_id'] + '.jpg' == fname and ann['score'] > 0.3:
            n += 1
            # print(fname)
            x1, y1 = int(ann['bbox'][0]), int(ann['bbox'][1])
            x2, y2 = int(ann['bbox'][2]), int(ann['bbox'][3])
            # Draw bboxes
            # cv2.rectangle(img, (int(x1),int(y1),int(x2),int(y2)), (0, 0, 255), 2)
            # Add texts
            # text = str(ann['category'])
            # cv2.putText(img, text, (int(x1), int(y1 - 1)), 2, 2, (0, 0, 255), 1)
            
            cv2.imwrite('res/%s_croped_%s' % (n,fname), img[y1:y1+y2, x1:x1+x2])
