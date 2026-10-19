# samuel-sm64-launcher

Um launcher simples em Python para rodar Super Mario 64 no Windows em tela cheia, sem precisar abrir interface de emulador ou configurar nada manualmente.

## 🕹️ Como Jogar

1. Vá na seção de [Releases](../../releases) ao lado.
2. Baixe o executável da versão mais recente (`run.exe`).
3. Dê dois cliques para jogar. Para fechar o jogo a qualquer momento, aperte **ESC**.

## 🛠️ Como Funciona

O script em Python (`run.py`) utiliza as bibliotecas nativas `subprocess` e `os` para disparar o motor do Mupen64Plus em segundo plano, ocultando a janela do terminal (`CREATE_NO_WINDOW`) e carregando a ROM direto em tela cheia. 

O projeto foi empacotado em um único arquivo `.exe` utilizando o **PyInstaller**.

## 💻 Como Compilar Localmente

Se quiser clonar o projeto e gerar o executável na sua máquina:

1. Clone o repositório:
```bash
git clone https://github.com/Stuartti/samuel-sm64-launcher.git
cd samuel-sm64-launcher
```

2. Coloque os arquivos do Mupen64Plus e a ROM renomeada para `mario.z64` dentro da pasta `bin/`.

3. Instale o PyInstaller e compile:
```bash
pip install pyinstaller
pyinstaller --noconsole --onefile --add-data "bin;bin" run.py
```
