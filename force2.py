import os

file_list = os.listdir('C:/Users/Seo/Desktop/hand_label')
print(file_list)


for i in file_list:
    a = os.path.join('C:/Users/Seo/Desktop/hand_label', i)
    b = os.path.join('C:/Users/Seo/Desktop/hand_label', i[:-4])
    os.rename(a, b)

