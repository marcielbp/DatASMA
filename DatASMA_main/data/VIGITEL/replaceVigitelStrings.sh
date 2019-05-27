#!/bin/bash
lines=$(cat "$1" | wc -l)
echo "$lines"
#for (( counter=2; counter<=$lines+1; counter++ ))
for (( counter=2; counter<=5; counter++ ))
do
	#arch=$(uname -m)
	lineText=$(sed -n "$counter p" "$1")
	#regex (?<=^).*(?=;) - begin to ; char
	replaceText=$(echo "$lineText" | grep -o -P '(?<=^).*(?=;)')
	#echo "$inputText"
	#regex (?<=;).*(?=$) - ; to end char
	inputText=$(echo "$lineText" | grep -o -P '(?<=;).*(?=$)')
	#echo "$replaceText"
	echo "Replacing $inputText to $replaceText"
	# https://stackoverflow.com/questions/47827749/replacing-text-with-sed-containing-whitespace-in-variable
	sed -in 's|'"$inputText"'|'"$replaceText"'|g' "$2"
	echo "done!"
done

