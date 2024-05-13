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

resource "aws_s3_object" "index_html" {
  bucket       = aws_s3_bucket.jet_website_bucket.bucket
  key          = "index.html"
  content      = file("../dist/index.html")
  content_type = "text/html"
}

resource "aws_s3_bucket_policy" "allow_public_read" {
  bucket = aws_s3_bucket.jet_website_bucket.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect    = "Allow"
        Principal = "*"
        Action    = "s3:GetObject"
        Resource  = "${aws_s3_bucket.jet_website_bucket.arn}/*"
      },
    ]
  })
}
