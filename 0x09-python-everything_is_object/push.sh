#!/bin/bash

echo "enter message"
read message

git add .
git commit -m "$message"
git push
