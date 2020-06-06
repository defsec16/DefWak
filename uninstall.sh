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

        echo "\033[31m[✘] If you want to uninstall you must remove previous installations\033[31m [✘] ";

        echo "\033[31m[✘] Если вы хотите удалить, вы должны удалить предыдущие установки \033[31m[✘]"

        echo "\033[31m[✘] Провал! (Failed!)[✘]\033[31m ";

fi


clear

echo "'\033[32m'+[✔] Отлично готово! (all good!)[✔]"

cd
