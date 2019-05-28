#!/bin/bash
lines=$(cat "$1" | wc -l)
for (( counter=$lines; counter>0; counter-- ))
do
	echo "Doing $counter of $lines"
	lineText=$(sed -n "$counter p" "$1")
	#regex (?<=^).*(?=;) - begin to ; char
	replaceText=$(echo "$lineText" | grep -o -P '(?<=^).*(?=;)')
	#regex (?<=;).*(?=$) - ; to end char
	inputText=$(echo "$lineText" | grep -o -P '(?<=;).*(?=$)')
	echo "Replacing $inputText to $replaceText"
	sed -in 's|'"$inputText"'|'"$replaceText"'|gI' "$2"
	echo "done!"
done
