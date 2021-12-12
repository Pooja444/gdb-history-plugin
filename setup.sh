FILE=~/.gdbinit
if [ ! -f "$FILE" ]; then
    touch $FILE
fi
echo "source ${PWD}/plugin.py" >> $FILE