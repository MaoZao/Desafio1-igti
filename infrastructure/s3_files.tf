resource "aws_s3_bucket_object" "job_spark_delta" {
  bucket = aws_s3_bucket.dl.id
  key    = "emr-code/pyspark/job_spark_from_tf.py"
  acl    = "private"
  source = "../job_spark_delta.py"
  etag   = filemd5("../job_spark_delta.py")
}