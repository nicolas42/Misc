# ffmpeg -ss 01:07:07 -to 01:07:45 -i input.mp4 -c:v copy -c:a copy output.mp4

echo $1
echo $2
echo $3


ffmpeg -ss $2 -to $3 -i "$1" -c:v copy -c:a copy output.mp4
