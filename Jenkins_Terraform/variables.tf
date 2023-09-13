#Variables

variable "aws_ami" {
  type    = string
  default = "ami-05548f9cecf47b442"
}
variable "instance_type" {
  type    = string
  default = "t2.micro"
}
variable "aws_access_key" {
    default = "access key"
}
variable "aws_secret_key" {
    default = "secret key"
}