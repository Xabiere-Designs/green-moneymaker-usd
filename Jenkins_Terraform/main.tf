# Resource Blocks

resource "aws_instance" "app_server" {
  ami           = var.aws_ami
  instance_type = var.instance_type

<<<<<<< Updated upstream
  tags    = {}
    Name  = "jenkins_pipeline"
=======
  tags = {
    Name = "Jenkins_Server"
  }
>>>>>>> Stashed changes
}



