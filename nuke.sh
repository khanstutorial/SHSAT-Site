#!/usr/bin/env bash

rm ./nukeShelter/index.html
rm ./nukeShelter/thankyou.html
cp ./index.html ./nukeShelter
cp ./thankyou.html ./nukeShelter
rm *.html
cp ./nukeShelter/index.html ./nukeShelter/thankyou.html .
