#!/bin/bash

echo "Enter you Message"

read message

git add .
git commit -m "$message"
git push
