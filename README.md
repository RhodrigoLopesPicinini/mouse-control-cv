# Controle de mouse utilizando Computer Vision
## Descrição
Algoritmo criado para interagir com ações simples do mouse, através da câmera e objetos de cores: azul, verde e vermelho. Para o desenvolvimento foi utilizado a linguagem Python e as libraries: opencv, numpy e pyautogui.

## Libraries
> - [OpenCV](https://github.com/opencv/opencv.git)
> - [Numpy](https://github.com/numpy/numpy.git)
> - [Pyautogui](https://github.com/asweigart/pyautogui.git)

## Instalação

Foi utilizado Python na versão 3.9.10
> [Python 3.9.10](https://www.python.org/downloads/)

Clonar o repositório para diretório remoto
> ```sh
> git clone https://github.com/RhodrigoLopesPicinini/mouse-control-cv.git
> ```

## Funcionamento

1. Ao executar o código, será necessário uma câmera conectada ao dispositivo que estiver com o programa aberto.
>
2. Será necessário o uso de objetos com as seguintes cores: azul, verde e vermelho. Para a detecção dos objetos através da câmera.
>
3. Cada cor representa uma ação dentro do programa. Lista de funcionamentos de cada cor:
   - Azul - Controla a movimentação do ponteiro de acordo com a posição do objeto na câmera;
   - Verde - Executa o clique do botão esquerdo do mouse;
   - Vermelho - Interrompe o processo de execução do programa.
>
4. Para fechar o programa, basta pressionar a tecla ESCAPE(ESC)

## Desenvolvedor
Rhodrigo Lopes Picinini