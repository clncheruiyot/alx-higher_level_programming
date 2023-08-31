#!/bin/bash

# Send a request to a URL with curl and display the size of the response body
curl_response=$(curl -s "$1")
response_size=$(echo -n "$curl_response" | wc -c)

# Display the size of the response body in bytes
echo "Size of the response body: $response_size bytes"
