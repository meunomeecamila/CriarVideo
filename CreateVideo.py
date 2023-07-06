#sistema operacional (listdir)
import os
#ler as imagens e criar o video
import cv2

path = "Desenhos"
images = []

#verificar cada arquivo do path (pasta de imagens)
for file in os.listdir(path):
    #separar o nome e a extensão do video
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)
               
        #colocar file name dentro da matriz vazia (images)
        images.append(file_name)
        
print(len(images))
count = len(images)

frame = cv2.imread(images[0])
height,width,channels = frame.shape
size = (width,height)
print(size)

#Compactar o video e determinar a extensão do vídeo
#5 -> FPS
out = cv2.VideoWriter("video2.mp4",cv2.VideoWriter_fourcc(*"DIVX"),5,size)

#Nascer do Sol
#Começa pela última imagem - diminuindo -1
for i in range(count-1,0,-1):
    frame = cv2.imread(images[i])
    out.write(frame)

#fechar o vídeo
out.release()
print("Concluído!")