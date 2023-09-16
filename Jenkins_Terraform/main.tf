# Resource Blocks

resource "aws_instance" "app_server" {
  ami           = var.aws_ami
  instance_type = var.instance_type

<<<<<<< Updated upstream
=======
  tags = {
    Service   = "EC2"
    ManagedBy = "Jenkins"
  }
}




>>>>>>> Stashed changes
