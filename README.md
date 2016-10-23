## Real-Time-Stock-Analysis-System

Prerequisites.

- Python
- Docker Toolbox 
- zookeepr
- Kafka
- Redis
- Spark

#### Create a docker machine called bigdata
#### Name of my docker-machine : bigdata

Check the list of docker machine

```
$ docker-machine ls
```

Start docker machine 

```
$ docker-machine start bigdata
```

Steps 1: Fetch data from stock (terminal 1)

```
$ docker rm -f $(docker ps -a -q)

$ docker ps

$ eval $(docker-machine env bigdata)

$ ./local-setup.sh bigdata

$ python simple-data-producer.py AAPL stock-analyzer 192.168.99.100:9092


```

Step 2: Start streaming processor (terminal 2 )

```
$ spark-submit --jars spark-streaming-kafka-0-8-assembly_2.11-2.0.0.jar stream-processing.py stock-analyzer average-stock-price 192.168.99.100:9092

```


Start a Zookeeper Container:

```
$ docker run -d -p 2181:2181 -p 2888:2888 -p 3888:3888 --name zookeeper confluent/zookeeper
```

Start a Kafka Container

```
$ docker run -d -p 9092:9092 -e KAFKA_ADVERTISED_HOST_NAME=`docker-machine ip bigdata` -e KAFKA_ADVERTISED_PORT=9092 --name kafka --link zookeeper:zookeeper confluent/kafka
```

Start a Redis Container

```
$ docker run -d -p 6379:6379 --name redis redis:alpine
```