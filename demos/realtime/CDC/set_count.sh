curl -XPUT localhost:9200/cdctest_cdctest_info -d '
{
  "mappings": {
    "cdctest_info": {
      "properties": {
        "count": {
          "type":   "integer"
        }
      }
    }
  }
}
'
