# 🎬 Gerador de Vídeo a partir de Imagens

Este projeto em Python utiliza a biblioteca OpenCV para criar um vídeo a partir de imagens armazenadas em uma pasta.
A ideia é pegar arquivos de imagem (em formatos como .jpg, .png, .gif, etc.) e organizá-los em sequência para gerar um vídeo final (.mp4).

---

## 🎯 Objetivo

O objetivo é demonstrar o uso de:
Manipulação de arquivos com os
Processamento de imagens/vídeos com cv2

---

## Pré-requisitos
Antes de rodar o projeto, certifique-se de ter instalado:
* Python 3.x
* OpenCV

Instale as dependências com:
pip install opencv-python

---

## ▶️ Como executar
- Coloque suas imagens na pasta
- Execute o script principal: python main.py

O vídeo gerado será salvo como video2.mp4 no diretório atual.

## Formatos aceitos
O programa reconhece automaticamente imagens com extensões:
.gif
.png
.jpg
.jpeg
.jfif

## Observações
* O vídeo é criado em 5 FPS por padrão (pode ser alterado na linha VideoWriter).
* A ordem das imagens é invertida (da última para a primeira).
* Caso nenhuma imagem seja encontrada, o programa exibirá 0 como contagem.
