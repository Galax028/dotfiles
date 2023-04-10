#!/bin/bash

SCREENSHOT_TIME=$(date +"%I-%M-%S%P_%d-%m-%y")
SCREENSHOT_FILE="$HOME/Pictures/Screenshots/screenshot_$SCREENSHOT_TIME.png"

gnome-screenshot -cf "$SCREENSHOT_FILE" &&
    cat "$SCREENSHOT_FILE" | xclip -i -selection clipboard -target image/png &&
    dunstify "Screenshot taken" "Screenshot saved as screenshot_$SCREENSHOT_TIME.png"
