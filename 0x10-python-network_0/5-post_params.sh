#!/bin/bash
# Bash scripts that sends a POST request to a given URL, and display the body of the variable
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
