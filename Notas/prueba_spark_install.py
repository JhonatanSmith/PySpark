from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("MiPrimeraSesion").getOrCreate()
print(spark.version)
spark.stop()
