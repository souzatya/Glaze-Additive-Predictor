import os
import sys
import shutil

def res_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def check():
    if os.path.exists(os.path.join(os.path.expanduser('~'), 'Documents', 'com.soujatya_sarkar.gap')) == False:
        os.mkdir(os.path.join(os.path.expanduser('~'),'Documents','com.soujatya_sarkar.gap'))

    if os.path.exists(os.path.join(os.path.expanduser('~'),'Documents','com.soujatya_sarkar.gap', 'icon.ico')) == False:
        shutil.copy(res_path("res/icon.ico"),os.path.join(os.path.expanduser('~'),'Documents','com.soujatya_sarkar.gap'))

    if os.path.exists(os.path.join(os.path.expanduser('~'),'Documents','com.soujatya_sarkar.gap', 'logo.png')) == False:
        shutil.copy(res_path("res/logo.png"),os.path.join(os.path.expanduser('~'),'Documents','com.soujatya_sarkar.gap'))

    if os.path.exists(os.path.join(os.path.expanduser('~'),'Documents','com.soujatya_sarkar.gap', 'GLAZE_DATASET.xlsx')) == False:
        shutil.copy(res_path("res/GLAZE_DATASET.xlsx"),os.path.join(os.path.expanduser('~'),'Documents','com.soujatya_sarkar.gap'))