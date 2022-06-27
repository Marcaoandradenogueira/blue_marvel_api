variable "service_name" {
  type = string
}

variable "environment" {
  type        = string
  description = "Environment where the resources are deployed. Eg. dev, qas, prod"
}


variable "instances_params" {}

variable "lambda_environment" {}

variable "lambda_environment_ingest" {}

variable "conf_tables" {}

