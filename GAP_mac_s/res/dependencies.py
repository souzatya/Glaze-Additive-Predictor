import os
import shutil

def res_path(relative_path):
    if (os.getcwd().__contains__("Resources")):
        base_path = os.getcwd()
    else:
        base_path = os.path.abspath("./res")

    return os.path.join(base_path, relative_path)

def check():
    if os.path.exists(os.path.join(os.path.expanduser('~'), 'Documents', 'com.soujatya_sarkar.gap')) == False:
        os.mkdir(os.path.join(os.path.expanduser('~'),'Documents','com.soujatya_sarkar.gap'))

    if os.path.exists(os.path.join(os.path.expanduser('~'),'Documents','com.soujatya_sarkar.gap', 'icon.ico')) == False:
        shutil.copy(res_path("icon.ico"),os.path.join(os.path.expanduser('~'),'Documents','com.soujatya_sarkar.gap'))

    if os.path.exists(os.path.join(os.path.expanduser('~'),'Documents','com.soujatya_sarkar.gap', 'logo.png')) == False:
        shutil.copy(res_path("logo.png"),os.path.join(os.path.expanduser('~'),'Documents','com.soujatya_sarkar.gap'))

    if os.path.exists(os.path.join(os.path.expanduser('~'),'Documents','com.soujatya_sarkar.gap', 'GLAZE_DATASET.xlsx')) == False:
        shutil.copy(res_path("GLAZE_DATASET.xlsx"),os.path.join(os.path.expanduser('~'),'Documents','com.soujatya_sarkar.gap'))