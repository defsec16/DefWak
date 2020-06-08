#обновление до последней версии
INSTALL_DIR="$HOME/DefWak"

BIN_DIR="/usr/local/bin/"

BASH_PATH="/bin/bash"

TERMUX=false


echo "\033[32m[✔] Checking directories...(Проверка каталогов...)";

if [ -d "$INSTALL_DIR" ]; then

        rm -rf "$INSTALL_DIR"

        rm "$BIN_DIR/DefWak*"

        sudo rm -rf "$INSTALL_DIR"

        sudo rm "$BIN_DIR/DefWak*"

    else

        echo "[✘] If you want to uninstall you must remove previous installations ";

        echo "[✘] Если вы хотите удалить, вы должны удалить предыдущие установки "

        echo "[✘] Провал! (Failed!)[✘]";

fi


clear

echo -e "\e[32m[✔] Отлично готово! (all good!)[✔]\e[0m"
echo -e "\e[32mВсё успешно установлено идет запуск...\e[0m"
echo -e "\e[32mEverything is successfully installed, it is starting...\e[0m"
cd

cd
git clone --depth=1 https://github.com/defsec16/DefWak.git
cd DefWak
chmod +x *
python defwak.py
