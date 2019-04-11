echo "DELETE the index <cdctest_cdctest_info>..."
curl -X DELETE localhost:9200/cdctest_cdctest_info
echo
sleep 1

##Enable this only once (before creating mapping)
#echo "CREATE mapping for index <cdctest_cdctest_info>..."
#curl -XPUT 'localhost:9200/cdctest_cdctest_info?pretty'
#echo
echo
echo "CREATE mapping for INDEX <cdctest_cdctest_info> and TYPE <log_entry>..."
curl -XPUT 'http://localhost:9200/cdctest_cdctest_info/' -d '
{
    "mappings" : {
        "cdctest_info" : {
            "properties" : {
                "OP_TYPE" : {
                    "type" : "text",
                    "fields" : {
                        "keyword" : {
                            "type" : "keyword",
                            "ignore_above" : 256
                        }
                    }
                },
                "TimeStampDateTime" : {
                    "type" : "text",
                    "fields" : {
                        "keyword" : {
                            "type" : "keyword",
                            "ignore_above" : 256
                        }
                    }
                },
                "TimeStampStr" : {
                    "type" : "date"
                },
                "count" : {
                    "type" : "integer"
                },
                "post_date" : {
                    "type" : "date"
                }
            }
        }
    }
}

'

## To visualize index content:
#http://localhost:9200/cdctest_cdctest_info/_search?pretty=true&q=*:*

sleep 1
echo
echo
echo "Displaying created index..."
curl -XGET "http://localhost:9200/cdctest_cdctest_info/_mapping?pretty=true"

sleep 1
echo
echo
echo "Listing existing indexes..."
curl 'localhost:9200/_cat/indices?v'
echo
echo "<done>"
#        "coords": {
#              "type":"geo_point"
#        },

#"tstamp":"2017-04-26T18:33:58.861706Z"

#"location" : "41.12,-71.34"
#"location" : "drm3btev3e86"

# python WebLogExt2ES.py WebLogExt.json > WebLogExt2ES.json

#curl -XPUT localhost:9200/gt_readings/_bulk?pretty --data-binary @WebLogExt2ES.json

