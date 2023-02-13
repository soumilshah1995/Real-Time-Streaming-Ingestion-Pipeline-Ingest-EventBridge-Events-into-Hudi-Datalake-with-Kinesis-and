
Real Time Streaming Ingestion Pipeline Ingest EventBridge Events into Hudi Datalake with Kinesis and Glue 
![image](https://user-images.githubusercontent.com/39345855/218350182-929ff7e9-bd8c-40ae-8085-b987e204e829.png)

#### Note 
#### Make sure to select Glue 4.0 and add following job parameter

```
--conf   spark.serializer=org.apache.spark.serializer.KryoSerializer --conf spark.sql.hive.convertMetastoreParquet=false
--datalake-formats  hudi
```
![image](https://user-images.githubusercontent.com/39345855/218350588-e829c827-0221-4c01-b23d-1ff237c459f5.png)
