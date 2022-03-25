import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import face_recognition
fnt=ImageFont.truetype('MR ROBOT.ttf',50)
f=pd.read_csv('./List/Employee.csv')
print(f.to_string())
empno=f["Employee ID"].tolist()
name=f["Name"].tolist()
filename=f["File Name"].tolist()
n=len(empno)
emp=[]
emp_encod=[]
uk=face_recognition.load_image_file('./Images/tony1.jpg')
uk_encod=face_recognition.face_encodings(uk)[0]
for i in range(n):
    emp.append(face_recognition.load_image_file(filename[i]))
    emp_encod.append(face_recognition.face_encodings(emp[i])[0])
found=face_recognition.compare_faces(emp_encod,uk_encod, tolerance=0.5)
print(found)
for i in range(n):
    if found[i]:
        print(emp[i].shape)
        print(emp[i].shape[0])
        left=100
        bottom=emp[i].shape[0]
        pil_uk=Image.fromarray(uk)
        draw=ImageDraw.Draw(pil_uk)
        draw.text((left,bottom-50), name[i], font=fnt, fill=(255,0,0))
        pil_uk.show()
