import subprocess
import sys
import os


def main():
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))

    bin_path = os.path.join(base_path, "bin")


    emulador = os.path.join(bin_path, "mario_engine.exe")
    rom = os.path.join(bin_path, "mario.z64")

    comando = [emulador, "--fullscreen", rom]

    subprocess.run(comando, cwd=bin_path, creationflags=subprocess.CREATE_NO_WINDOW)

if __name__ == '__main__':
    main()