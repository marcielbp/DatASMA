#!/bin/bash
#cat "$1" | sed -e 's/;;/; ;/g'| column -s, -t
#sed -n '9p' "$1" | sed -n '/[[:digit:]];/p'
#matchText=$(sed -n '9p' "$1")
#;.*\n
#echo "8;florianopolis67" | grep -o -P '(?<=;).*(?=67)'
lines=$(cat "$1" | wc -l)
echo "$lines"
for (( counter=2; counter<=$lines+1; counter++ ))
do
	#arch=$(uname -m)
	lineText=$(sed -n "$counter p" "$1")
	inputText=$(echo "$lineText" | grep -o -P '(?<=^).*(?=;)')
	echo "$inputText"
	replaceText=$(echo "$lineText" | grep -o -P '(?<=;).*(?=$)')
	echo "$replaceText"
done
