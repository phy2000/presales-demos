echo
echo
echo "Listing existing ES docs [for index geo_weblogs]..."
curl -XGET 'http://localhost:9200/geo_weblogs/_search?pretty=true&q=*:*'
echo
echo "<done>"
