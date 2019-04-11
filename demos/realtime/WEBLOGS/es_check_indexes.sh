echo
echo
echo "Listing existing ES indexes..."
curl 'localhost:9200/_cat/indices?v'
echo
echo "<done>"
