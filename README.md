Gerador de Vídeo a partir de Imagens

Este projeto em Python utiliza a biblioteca OpenCV para criar um vídeo a partir de imagens armazenadas em uma pasta. A ideia é pegar os arquivos de imagem (em formatos como .jpg, .png, .gif, etc.) e organizá-los em sequência para gerar um vídeo final (.mp4).

🚀 Objetivo

O objetivo é demonstrar o uso de manipulação de arquivos com os e processamento de imagens/vídeos com cv2, criando um vídeo automático a partir de imagens.

📂 Estrutura do Projeto
├── Desenhos/        # Pasta que contém as imagens
├── video2.mp4       # Arquivo de saída (gerado após execução)
└── main.py          # Script principal

⚙️ Pré-requisitos
Antes de rodar o projeto, certifique-se de ter instalado:
Python 3.x
OpenCV

Instale as dependências com:
pip install opencv-python

▶️ Como executar
Coloque suas imagens na pasta 
Execute o script principal:
python main.py

O vídeo gerado será salvo como video2.mp4 no diretório atual.

🖼️ Formatos aceitos
O programa reconhece automaticamente imagens com extensões:
.gif
.png
.jpg
.jpeg
.jfif

📝 Observações
O vídeo é criado em 5 FPS por padrão (pode ser alterado na linha VideoWriter).
A ordem das imagens é invertida (nasce do sol → da última para a primeira).
Caso nenhuma imagem seja encontrada, o programa exibirá 0 como contagem.
