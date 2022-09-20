import face_recognition as fr # Quando o (as) está sendo utilizado é na maioria dos casos uma maneira de abreviar o nome da bliblioteca, variavel ou função 

def reconhece_face(url_foto): #url da foto já é auto explicativo é o nome que foi dado para a imagem
    foto = fr.load_image_file(url_foto)
    rostos = fr.face_encodings(foto)
    if(len(rostos) > 0):
        return True, rostos
    
    return False, []

def get_rostos(): # São todas as faces e nomes salvos, lembrando get_rostos não é uma bliblioteca é apenas o nome da função que foi criada
    rostos_cadastrados = []
    nomes_dos_rostos = []

    rosto_1 = reconhece_face("./Imagens/whillian.jpg") # Aqui fica o caminho de onde o arquivo engine puxará as imagens 
    if(rosto_1[0]):
        rostos_cadastrados.append(rosto_1[1][0])
        nomes_dos_rostos.append("Whillian")

    rosto_2 = reconhece_face("./Imagens/higor.jpg")
    if(rosto_2[0]):
        rostos_cadastrados.append(rosto_2[1][0])
        nomes_dos_rostos.append("Higor")

    rosto_3 = reconhece_face("./Imagens/reis.jpg")
    if(rosto_3[0]):
        rostos_cadastrados.append(rosto_3[1][0])
        nomes_dos_rostos.append("Reis")

    rosto_4 = reconhece_face("./Imagens/barsotti.jpg")
    if(rosto_4[0]):
        rostos_cadastrados.append(rosto_4[1][0])
        nomes_dos_rostos.append("Barsotti")

    rosto_5 = reconhece_face("./Imagens/isabella.jpg")
    if(rosto_5[0]):
        rostos_cadastrados.append(rosto_5[1][0])
        nomes_dos_rostos.append("Isabela")
    
    return rostos_cadastrados, nomes_dos_rostos