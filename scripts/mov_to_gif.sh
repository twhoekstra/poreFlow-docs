# Source - https://stackoverflow.com/q/34552247
# Posted by Konstantin, modified by community. See post 'Timeline' for change history
# Retrieved 2026-03-31, License - CC BY-SA 3.0

#!/bin/sh

palette="./tmp/palette.png"

filters="fps=15,scale=320:-1:flags=lanczos"

ffmpeg -v warning -i $1 -pix_fmt rgb24 -r 24 $2
