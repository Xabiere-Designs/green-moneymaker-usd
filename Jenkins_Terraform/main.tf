# Resource Blocks

resource "aws_instance" "Jenkins" {
  ami           = var.aws_ami
  instance_type = var.instance_type

  tags = {
    Service   = "EC2"
    ManagedBy = "Jenkins"
  }
}




