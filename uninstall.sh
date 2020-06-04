INSTALL_DIR="$HOME/DefWak"

BIN_DIR="/usr/local/bin/"

BASH_PATH="/bin/bash"

TERMUX=false


echo "[✔] Checking directories...";

if [ -d "$INSTALL_DIR" ]; then

        rm -rf "$INSTALL_DIR"

        rm "$BIN_DIR/DefWak*"

        sudo rm -rf "$INSTALL_DIR"

        sudo rm "$BIN_DIR/DefWak*"

    else

        echo "[✘] If you want to uninstall you must remove previous installations [✘] ";

        echo "[✘] Failed! [✘] ";

fi


clear

echo "[✔] all good!"
