# Install Offline Wheels / オフラインホイールインストーラー

## English

A simple Python script to install offline wheel files from a local directory.

### Features
- Installs Python wheel (.whl) files from a `./downloads/` directory
- Checks for virtual environment usage (recommended for safety)
- Uses `--no-deps --force-reinstall` flags for offline installation
- Can be used with [download_requirements_wheels](https://github.com/Moge800/download_requirements_wheels) to download wheels first.

### Usage
1. Place your wheel files in a `./downloads/` directory
2. Run the script:
   ```bash
   python main.py
   ```
   Or use the PowerShell launcher:
   ```powershell
   .\launch.ps1
   ```

### Requirements
- Python 3.6+
- pip
- Wheel files in `./downloads/` directory

### Safety Features
- Virtual environment detection with user confirmation if not using one
- Prevents accidental system-wide installations

---

## 日本語

ローカルディレクトリからオフラインのホイールファイルをインストールするシンプルなPythonスクリプトです。

### 機能
- `./downloads/` ディレクトリからPythonホイール(.whl)ファイルをインストール
- 仮想環境の使用チェック（安全のため推奨）
- オフラインインストール用に `--no-deps --force-reinstall` フラグを使用
- [download_requirements_wheels](https://github.com/Moge800/download_requirements_wheels) と併用することで、先にホイールをダウンロードできます。

### 使用方法
1. ホイールファイルを `./downloads/` ディレクトリに配置
2. スクリプトを実行:
   ```bash
   python main.py
   ```
   またはPowerShellランチャーを使用:
   ```powershell
   .\launch.ps1
   ```

### 必要条件
- Python 3.6+
- pip
- `./downloads/` ディレクトリ内のホイールファイル

### 安全機能
- 仮想環境の検出機能と、使用していない場合のユーザー確認
- システム全体への意図しないインストールを防止
