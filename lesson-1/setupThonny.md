## 🖥️ Raspberry Pi Pico2 の開発環境設定

### 🔧 **Raspberry Pi Pico2 とは？**

- **概要:**
  - 小型で強力なマイクロコントローラーボード
  - RP2040 チップを搭載し、豊富な GPIO ピンを持つ
  - プログラミング言語として MicroPython や C/C++が使用可能

### 📥 **開発環境のインストール（事前準備）**

- **推奨開発環境:**
  - **MicroPython:** 初心者に優しく、インタラクティブなプログラミングが可能
  - **Thonny IDE:** 簡単に使える Python 専用の統合開発環境
- **インストール手順:**
  1. **Thonny のダウンロードとインストール:**
     - [Thonny 公式サイト](https://thonny.org/)から最新バージョンをダウンロード
     - インストーラーを実行し、画面の指示に従ってインストール
  2. **MicroPython ファームウェアのインストール:**
     - [Raspberry Pi 公式サイト](https://www.raspberrypi.org/documentation/microcontrollers/micropython.html)から最新の MicroPython ファームウェアをダウンロード
     - Pico2 をブートローダーモードで接続（BOOTSEL ボタンを押しながら USB 接続）
     - ダウンロードした`.uf2`ファイルを Pico2 のドライブにドラッグ＆ドロップ

### 🖱️ **Raspberry Pi Pico2 の接続**

#### 📦 **必要なもの**

- **Raspberry Pi Pico2 ボード**
- **USB ケーブル:** データ転送対応のマイクロ USB ケーブル
- **パソコン:** Thonny IDE がインストールされたもの

#### 🖇️ **接続手順**

1. **USB ケーブルを用意:**
   - マイクロ USB ケーブルの一端を Pico2 の USB ポートに、もう一端をパソコンの USB ポートに接続
2. **ブートローダーモードで接続:**
   - Pico2 の BOOTSEL ボタンを押しながら USB ケーブルを接続
   - パソコンに「RPI-RP2」というドライブが認識されることを確認
3. **MicroPython ファームウェアのフラッシュ:**
   - ダウンロードした`.uf2`ファイルを「RPI-RP2」ドライブにドラッグ＆ドロップ
   - 自動的に再起動し、Pico2 が MicroPython モードで動作を開始

#### ✅ **ボードの認識確認**

- **Thonny IDE での設定:**
  1. Thonny を起動
  2. メニューから `ツール > オプション > インタープリター` を選択
  3. **インタープリター:** `MicroPython (Raspberry Pi Pico)` を選択
  4. **ポート:** 自動的に認識されるポートを選択
  5. **OK** をクリックして設定を保存
- **接続確認:**
  - Thonny の下部にシリアルコンソールが表示され、Pico2 からのメッセージが確認できる

---

## 💡 基本的な IDE の使い方

### 📝 **Thonny IDE の基本操作**

- **新しいスクリプトの作成:**
  - `ファイル > 新規` で新しい Python スクリプトを開始
- **コードの保存:**
  - `ファイル > 名前を付けて保存` でスクリプトを保存
  - 自動的に Pico2 に保存され、実行準備が整う
- **コードの実行:**
  - 上部の`▶️ 実行`ボタンをクリックしてスクリプトを実行
- **シリアルコンソールの活用:**
  - Thonny の下部にあるシリアルコンソールで、Pico2 からの出力やデバッグメッセージを確認

### 🔄 **基本的なプログラムの書き方**

- **基本構造:**

  ```python
  import machine
  import utime

  led = machine.Pin(25, machine.Pin.OUT)  # 内蔵LEDを設定

  while True:
      led.toggle()        # LEDの状態を反転
      utime.sleep(1)      # 1秒待機
  ```
