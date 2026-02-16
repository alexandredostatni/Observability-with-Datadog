terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
  }
}

provider "aws" {
  region                      = "us-east-1"
  access_key                  = "test"
  secret_key                  = "test"
  skip_credentials_validation = true
  skip_metadata_api_check     = true
  skip_requesting_account_id  = true
  s3_use_path_style           = true

  endpoints {
    s3             = "http://localhost:4566"
    secretsmanager = "http://localhost:4566"
  }
}


resource "aws_s3_bucket" "my_bucket" {
  bucket = "my-devops-bucket"
}

resource "aws_secretsmanager_secret" "my_secret" {
  name = "my-api-key"
}

resource "aws_secretsmanager_secret_version" "my_secret_version" {
  secret_id     = aws_secretsmanager_secret.my_secret.id
  secret_string = "{\"api_key\":\"fakekey\"}"
}

output "bucket_name" {
  value = aws_s3_bucket.my_bucket.bucket
}

output "secret_arn" {
  value = aws_secretsmanager_secret.my_secret.arn
}