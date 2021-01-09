# FaceCut-Python

--------------------------------

ImageSave.py dosyanının içinden fotoğraflarımızın bulunduğu klasörü ve kayıt klasörünü ayarlıyoruz.

Ne kadar fotoğrafımız varsa bir eksiğini for döngüsüne yazıyoruz.

Fotoğraflarımızın bulunduğu klasöre girip ctrl+a yapıp yeniden adlandır deyip '0' a basıp kaydediyoruz.

-------------------------------
FaceDetection kütüphanesini

```
from facedetection import facedetect

IMAGE_PATH = "FOTOĞRAFIMIZIN DOSYA YOLU"

face_image = facedetect(IMAGE_PATH)

```

şeklinde kendi projemize import edebiliriz.

