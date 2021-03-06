from pyspark.sql import SparkSession

spark = (
    SparkSession.builder.appName("ExerciseSpark")
    .getOrCreate()
)

censo = (
    spark
    .read
    .option("inferSchema", True)
    .option("header", True)
    .option("delimiter", "|")
    .csv("s3://datalake-psalomao-155914520574/raw-data/matricula_*.csv")
)

(
    censo
    .write
    .mode("overwrite")
    .format("parquet")
    .partitionBy("CO_UF")
    .save("s3://datalake-psalomao-155914520574-tf/staging-zone/censo/")
)