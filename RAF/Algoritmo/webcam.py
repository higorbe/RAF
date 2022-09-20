import numpy as np
import face_recognition as fr
import cv2
import os
import time
from engine import get_rostos

rostos_cadastrados, nomes_dos_rostos = get_rostos()

video_capture = cv2.VideoCapture(0)

while True: # Inicia um loop infinito
    sucesso, frame = video_capture.read()

    cores_em_rgb = frame[:, :, ::-1]

    localizacao_dos_rostos = fr.face_locations(cores_em_rgb)
    rosto_desconhecidos = fr.face_encodings(cores_em_rgb, localizacao_dos_rostos)

    for (top, right, bottom, left), rosto_desconhecido in zip(localizacao_dos_rostos, rosto_desconhecidos):
        resultados = fr.compare_faces(rostos_cadastrados, rosto_desconhecido)
    
        print('===================== TABELA DOS RESULTADOS ====================') 
        print('     E o seu resultado foi:',  resultados) # O comando print exibe no terminal tudo ou qualquer letra, número e simbolos que estiver dentro das aspas. E neste caso retorna os resultados (true ou false)
        print('================================================================')

        time.sleep (3) # Faz com que a TABELA DOS RESULTADOS espere por 3 segundos para exibir a proxima   
        
        face_distances = fr.face_distance(rostos_cadastrados, rosto_desconhecido)
        distancia_da_face = np.argmin(face_distances)

        if resultados[distancia_da_face]: # Procura pela melhor distância  
            nome = nomes_dos_rostos[distancia_da_face] # Compara os nomes dos rostos cadastrados
        else:
            nome = "Desconhecido" # E se não estiver entre os rostos cadastrados ele exibira na tela "Desconhecido".
        
        # Está etapa gera um quadrado ao redor do seu rosto, desde altura, largura, intensidade entre outros. 
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 0), 3)

        # Está é a etapa onde é gerado um segundo espaço "quadrado", onde ficam alocadas as letras; que pode ser vista logo abaixo.
        cv2.rectangle(frame, (left, bottom -35), (right, bottom), (0, 0, 0), cv2.FILLED)
        font = cv2.FONT_HERSHEY_SIMPLEX

        # Aqui é onde são geradas as letras, strings, palavras, textos, desde de tamanho a formatos.
        cv2.putText(frame, nome, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        # Está etapa abre uma aba, com o nome que definimos entre o (''), e também retorna o frame.
        cv2.imshow('Webcam', frame)

        # Aqui é o comando que quando a tecla 'Q' for clicada o loop será encerrado.  
    if cv2.waitKey(1) & 0xFF == ord('q'):
        os.system('cls') # Após esperar os 3 segundos, este comando limpara todo o terminal 
        break
    cv2.imwrite("./Fotos/Foto.jpg", frame) # Este comando tira uma "fotógrafia" e direciona para a pasta Fotos.

video_capture.release()
cv2.destroyAllWindows()