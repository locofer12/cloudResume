terraform {
  required_providers {
    aws = {
        version = ">=4.9.0"
    }
  }
}
provider "aws" {
          profile= "your_cli_profile"
        access_key = ""
        secret_key = "" 
}