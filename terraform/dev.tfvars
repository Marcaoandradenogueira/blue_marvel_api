service_name = "MARVEL"
environment  = "dev"


instances_params = {
  kafka_delta = {
    keypair_name  = "inter_tech_key"
    subnet_id     = "subnet-dc9a2bba"
    vpc_id        = "vpc-6bfd3016"
    instance_type = "t2.large"
  }
}

lambda_environment =  [
  {
    function_name        = "EMR-DELTALAKE"
    keypair_name         = "debezium"
    master_instance_type = "m5.xlarge"
    core_instance_type   = "m5.xlarge"
    instance_count       = 1
    ec2_master_name      = "EMR-DELTALAKE-MASTER"
    ec2_core_name        = "EMR-DELTALAKE-CORE"
    ebs_size_gb          = 50
    ec2_subnet_id        = "subnet-dc9a2bba"
    time_interval        = 144000
  },
]

lambda_environment_ingest =  [
  {
    function_name        = "INGEST_DATA"
    time_interval        = 144000
  },
]


