# UiFLow_簡易接硬幣
---

## 遊戲目標:  
當畫面上有球從右側滑進來，並進入某一條「軌道」時，玩家需要快速按下對應的按鈕來攔截它。
---
## 使用元件：
- M5Stack 主機
- 雙按鈕擴充模組（DUAL_BUTTON）
- 3Ｄ 列印工件（本人創作，請勿販賣）
  [3D 模型](./3D_OBJ/)

---
## 遊戲邏輯解析：
### 初始化：

```python
rectangle0 = M5Rect(8, 70, 2, 90, 0xFFFFFF, 0xFFFFFF)  # 中間的接球區
label0 = M5TextBox(83, 70, "Score:00", ...)  # 顯示分數
```
---

### 控制邏輯：  
玩家可以操作雙按鈕：
	•	Blue 按鈕 對應往左邊（LineY = -1）
	•	Red  按鈕 對應往右邊（LineY = 1）
	•	預設狀態 LineY = 0 對應中間軌道
```
def btnBlue0_wasPressed(): LineY = -1
def btnBlue0_wasReleased(): LineY = 0
def btnRed0_wasPressed(): LineY = 1
def btnRed0_wasReleased(): LineY = 0
```

### 遊戲主迴圈：
```
for count in range(10):
    if random.randint(1, 3) == 1:  # 左邊球出現
        ...
    elif random.randint(1, 3) == 2:  # 中間球
        ...
    elif random.randint(1, 3) == 3:  # 右邊球
        ...
```
每次隨機選擇一條軌道，從右往左動畫移動一個圓形（球），如果球抵達左邊、而使用者有按對應的方向，就加分。
