output=$(awk '{print $1}' ./access_log.txt | sort | uniq -c | sort -nr | head -n 1 | awk '{print $2}')
curl http://ipwhois.app/json/{$output} | \
    python3 -c "import sys, json; print(json.load(sys.stdin)['country'])"
