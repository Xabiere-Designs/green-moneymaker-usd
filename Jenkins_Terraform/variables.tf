#Variables

variable "aws_ami" {
  type    = string
  default = "ami-0f9ce67dcf718d332"
}
variable "instance_type" {
  type    = string
  default = "t2.micro"
}
