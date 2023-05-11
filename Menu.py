import os  # 引入 os 模組
import tkinter as tk  # 引入 tkinter 模組
import pickle  # 引入 pickle 模組


def Golden_ERP():
    # os.system("start C:\Datawin\GoldenTop\EXE\erp2014.exe")
    os.system("start "+Path_Golden_ERP)  # 執行Golden_ERP


def Star_ERP():
    # os.system("start C:\STARERP\RemoteClient\starerp1t.exe")
    os.system("start "+Path_Star_ERP)  # 執行Start_ERP


def createNewWindow():
    global Path_setting, setting, Path_in_Golden_ERP, Path_in_Star_ERP, Path_Golden_ERP, Path_Star_ERP  # 定義全域變數
    with open('setting.pickle', 'rb') as f:
        setting = pickle.load(f)
    Path_Golden_ERP = setting["golden_path"]  # 建立變數
    Path_Star_ERP = setting["star_path"]  # 建立變數
    Path_setting = tk.Toplevel(window)   # 建立子視窗
    Path_setting.title('設定ERP路徑')  # 設定視窗標題
    window_width = 450  # 視窗寬度
    window_height = 75  # 視窗高度
    Path_setting.resizable(False, False)  # 禁止變更大小
    left = int((screen_width - window_width)/2)  # 計算左上 x 座標
    top = int((screen_height - window_height)/2)  # 計算左上 y 座標
    Path_setting.geometry(
        f'{window_width}x{window_height}+{left}+{top}')  # 設定視窗大小、位置

    Path_setting_Golden_ERP = tk.Label(Path_setting)  # 建立標籤
    Path_setting_Golden_ERP.config(text='Golden ERP路徑：')  # 設定標籤內容
    Path_setting_Golden_ERP.grid(column=0, row=0)  # 設定標籤位置

    Path_setting_Star_ERP = tk.Label(Path_setting)   # 建立標籤
    Path_setting_Star_ERP.config(text='Star ERP路徑：')  # 設定標籤內容
    Path_setting_Star_ERP.grid(column=0, row=1)  # 設定標籤位置

    Path_in_Golden_ERP = tk.Entry(Path_setting)  # 建立單行輸入框
    Path_in_Golden_ERP.insert(0, Path_Golden_ERP)  # 設定預設文字
    Path_in_Golden_ERP.config(width=30)  # 放入單行輸入框
    Path_in_Golden_ERP.grid(column=1, row=0)  # 設定輸入框位置

    Path_in_Star_ERP = tk.Entry(Path_setting)  # 建立單行輸入框
    Path_in_Star_ERP.insert(0, Path_Star_ERP)  # 設定預設文字
    Path_in_Star_ERP.config(width=30)  # 放入單行輸入框
    Path_in_Star_ERP.grid(column=1, row=1)  # 設定輸入框位置

    Path_setting_Confirm = tk.Button(Path_setting)  # 建立按鈕
    Path_setting_Confirm.config(text="確認",  # # 顯示文字
                                command=path_save)  # 按下按鈕所執行的函數
    Path_setting_Confirm.grid(column=0, row=3)  # 設定按鈕位置


def path_save():
    golden_path = Path_in_Golden_ERP.get()  # 獲取Entry元件中的值
    star_path = Path_in_Star_ERP.get()  # 獲取Entry元件中的值

    setting = {"golden_path": golden_path,
               "star_path": star_path}  # 建立一個字典，儲存這兩個值

    with open('setting.pickle', 'wb') as f:    # 使用pickle模組將字典儲存到文件中
        pickle.dump(setting, f)

    Path_setting.destroy()     # 關閉視窗


window = tk.Tk()  # 建立主視窗
menubar = tk.Menu(window)  # 建立主選單
menubar.add_command(label="設定路徑", command=createNewWindow)    # 主選單項目&事件
window.title('ERP選單')  # 設定視窗標題
window.configure(menu=menubar,
                 background='#9D9D9D')   # 設定背景色灰色
screen_width = window.winfo_screenwidth()    # 取得螢幕寬度 (pixels)
screen_height = window.winfo_screenheight()  # 取得螢幕高度 (pixels)

window_width = 540  # 視窗寬度 (pixels)
window_height = 340  # 視窗高度 (pixels)
window.resizable(False, False)  # 禁止變更大小
left = int((screen_width - window_width)/2)       # 計算左上 x 座標
top = int((screen_height - window_height)/2)      # 計算左上 y 座標
window.geometry(f'{window_width}x{window_height}+{left}+{top}')  # 設定視窗大小、位置

button_Golden_ERP = tk.Button(window)  # 建立按鈕所在視窗
button_Golden_ERP.config(
    font=("Arial", 14, "bold"),  # 文字大小
    text='Golden ERP',  # 顯示文字
    width=15,
    pady=25,
    command=Golden_ERP)  # 按下按鈕所執行的函數
button_Golden_ERP.pack(side="top", pady=50)  # 設定按鈕位置

button_Star_ERP = tk.Button(window)  # 建立按鈕所在視窗
button_Star_ERP.config(
    font=("Arial", 14, "bold"),  # 文字大小
    text='Star ERP',  # 顯示文字
    anchor="center",
    width=15,
    pady=25,
    command=Star_ERP)  # 按下按鈕所執行的函數
button_Star_ERP.pack(side="top")  # 設定按鈕位置

window.mainloop()  # 執行主程式
