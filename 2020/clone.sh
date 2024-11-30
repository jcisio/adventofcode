#!/bin/sh
cp -r day01 day$1
cd day$1
rename s/01/$1/ *.*
sed -i s/d01.in/d$1.in/ d$1.py
echo -n > d$1.in
echo -n > problem.md
git add d$1.in problem.md
