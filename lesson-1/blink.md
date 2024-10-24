## 💡 基本的なプログラミング概念の紹介

### 🖥️ **プログラミングとは？**

- **定義:** コンピュータやマイクロコントローラーに指示を与えるための言語
- **目的:** ハードウェアを制御し、特定の動作を実行させる

### 🔑 **基本概念**

- **変数:** データを保存するための場所
  - 例: `led_pin = machine.Pin(25, machine.Pin.OUT)`
- **関数:** 特定のタスクを実行するためのコードブロック
  - 例: `utime.sleep(1)`
- **ループ:** 同じコードを繰り返し実行するための構造
  - 例: `while True:`
- **条件分岐:** 特定の条件に基づいて異なる動作を実行
  - 例: `if button_pressed:`

---

## 🚀 サンプルコードの説明とアップロード

### 📜 **サンプルコード: LED を点滅させる**

```python
import machine
import utime

# 内蔵LEDを設定
led = machine.Pin(25, machine.Pin.OUT)

# 無限ループでLEDを点滅させる
while True:
    led.toggle()        # LEDの状態を反転
    utime.sleep(1)      # 1秒待機
```
