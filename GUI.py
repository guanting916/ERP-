import os  # 引入 os 模組
import tkinter as tk  # 引入 tkinter 模組


#Path_Golden_ERP = ""
#Path_Star_ERP = ""


def Golden_ERP():
    os.system("start C:\Datawin\GoldenTop\EXE\erp2014.exe")  # 執行Start_ERP


def Star_ERP():
    os.system("start C:\STARERP\RemoteClient\starerp1t.exe")  # 執行ERP


'''
def createNewWindow():
    Path_setting = tk.Toplevel(window)
    Path_setting.title('設定ERP路徑')
    window_width = 450  # 視窗寬度
    window_height = 75  # 視窗高度
    Path_setting.resizable(False, False)
    left = int((screen_width - window_width)/2)       # 計算左上 x 座標
    top = int((screen_height - window_height)/2)      # 計算左上 y 座標
    Path_setting.geometry(
        f'{window_width}x{window_height}+{left}+{top}')  # 設定視窗大小、位置
    Path_setting_Golden_ERP = tk.Label(Path_setting)
    Path_setting_Golden_ERP.config(text='Golden ERP路徑：')
    Path_setting_Golden_ERP.grid(column=0, row=0)
    Path_setting_Star_ERP = tk.Label(Path_setting)
    Path_setting_Star_ERP.config(text='Star ERP路徑：')
    Path_setting_Star_ERP.grid(column=0, row=1)
    Path_in_Golden_ERP = tk.Entry(Path_setting)
    Path_in_Golden_ERP.config(width=30)  # 放入單行輸入框
    Path_in_Golden_ERP.grid(column=1, row=0)
    Path_in_Star_ERP = tk.Entry(Path_setting)
    Path_in_Star_ERP.config(width=30)  # 放入單行輸入框DF
    Path_in_Star_ERP.grid(column=1, row=1)
    Path_setting_Confirm = tk.Button(Path_setting)
    Path_setting_Confirm.config(text="確認",
                                command=Path_setting.destroy)
    Path_setting_Confirm.grid(column=0, row=3)
'''


window = tk.Tk() # 建立主視窗
'''
menubar = tk.Menu(window)              # 建立主選單
menubar.add_command(label="設定路徑", command=createNewWindow)    # 主選單項目&事件
'''

window.title('ERP選單') # 設定視窗標題
window.configure(  # menu=menubar,
    background='#9D9D9D')   # 設定背景色黑色
screen_width = window.winfo_screenwidth()    # 取得螢幕寬度
screen_height = window.winfo_screenheight()  # 取得螢幕高度

window_width = 720  # 視窗寬度
window_height = 480  # 視窗高度
window.resizable(False, False)
left = int((screen_width - window_width)/2)       # 計算左上 x 座標
top = int((screen_height - window_height)/2)      # 計算左上 y 座標
window.geometry(f'{window_width}x{window_height}+{left}+{top}')  # 設定視窗大小、位置

button_width = 20  # 按鈕寬度
button_height = 5  # 按鈕高度
print(window.winfo_reqwidth())
button_x_place = int((window.winfo_reqwidth()-button_width)/2)
# 建立按鈕
button_ERP = tk.Button(window)  # 按鈕所在視窗
button_ERP.config(
    font=10,  # 文字大小
    text='Golden ERP',  # 顯示文字
    width=button_width,  # 設定按鈕寬度
    height=button_height,  # 設定按鈕高度
    command=Golden_ERP)  # 按下按鈕所執行的函數

button_ERP.place(x=button_x_place,  # 設定按鈕x位置
                 rely=0.2)  # 設定按鈕y位置

button_ERPII = tk.Button(window)  # 按鈕所在視窗
button_ERPII.config(
    font=10,  # 文字大小
    text='Star ERP',  # 顯示文字
    width=button_width,  # 設定按鈕寬度
    height=button_height,  # 設定按鈕高度
    command=Star_ERP)  # 按下按鈕所執行的函數

button_ERPII.place(x=button_x_place,  # 設定按鈕x位置
                   rely=0.55)  # 設定按鈕y位置

# 執行主程式
window.mainloop()
