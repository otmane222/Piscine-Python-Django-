#!/bin/sh

bitly_link="$1"

response=$(curl -I -L "$bitly_link" 2>/dev/null )

final_url=$(echo "$response" | grep -m 1 "^Location:" | cut -d ' ' -f 2 | tr -d '\r')

echo "$final_url"