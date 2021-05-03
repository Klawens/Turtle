import os, csv


f = open('test.csv', 'w', newline='')
images = os.listdir('YOUR IMAGES PATH/')
csv_writer = csv.writer(f)

for i in images:
    # print(i)
    name = os.path.splitext(i)[0]
    csv_writer.writerow([name, 1, 1, 1, 1, "turtle_head"])
    print(name)

f.close()