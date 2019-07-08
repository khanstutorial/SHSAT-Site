#!/usr/bin/env bash

rm ./nukeShelter/index.html
rm ./nukeShelter/thankyou.html
rm ./nukeShelter/indexAST.html
rm ./nukeShelter/indexBK.html
rm ./nukeShelter/indexFP.html
rm ./nukeShelter/indexJA.html
rm ./nukeShelter/indexJH.html
rm ./nukeShelter/indexOP.html
rm ./nukeShelter/indexPCCH.html
rm ./nukeShelter/indexRH.html
rm ./nukeShelter/indexSS.html
rm ./nukeShelter/indexSUT.html
cp ./index.html ./nukeShelter
cp ./thankyou.html ./nukeShelter
cp ./indexAST.html ./nukeShelter
cp ./indexBK.html ./nukeShelter
cp ./indexFP.html ./nukeShelter
cp ./indexJA.html ./nukeShelter
cp ./indexJH.html ./nukeShelter
cp ./indexOP.html ./nukeShelter
cp ./indexPCCH.html ./nukeShelter
cp ./indexRH.html ./nukeShelter
cp ./indexSS.html ./nukeShelter
cp ./indexSUT.html ./nukeShelter
rm *.html
cp ./nukeShelter/index.html ./nukeShelter/thankyou.html .
cp ./nukeShelter/indexAST.html .
cp ./nukeShelter/indexBK.html .
cp ./nukeShelter/indexFP.html .
cp ./nukeShelter/indexJA.html .
cp ./nukeShelter/indexJH.html .
cp ./nukeShelter/indexOP.html .
cp ./nukeShelter/indexPCCH.html .
cp ./nukeShelter/indexRH.html .
cp ./nukeShelter/indexSS.html .
cp ./nukeShelter/indexSUT.html .
