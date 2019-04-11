kafkaConsumer customerOrders | elasticWrite -e localhost:9200 -i hermes_customer_orders -t hermes_customer_orders
