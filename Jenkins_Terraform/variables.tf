#Variables

variable "aws_ami" {
  type    = string
  default = "ami-0f9ce67dcf718d332"
}
variable "instance_type" {
  type    = string
  default = "t2.micro"
}
variable "aws_access_key" {
    default = "ACCESS KEY"
}
variable "aws_secret_key" {
    default = "SECRET KEY"
}
