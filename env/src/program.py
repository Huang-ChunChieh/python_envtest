# 使用 venv 來建立虛擬環境。
# 開啟新的 Bash 視窗，然後執行下列命令：

# Bash-->
python - m venv env
# 已在終端機中建立 env 目錄


# 啟動虛擬環境
# Windows
source env/Scripts/activate
# Linux, WSL or macOS
source env/bin/activate
# 終端機中看到 (env)。表示已啟用虛擬環境，並自行與機器的其餘部分隔離。


# 安裝程式庫
# 執行 pip freeze 查看環境中已安裝的程式庫：
# Bash-->
pip freeze
# 執行 pip install ...以安裝程式庫：
pip install python-dateutil


# 停用虛擬環境
# Bash-->
deactivate

#--------------------------------------------------------------------------------------------------------#

# 凍結：建立專案檔
您已了解如何使用命令 pip freeze 來列出虛擬環境中安裝的套件。但其有其他用途
請想像您想要與其他開發人員共同作業專案。 共同作業的好方法是使用 GitHub。

# 共用專案
若要共用您的專案，以讓其他人可以處理該專案，請執行下列步驟：

1.呼叫 pip freeze > requirements.txt。 此命令會建立 requirements.txt 檔案，其中包含程式所需的所有套件。
2.建立 .gitignore 檔案，並簽入您的應用程式程式碼和 requirements.txt。
3.將程式碼簽入 GitHub。

# 取用專案
若要作為參與者(開發人員) 取用專案，請執行下列步驟：

1.從 GitHub 擷取專案。
2.建立虛擬環境並將您自己放置到其中。
3.使用 pip install - r requirements.txt 還原專案。 其會尋找 requirements.txt 並擷取和安裝針對該檔案列出的套件。
4.執行應用程式。

#--------------------------------------------------------------------------------------------------------#

# 管理相依性
# 針對 Bug 修正套件或新增更多功能時，其版本號碼通常會變更。為了方便程式運作，可能需要特定版本的套件。

升級套件的主要原因：

1.錯誤修正。 您使用的程式庫可能會有問題。 例如，功能無法如預期般運作，而且作者會進行修正。 您很可能想要在這類修正就緒時立即升級套件。
2.安全性問題。 您的套件可能有安全性弱點。 發行這類修正程式之後，您想要升級套件以保護公司與客戶。
3.其他功能。 更多功能的版本雖然好，但不是升級套件的強力原因。 不過，如果有一個您正在等候的功能，您可能會想要為了該原因升級。

# 安裝特定版本
# EX:
pip install python-dateutil == =1.4

# 升級套件
pip install < name of package > --upgrade

# 清除未使用的套件
pip uninstall python-dateutil

較佳的方法是使用 autoremove 命令：
pip install pip-autoremove
pip-autoremove python-dateutil - y
