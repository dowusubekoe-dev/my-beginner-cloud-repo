from diagrams import Diagram
from diagrams import Cluster
from diagrams.aws.general import User
from diagrams.onprem.client import Client
# from diagrams.programming.language import Bash
from diagrams.aws.network import VPC
from diagrams.aws.compute import EC2

with Diagram("Connect to Windows EC2 Instance", show=False):
    iam_user = User("iam_user")
    rdp_client = Client("rdp_client")

    with Cluster("Virtual Private Cloud"):
            svc_vpc = EC2("web")
    iam_user >> rdp_client >> svc_vpc

