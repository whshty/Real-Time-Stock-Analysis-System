#1. read from kafka, kafka broker, kafka topic 
#2. write back to kafka , kafka broker, new kafka topic 

import atexit
import sys
import logging 

logger_format = '%(asctime)-15s %(message)s'
logging.basicConfig(format=logger_format)
logger = logging.getLogger('stream-processing')
logger.setLevel(logging.INFO)

#empty string
topic = ""
new_topic = ""
kafka_broker = ""


# write back to kafka 
from kafka import KafkaProducer
from kafka.errors import KafkaError, KafkaTimeoutError

# import spark 
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils



def stutdown_hook(producer):
	try:
		logger.info('flush pending message to kafka')
		producer.flush(10)
		logger.info('finish flushing pendning message')
	except KafkaError as kafka_error:
		logger.warn('Failed to flush pending message to kafka')
	finally:
		try:
			producer.close()
		except Exception as e:
			logger.warn('Failed to close kafka connection')

	producer.close(10)

def process(timeobj ,rdd):
	# - test No.1
	print(rdd)



if __name__== '__main__':
    if len(sys.argv) != 4;
     	print('Usage: streaming processing [topoc] [new topic] [kafka_broker]')
     	exit(1)
     # ignore the name of index 1 (which is steaming processing )
     topic , new_topic, kafka_broker = sys.argv[1:]

     # - setup connection to spark cluster
     ## spark run on local
     ### 2 : number of thread
     sc = sparkContext("local[2]", "StockAveragePrince")
     #logging
     sc.setLogLevel('ERROR')
     ### every 5 second 
     ssc = StreamingContext(sc, 5)

     # - create a data stream from spark
     ### - stream data - the source of data - the location of Kafka
     directKafkaStream = kafkaUtils.createDirectStream(ssc, [topic], {'metadata.broker.list':kafka_broker});
     
     # for each RDD , do something
     # TODO
     directKafkaStream.foreachRDD(process)

     # - instantiate kafka producer 
     kafka_producer  = KafkaProducer(bootstra_servers = kafka_broker)

     # - setup proper shutdown hook 
     # TODO
     atexit.register(shutdown_hook, kafka_producer)

     # - start data streaming
     ssc.start();
     ssc.awaitTermination();










    
