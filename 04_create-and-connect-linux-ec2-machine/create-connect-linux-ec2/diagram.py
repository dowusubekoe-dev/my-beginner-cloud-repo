from diagrams import Diagram
from diagrams import Cluster
from diagrams.aws.general import User
# from diagrams.onprem.client import Client
from diagrams.programming.language import Bash
from diagrams.aws.network import VPC
from diagrams.aws.compute import EC2

with Diagram("Connect to Linux EC2 Instance", show=False):
    iam_user = User("iam_user")
    terminal = Bash("terminal")

    with Cluster("Virtual Private Cloud"):
        svc_vpc = EC2("linux")
    iam_user >> terminal >> svc_vpc

