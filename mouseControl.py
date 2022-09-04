import cv2 as cv # importando opencv
import numpy as np # importando numpy
import pyautogui as gui # importando pyautogui
gui.FAILSAFE = False # desabilitando o limite de borda da lib

camera = cv.VideoCapture(0, cv.CAP_DSHOW)                           # captura de vídeo da câmera selecionada

camW = camera.get(cv.CAP_PROP_FRAME_WIDTH)                          # variável que recebe a largura da câmera
camH = camera.get(cv.CAP_PROP_FRAME_HEIGHT)                         # variável que recebe a altura da câmera
monitorW, monitorH = gui.size()                                     # variáveis que recebem largura e altura, respectivamente, da resolução do monitor 
    
# função para transformar as coordenadas do ponteiro dentro da resolução da câmera para a resolução do monitor
def returnTrueCoordinates(camW, camH, monitorW, monitorH, x, y):

    pixelTotalCam = camW * camH                                     # variável que recebe o total de pixels na resolução da câmera
    pixelTotalMonitor = monitorW * monitorH                         # variável que recebe o total de pixels na resolução do monitor

    trueX = (x * pixelTotalMonitor) // pixelTotalCam                # valor da coordenada x na resolução do monitor
    trueY = (y * pixelTotalMonitor) // pixelTotalCam                # valor da coordenada y na resolução do monitor

    coordinate = (trueX, trueY)                                     # tupla das coordenadas reais
    return coordinate

# algoritmo para processamento da imagem e obtenção de informações para interações com o mouse
aberto = True
while aberto:

    _, frame = camera.read()                                        # capturando o frame através do dispositivo de imagem
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)                      # convertendo a cor do frame de rgb(bgr) para hsv

    # captura da cor do objeto azul para movimentar o ponteiro do mouse
    lowerBlue = np.array([102, 74, 112])                            # cor hsv azul obtida
    upperBlue = np.array([130, 255, 255])                           # limite da cor hsv azul obtida
    maskBlue = cv.inRange(hsv, lowerBlue, upperBlue)                # cria a máscara para capturar somente a cor na imagem/video

    # captura da cor do objeto verde para clicar com o ponteiro do mouse
    lowerGreen = np.array([51, 104, 160])                           # cor hsv verde obtida
    upperGreen = np.array([80, 255, 255])                           # limite da cor hsv verde obtida
    maskGreen = cv.inRange(hsv, lowerGreen, upperGreen)             # cria a máscara para capturar somente a cor na imagem/video

    lowerYellow = np.array([17, 82, 130])                           # cor hsv amarela obtida
    upperYellow = np.array([30, 255, 255])                           # limite da cor hsv amarelo obtida
    maskYellow = cv.inRange(hsv, lowerYellow, upperYellow)          # cria a máscara para capturar somente a cor na imagem/video

    # captura da cor do objeto vermelho para fechar o programa
    lowerRed = np.array([144, 102, 192])                            # cor hsv avermelho obtida
    upperRed = np.array([225, 255, 255])                            # limite da cor hsv vermelho obtida
    maskRed = cv.inRange(hsv, lowerRed, upperRed)                   # cria a máscara para capturar somente a cor na imagem/video

    # resultado Azul
    resultBlue = cv.bitwise_and(frame, frame, mask=maskBlue)        # detecta o objeto azul frame por frame utilizando a máscara criada

    # resultado Verde
    resultGreen = cv.bitwise_and(frame, frame, mask=maskGreen)      # detecta o objeto verde frame por frame utilizando a máscara criada

    # resultado Amarelo
    resultYellow = cv.bitwise_and(frame, frame, mask=maskYellow)    # detecta o objeto verde frame por frame utilizando a máscara criada

    # resultado Vermelho
    resultRed = cv.bitwise_and(frame, frame, mask=maskRed)          # detecta o objeto vermelho frame por frame utilizando a máscara criada

    # encontra os contornos do objeto com a cor específica para melhor identificação
    contours, _ = cv.findContours(maskBlue, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    # laço percorre o valor de contorno do objeto 
    for _, contour in enumerate(contours):
        area = cv.contourArea(contour)                              # área do objeto
        if area > 800:
            x, y, w, h = cv.boundingRect(contour)                   # coordenadas do objeto

            # função para transformar as coordenadas dentro da resolução da câmera para a resolução do monitor
            x, y = returnTrueCoordinates(camW, camH, monitorW, monitorH, x, y)

            print(x, y)                                             # coordenadas no terminal
            gui.moveTo(x, y)                                        # move o ponteiro do mouse para as coordenadas no monitor

    # encontra os contornos do objeto com a cor específica para melhor identificação
    contours, _ = cv.findContours(maskGreen, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    # laço percorre o valor de contorno do objeto 
    for _, contour in enumerate(contours):
        area = cv.contourArea(contour)                              # área do objeto
        if area > 800:
            x, y, w, h = cv.boundingRect(contour)                   # coordenadas do objeto
            gui.click(button='left')                                # clica no botão esquerdo do mouse

    # encontra os contornos do objeto com a cor específica para melhor identificação
    contours, _ = cv.findContours(maskYellow, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    # laço percorre o valor de contorno do objeto 
    for _, contour in enumerate(contours):
        area = cv.contourArea(contour)                              # área do objeto
        if area > 800:
            x, y, w, h = cv.boundingRect(contour)                   # coordenadas do objeto
            gui.click(button='right')                               # clica no botão direito do mouse

    # encontra os contornos do objeto com a cor específica para melhor identificação
    contours, _ = cv.findContours(maskRed, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    # laço percorre o valor de contorno do objeto 
    for _, contour in enumerate(contours):
        area = cv.contourArea(contour)                              # área do objeto
        if area > 800:
            x, y, w, h = cv.boundingRect(contour)                   # coordenadas do objeto
            aberto = False                                               # fecha o programa

    cv.imshow("result", frame)                                      # janela para exibição da câmera

    k = cv.waitKey(60)
    if k == 27:                                                     # tecla ESCAPE para interromper o programa
        break

# fecha as janelas/programa
camera.release()
cv.destroyAllWindows()
