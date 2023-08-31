#!/bin/bash
# Sends a JSON POST request to the given URL with and a JSON file.
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
