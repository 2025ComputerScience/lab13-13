# =============================================================================
# 作業名稱：OCR-Tesseract 手寫英文辨識
# 學號：E94111261
# 姓名：(請在此填寫您的姓名)
# 組別：(請在此填寫您的組別，例如第45組)
# 說明：使用 Tesseract-OCR 工具辨識手寫英文數字文字 (e.g., forty-five)
# =============================================================================

import pytesseract
from PIL import Image
import os  # 用於處理檔案路徑系統

def main():
    # ---------------------------------------------------------
    # 1. 設定 Tesseract OCR 引擎安裝路徑
    # ---------------------------------------------------------
    # 注意：Windows 系統必須指定 tesseract.exe 的位置
    # 預設安裝路徑通常為 C:\Program Files\Tesseract-OCR\tesseract.exe
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    # ---------------------------------------------------------
    # 2. 設定圖片檔案路徑 (自動偵測)
    # ---------------------------------------------------------
    # 取得目前這支 Python 程式所在的資料夾路徑
    current_folder = os.path.dirname(os.path.abspath(__file__))
    
    # 設定目標圖片檔名 (需與程式放在同一資料夾)
    image_filename = 'handwritten.png'
    
    # 組合出完整的檔案路徑 (避免發生找不檔案的錯誤)
    image_path = os.path.join(current_folder, image_filename)

    print(f"正在讀取圖片: {image_path}")

    # 檢查圖片檔案是否存在
    if not os.path.exists(image_path):
        print("❌ 錯誤：找不到圖片檔案，請確認檔名是否為 handwritten.png 且位於同一資料夾。")
        return

    # ---------------------------------------------------------
    # 3. 執行 OCR 圖像辨識
    # ---------------------------------------------------------
    try:
        # 開啟圖片
        img = Image.open(image_path)

        # 設定辨識參數 config
        # --psm 7 : 表示將圖片視為單行文字 (Page Segmentation Mode 7)
        # lang='eng' : 指定辨識語言為英文
        text = pytesseract.image_to_string(img, lang='eng', config='--psm 7')

        # ---------------------------------------------------------
        # 4. 輸出辨識結果
        # ---------------------------------------------------------
        print("-" * 30)
        print("【 Tesseract OCR 辨識結果 】")
        print(f"圖片內容: {text.strip()}")
        print("-" * 30)
        print("執行狀態: 成功")

    except Exception as e:
        print("❌ 發生例外錯誤:")
        print(e)
        print("請檢查 Tesseract 是否已正確安裝，或路徑設定是否有誤。")

# 程式進入點
if __name__ == "__main__":
    main()