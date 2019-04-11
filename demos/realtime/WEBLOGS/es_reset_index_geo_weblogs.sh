echo "DELETE the index <geo_weblogs>..."
curl -X DELETE localhost:9200/geo_weblogs
echo
sleep 1

##Enable this only once (before creating mapping)
#echo "CREATE mapping for index <geo_weblogs>..."
#curl -XPUT 'localhost:9200/geo_weblogs?pretty'
#echo
echo
echo "CREATE mapping for INDEX <geo_weblogs> and TYPE <log_entry>..."
curl -XPUT 'http://localhost:9200/geo_weblogs/' -d '
{
  "mappings": {
      "log_entry": {
	    "properties": {
			"date_time": {
				"type":   "date",
				"format": "yyyy-MM-dd'"'T'"'HH:mm:ss.SSSSSSZ"
			},
			"receiveTime": {
				"type": "keyword"
			},
			"pageType": {
				"type": "keyword"
			},
			"orderId": {
				"type": "keyword"
			},
			"customerId": {
				"type": "keyword"
			},
			"productId": {
				"type": "keyword"
			},
			"productReview": {
				"type": "keyword"
			},
			"productDescription": {
				"type": "keyword"
			},
			"returnReason": {
				"type": "keyword"
			},
			"first_hit_time_gmt": {
				"type": "text"
			},
			"last_hit_time_gmt": {
				"type": "text"
			},
			"hit_time_gmt": {
				"type": "text"
			},
			"domain": {
				"type": "keyword"
			},
			"accept_language": {
				"type": "keyword"
			},
			"ip": {
				"type": "keyword"
			},
			"longitude": {
				"type": "text"
			},
			"latitude": {
				"type": "text"
			},
			"id": {
				"type": "keyword"
			},
			"index": {
				"type": "keyword"
			},
			"visit_page_num": {
				"type": "keyword"
			},
			"cookies_accepted": {
				"type": "keyword"
			},
			"java_enabled": {
				"type": "text"
			},
			"visit_num": {
				"type": "text"
			},
			"login_id": {
				"type": "keyword"
			},
			"registered": {
				"type": "text"
			},
			"paid_search": {
				"type": "keyword"
			},
			"page_event": {
				"type": "keyword"
			},
			"pagename": {
				"type": "keyword"
			},
			"user_srvr": {
				"type": "keyword"
			},
			"referrer": {
				"type": "text"
			},
			"user_agent": {
				"type": "text"
			},
			"page_url": {
				"type": "text"
			}
	     }
       }
  }
}
'

## To visualize index content:
#http://localhost:9200/geo_weblogs/_search?pretty=true&q=*:*

sleep 1
echo
echo
echo "Displaying created index..."
curl -XGET "http://localhost:9200/geo_weblogs/_mapping?pretty=true"

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

