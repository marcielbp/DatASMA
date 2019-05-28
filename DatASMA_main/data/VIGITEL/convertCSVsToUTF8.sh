#!/bin/bash
for f in *.csv*
do
	filename=$(echo "$f" | sed 's/.csv/-UTF-8.csv/g')
	echo "converting $f to UTF-8..."
	iconv -f WINDOWS-1254 -t UTF-8//TRANSLIT "$f" -o "$filename"
	echo "Done!"
done