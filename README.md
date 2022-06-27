# Integracao Dados com do Postgres para o S3 com Debezium 
Integrate data from marvel_api to evalute characters and numbers of comics

### Architecture 
![alt text](https://github.com/Marcaoandradenogueira/blue_marvel_api/blob/master/images/Diagram.png?raw=true)


### Command Terraform

#### Init and construct terraform
```sh
terraform init
```
```sh
terraform apply --var-file="dev.tfvars" --var-file="table_conf_vars/information.tfvars"
```

#### Destruir toda a infraestrutura
```sh
terraform destroy --var-file="dev.tfvars" --var-file="table_conf_vars/information.tfvars"
```

