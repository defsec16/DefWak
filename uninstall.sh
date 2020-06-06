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

echo "\033[32m[✔] Отлично готово! (all good!)[✔]"

cd
