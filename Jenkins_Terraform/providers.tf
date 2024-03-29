#Providers


terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.9.0"
    }
  }
}

# Configure the AWS Provider
provider "aws" {
  region = var.region
}