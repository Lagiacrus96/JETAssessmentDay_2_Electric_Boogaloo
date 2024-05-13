provider "aws" {
    region = "us-west-2"
}

resource "aws_s3_bucket" "jet_website_bucket" {
    bucket = "jet-website-bucket"
}

resource "aws_s3_bucket_website_configuration" "config" {
    bucket = aws_s3_bucket.jet_website_bucket.bucket
    index_document {
        suffix = "index.html"
    }
    error_document {
        key = "404.html"
    }
}
