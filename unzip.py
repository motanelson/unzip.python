#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
descompacta_zip_gui.py — Interface gráfica para escolher um ficheiro ZIP e extrair tudo no diretório atual.
"""

import zipfile
import os
import tkinter as tk
from tkinter import filedialog, messagebox


def escolher_zip():
    """Abre diálogo gráfico para escolher o ficheiro ZIP."""
    return filedialog.askopenfilename(
        title="Selecione um ficheiro ZIP",
        filetypes=[("Ficheiros ZIP", "*.zip"), ("Todos os ficheiros", "*.*")]
    )


def descompactar_zip(zip_path):
    """Extrai o conteúdo do ZIP no diretório atual."""
    with zipfile.ZipFile(zip_path, 'r') as z:
        z.extractall()
    return z.namelist()


def main():
    root = tk.Tk()
    root.withdraw()  # oculta a janela principal

    zip_path = escolher_zip()
    if not zip_path:
        print("Operação cancelada. Nenhum ficheiro ZIP selecionado.")
        return

    try:
        ficheiros = descompactar_zip(zip_path)
        messagebox.showinfo("Sucesso", f"{len(ficheiros)} ficheiros extraídos para:\n{os.getcwd()}")
    except Exception as e:
        messagebox.showerror("Erro", f"Falha ao descompactar:\n{e}")

print("\033c\033[43;30m\n\select zip file?\n")
if __name__ == "__main__":
    main()

