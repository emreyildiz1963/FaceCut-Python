from facedetection import facedetect
import cv2



for i in range(1834):
    img_path = "./dataset/with_mask/0 ({0}).jpg".format(i+1)
    img = facedetect(img_path)
    x = "{0}".format(type(img))
    if x != "<class 'NoneType'>":
        status = cv2.imwrite("./dataset/maskeli/0 ({0}).jpg".format(i+1), img)
        print(i, ". Foto Bitti")

print("Basariyla tamamlandi")
