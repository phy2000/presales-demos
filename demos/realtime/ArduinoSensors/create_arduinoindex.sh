INDEX_NAME=arduino_sensors_index
echo DELETE the index $INDEX_NAME
curl -X DELETE localhost:9200/$INDEX_NAME
echo
echo CREATE mapping for index $INDEX_NAME and type reading
curl -XPUT localhost:9200/$INDEX_NAME -d '
{
  "mappings": {
    "arduino_reading": {
      "properties": {
        "receiveTime": {
          "type":   "date",
          "format": "yyyyMMdd-HHmmss.SSS"
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
