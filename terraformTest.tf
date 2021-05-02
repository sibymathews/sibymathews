provider "aws" {
   profile = "default"
   region  = "us-west-2"
}
resource "aws_s3_bucket" "tf_coure"{
   bucket = "tf-course-20210404"
   acl    = "private"
}
