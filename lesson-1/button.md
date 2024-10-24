## 🔘 ボタン入力の理解

### 🖥️ **デジタル信号の基礎**

- **デジタル信号:**
  - **特徴:** 0 と 1 の 2 つの状態のみを持つ
  - **用途:** スイッチ、LED のオン/オフ制御など
  - ![Digital Signal](https://example.com/digital-signal.jpg)

### 🧠 **ボタン入力の基本**

- **ボタンの種類:**
  - **プッシュボタン:** 簡単にオン/オフを切り替えられる
  - **タクトスイッチ:** 小型で多用途に使用可能
- **GPIO ピンとの接続:**
  - ボタンを Raspberry Pi Pico2 のデジタル GPIO ピンに接続し、入力として使用

---

## 📡 ボタンの使用方法

### 🔧 **ボタンの紹介と接続方法**

- **必要な部品:**
  - Raspberry Pi Pico2
  - プッシュボタン
  - 10kΩ 抵抗（プルアップまたはプルダウン用）
  - ブレッドボード
  - ジャンパーワイヤー

### 🛠️ **接続図**

```plaintext
ボタン接続図
  ┌─────────┐
  │         │
  │  ボタン │
  │         │
  └─────┬───┘
        │
       10kΩ
        │
      3.3V
        │
    GP15 (デジタル入力)
        │
       GND
```

---

### プログラミング

```python
import machine
import utime

# ボタンの設定 (GP15を入力ピンとして設定し、プルアップ抵抗を有効にする)
button = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_UP)

# LEDの設定 (内蔵LEDを出力ピンとして設定)
led = machine.Pin(25, machine.Pin.OUT)

# LEDの初期状態をオフに設定
led.value(0)

while True:
    if not button.value():  # ボタンが押された場合 (低電圧)
        led.toggle()        # LEDの状態を反転
        print("ボタンが押されました！LEDを切り替えます。")
        utime.sleep(0.3)    # デバウンスのために短い待機
    utime.sleep(0.1)        # メインループの待機
```
