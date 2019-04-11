echo DELETE the index geo_beer_readings
curl -X DELETE localhost:9200/geo_beer_readings
echo
echo CREATE mapping for index geo_beer_readings and type reading
curl -XPUT localhost:9200/geo_beer_readings -d '
{
  "mappings": {
    "reading": {
      "properties": {
        "receiveTime": {
          "type":   "date",
          "format": "yyyyMMdd-HHmmss.SSS"
        },
        "coords": {
              "type":"geo_point"
        }
      }
    }
  }
}
'
#"location" : "41.12,-71.34"
# "location" : "drm3btev3e86"

# python WebLogExt2ES.py WebLogExt.json > WebLogExt2ES.json

#curl -XPUT localhost:9200/gt_readings/_bulk?pretty --data-binary @WebLogExt2ES.json

curl 'localhost:9200/_cat/indices?v'
