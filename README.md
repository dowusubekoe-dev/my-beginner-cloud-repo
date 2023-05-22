### AWS Solution Architect
This is the notes I personally made during the K21 Academy Course and additional notes taken from the AWS official documentation site. You can clone this repository or contribute by adding any information that I might have missed.

#### Introduction to Cloud Computing
##### Traditional Architecture
Companies were hosting all their servers and other network resources either in the office or a data center (on-premise).

###### Problems with Traditional Architecture
- Payment for the data center (rent)
- Pay for both power and cooling maintenance
- Duration taken to replace faulty hardware
- Scaling is limited
- The need for 24/7 monitoring of infrastructure
- How to deal with natural disasters

##### What is Cloud  Computing?
Clouding computing is the delivery of computing services: *servers*, *storage*, *databases*, *networking tools*, and *software* over the internet.
Cloud Computing enables companies to consume a compute resources (servers, storage, or application).

#### Cloud Computing Characteristics
- On-demand self-service (No human intervention needed to get resources)
- Broad network access (Access from anywhere)
- Resource pooling (Provider shares resources to customers)
- Rapid elasticity (Get more resources quickly as needed)
- Measured services (Pay only for what you consume)


- **Converting**: *Capital Expense (Capex) into Operational Expense (Opex)*
- **Capex**: *is upfront investment*
- **Opex**: *is pay as you go*

#### Benefits of Cloud Computing
* Highly scalable
* More flexible
* Increased speed and agility
* Benefits from massive economies of scale
* Reduce Infrastructure cost
* Higher security
* Disaster recovery
* No location constraints


- **High Availability**: maintaining acceptable continuous performance despite temporary load fluctuations or failure in services, hardware and datacenter.
- **Disaster Recovery**: involves a set of policies, tools and procedures to enable recovery or continuation of vital technology infrastructure and systems. When designing Disaster Recovery, consider **RPO*** (Recovery Point Objective) and ***RTO*** (Recovery Time Objective). Also know as ***BCP*** (Business Continuity Planning).
- **Fault Tolerance**: systems ability to continue operations properly when one or more of its components fails.
- **Cloud Scalability**: is a strategic operation for adding computing resources to support demand. The need to have a system that can handle growth is very important.


 - **Scale-out/Horizontal Scaling**: upgrade the capacity of the app by increasing the number of host instances. Ex: Load Balancer where app is hosted on multiple instances. Normally done on the application servers or on the frontend.
 - **Scale-up/Vertical Scaling**: upgrade the capacity of the host where the app is hosted. Ex: increase RAM from 4 to 8 cores. Generally done on the database side.
 - *Cloud Elasticity*: represents more of a tactical approach to allocating resources. Elasticity provides the necessary resources required for the current workload but also scales up or down to handle peak utilization period as well as off-peak loads.


#### Cloud Service Model
- ***Traditional On-Premise*** -
Applications | Data | Runtime | Middleware | O/S | Virtualization | Servers | Storage | Networking
- ***IaaS*** -
Applications | Data | Runtime | Middleware | O/S | **Virtualization** | **Servers** | **Storage** | **Networking**
- ***PaaS*** -
Applications | Data | **Runtime** | **Middleware** | **O/S** | **Virtualization** | **Servers** | **Storage** | **Networking**
- ***SaaS*** -
**Applications** | **Data** | **Runtime** | **Middleware** | **O/S** | **Virtualization** | **Servers** | **Storage** | **Networking**

#### Cloud Deployment Model
##### Public Cloud
* Offered by third-party providers (AWS, Google Cloud, Azure)
* Available to anyone over the public internet
* Scales quickly and convenient

##### Hybrid Cloud
* Combination of both public and private cloud
* Shared security responsibility
* Helps maintain tighter controls over sensitive data and processes
* Highly Available / Disaster Recovery

##### Private Cloud
* Offered to select users over the internet or a private internal network
* Provides greater security controls
* Requires traditional data center staffing and maintenance

##### AWS Overview Comparison
| Amazon AWS         |      Microsoft Azure       |     Google Cloud Platform |
| :---------------- | :----------------- | :----------- |
| S3 | Blob Storage |        Storage |
| EC2       |    Virtual Machine    | Compute Engine |
| EC2 Container Service       |    Container Service    | Kubernetes Engine |
| Elastic Beanstalk       |    Azure App service    | App Engine |
| DynamoDB       |    Cosmos DB    | Cloud Datastore |
| RDS       |    SQL Database    | BigQuery |
| Lambda       |    Azure Functions    | Cloud Functions |

##### AWS Global Infrastructure
AWS Global infrastructure consist of:
* ***Region***: A group of Availability Zones
* ***Availability Zones***: Multiple Datacenters distance apart

#### AWS Services
##### Deployment & Management
***Application Services***: Amazon SQS, Amazon Elastic Transcoder, Amazon SES, Amazon AppStream, Amazon Cloud Search
***Mobile Services***: Amazon Cognito, Amazon Mobile Analytics, Amazon SNS		
***Enterprise Applications***: Amazon WorkDocs, Amazon WorkSpaces, Amazon WorkMail

##### Application Services
***Administration & Security***: AWS Directory Service, AWS Identity & Access Management, AWS Trusted Advisor, AWS Config, AWS CloudTrail, Amazon CloudWatch
***Deployment & Management***: AWS Cloud Formation, AWS OpsWorks, AWS CodeDeploy
***Analytics***: Amazon Kinesis, AWS Data Pipeline, Amazon EMR

##### Foundation Services
***Compute***: Amazon EC2, AWS Lambda
***Storage & Content Delivery***: Amazon CloudFront, Amazon Glacier, AWS Storage Gateway, Amazon Content Delivery
***Database***: Amazon Dynamo DB, Amazon RDS, Amazon Redshift, Amazon Elastic Cache
***Networking***: Amazon Route53, Amazon VPC, Amazon Direct Connect

#### How to Access AWS Resources
* ***Console***: simple web-based user interface (Android, iOS) to access AWS services
* ***CLI***: use to manage AWS resources and automates service management. Mac, Linux, and Windows OS support
* ***SDK***: All major programming languages has compatibility with AWS SDK

##### IAM Users, Group, Role
*IAM service securely control individual and group access to your AWS resources.*
* *IAM User*: individual who has a set of permissions. User has the credentials to make API calls in order to communicate with AWS resources.
* *IAM Group*: collection of IAM users. Users in a group can access the permissions assigned to that group.
* *IAM Roles*: define a set of permissions for making AWS service requests. Roles are basically assigned to the applications.

##### Types of Policy
* *Policies*: are documents that define permissions and are written in JSON.
* *IAM Policies*: specifies those permissions that you want to acquire.
* *Identity-based policy (Permissions Policy)*: policies can be applied to users, groups, and roles. JSON permission policy documents that control what actions an identity can perform, on which resources, and under what conditions.
* *Resource-based policy (Trust Policy)* policies are JSON policy documents that you attach to a resource such as Amazon S3.
* *IAM permissions boundaries*: set the maximum permissions an identity-based policy can grant an IAM entity.
* *AWS Organizations service control policies (SCP)*: specify the maximum permissions for an organization or OU.

```
"Version": "2012-10-17",
"Statement": [
  {
    "Effect": "Allow",
    "Action" "*",
    "Resource": "*"
  }
]
```
*All permissions are implicitly denied by default in AWS*


##### AWS Security Token Service (STS)
Is a web service that enables you to request temporary, limited-privilege credentials for AWS Identity and Access Management (IAM) users or for users that you authenticate.

##### Firewall: NACL & Security Group
A *security group* acts as a virtual firewall for your instances to control inbound and outbound traffic. Five (5) security groups can be assigned to an instance after creating it. Security Groups act at the instance level but not at the subnet level. Only Allow rules can be created in a security group.

A network access control list (ACL) is an optional layer of security for your VPC that acts as a firewall for controlling traffic in and out of one or more subnets. Allow and Deny rules can be created under ACL.

AWS Key Management Service (KMS) makes it easy for you to create and manage cryptographic keys and control their use across wide range of AWS Services and in your applications. AWS KMS is a secured and resilient service that uses hardware security modules that have been validated under FIPS 140-2. It is also integrated with AWS CloudTrail to provide you with logs of all key usage to help meet regulatory and compliance needs.

#### AWS:- Compute Services
##### Amazon EC2 (Virtual Server)
Amazon Elastic Compute Cloud provides scalable computing capacity in the Amazon Web Services Cloud. Amazon EC2 can be used to launch virtual severs, configure security and networking and manage storage. EC2 also enable scaling up or down to handle changes in requirement and spikes.

***Reduce risk***: Durable and secure, avoid risk of physical media handling.

##### Amazon EC2: Instance Types
* ***General Purpose***: M1, M3, M4
* ***Compute Optimized***: C1, CC2, C3, C4
* ***Storage and IO Optimized***: HI1, HS1, I2, I2, D2
* ***GPU Enabled***: CG1, G2
* ***Memory Optimized***: M2, CR1, R3
* ***Smaller instances***: T1, T2

##### Amazon EC2: Purchasing Options
* ***On-Demand Instances***: Pay by the hour (Purchasing Options)
* ***Reserved Instances***: Purchase, at a significant discount instance that are always available. 1 - 3yrs terms. (Purchasing Options)
* ***Scheduled Instances***: Purchase instances that are always available on the specified recurring schedule for a one-year term. (Purchasing Options)
* ***Spot Instances***: Bid on unused instances which can run as long as they are available and your bid is above the SPOT price. (Purchasing Options)
* ***Dedicated Instances***: Pay, by the hour, for instances that run on single-tenant hardware (Tenancy Models)
* ***Dedicated Hosts***: Pay for a physical host that is fully dedicated to running your instances (Tenancy Models)

##### EC2 Placement Groups
* ***Cluster***: packs instances close together inside an Availability Zone. This strategy enables workloads to achieve the low-latency network performance necessary for tight-coupled node-to-node communication that is typical of HPC applications.
* ***Partition***: spreads your instances across logical partitions such groups of instances in one partition do not share the underlying hardware with groups of instances in different partitions. This strategy is typical used by large distributed and replicated workloads, such as Hadoop, Cassandra, and Kafka.

##### Elastic Beanstalk (EBS) & Amazon LightSail
*AWS Elastic Beanstalk (PaaS)*:  is an easy-to-use service for deployment and scaling web applications and services deployed in multiple programming languages and servers such as Apache, Ngnix, Passenger and IIS. EBS automatically handles the deployment, from capacity provisioning, load balancing, auto-scaling to application health monitoring.
*Amazon LightSail*: is an easy to use cloud platform that offers everything needed to build an application or website, plus a cost efficient plan.
* ***EBS*** is scalable, durable, and reliable*

##### ECS, EKS, Fargate
These three (3) services are related to the DevOps Vertical.

| Topics    | Elastic Container (ECS)  |  Elastic Kubernetes Service (EKS) | AWS Fargate (Fargate)|
| :------------ | :--------------- | :----------- | :-------------- |
| Definition | Container Orchestration: By AWS | Managed Kubernetes (Open Source) Platform by AWS | Container on-demand |
| Cluster Creation   | Requires      | Requires       | Not Required      |
| Control Plane Cost | 0, pay for work nodes  | 144 $’, Pay for work nodes | Pay for task based on CPU & Memory  |
| Integration | Deeper Integration with other AWS services | Actively working on Integrations  | Currently runs on ECS  |
| Use Case  | Good for native container architecture | Easy to move on-prem Kubernetes to AWS EKS | Good for workload which runs on duration |

##### AWS Batch
AWS Batch enables developers, scientists, and engineers to easily and efficiently  run hundreds of thousands fo batch computing jobs on AWS.

##### AWS Outpost
Fully managed service that offers the same AWS infrastructure, AWS services, APIs, and tools to virtually any datacenter, co-location space, or on-premise facility or a truly consistent hybrid experience.
- Order
- Install
- Launch
- Build

##### Amazon AMI
Amazon Machine Image provides the information required to launch an instance.
***AMI are region specific***, if you need to use an AMI in another region you can copy an AMI into the destination region via ***Copy AMI***.

##### EC2 MetaData & UserData (Both not encrypted)
***User data*** is data that is supplied by the user at instance launch in the form of a script. Limited to 16KB
* *Windows*: http//169.254.169.254/latest/user-data/ also know as the link local address
* *Linux*: curl http//169.254.169.254/latest/user-data/
***MetaData*** is data about your instance that you can use to configure or manage the running instance
* *Windows*: http//169.254.169.254/latest/meta-data/ also know as the link local address
* *Linux*: curl http//169.254.169.254/latest/meta-data/

##### AWS Lambda (Serverless)
AWS Lambda is a server less compute service that allows you to run code without provisioning or managing servers.
No manual configuration is done on AWS Lambda but rather run or execute anything as a function. The *function* is stored in *memory* and called by a trigger to execute the code.
The results is displayed to the user and after that, the system goes into sleep mode. The client only pays for time that code was executed.
Lambda can be automatically triggered from 140 AWS Services.

### AWS:- Storage Services
#### File Storage
##### Amazon EFS
*Amazon EFS* (Windows OS) is a regional service. It stores data in and across multiple Availability Zones. File Storage for use with Amazon EC2.
The duplicate storage enables you to access data concurrently from all the Availability Zones in the Region where a file system is located. Additionally, on-premises servers can access Amazon EFS using AWS Direct Connect. *It is also Linux based.*
***Agility, Scale***: Reduce time to market, Focus on your business, not your infrastructure.

#### EFS: File (File Storage)
Sharing storage locations which will be accessed by multiple people or EC2 instances. This is specifically used on the Linux machine and this service use a protocol called NFS. EFS allows multiple NFS client across multiple AZ to access a file in an EFS via Multi Target (Specific IP address). EFS is also Region specific. File Storage Server = NFS Protocol + EFS. *EFS is High Availability managed File Storage for Linux machine.*
***Agility, Scale***: Reduce time to market, Focus on your business, not your infrastructure.

#### Block Storage
##### Amazon EC2 (Virtual server)
Amazon Elastic Compute Cloud provides scalable computing capacity in the Amazon Web Services Cloud. Amazon EC2 can be used to launch virtual severs, configure security and networking and manage storage. EC2 also enable scaling up or down to handle changes in requirement and spikes.
##### EBS: Block (Volumes)
Cannot be connected (Cross connection not allowed) from one AZ to another . EBS is AZ specific but multiple block storage can be attached to an EC2 instance in a specific AZ. Multi-attached service can be used in specific AZ to attach an EBS volume to multiple EC2 instances.
****Reduce risk***: Durable and secure, avoid risk of physical media handling.
*Amazon EBS Snapshot*
*Snapshot is Point in Time Replica (PITR) of the volume*.

#### Object Storage
##### Amazon S3
* *S3 Standard* is a storage class that is ideal for frequently accessed data, not archival data. Pay as you go, no upfront investment, no commitment.
* *S3 Intelligent-Tiering* monitors access patterns of objects and automatically moves them between the S3 Standard and S3 Standard-IA storage classes. It is not designed for archival data.
* *S3 Standard-IA* is ideal for data that is infrequently accessed but requires high availability when needed.
* *Objects* stored in the *S3 Glacier* storage class can be retrieved within a few minutes to a few hours. By comparison, objects that are stored in the *S3 Glacier Deep Archive* storage class can be retrieved within 12 hours.

##### S3: Types
###### S3: Simple Storage Service
*Active, frequently assessed data*.
Greater or Equal to 3 AZ
Is a service that is used to store and retrieve any amount of data, at any point of time, from anywhere through internet. Developers usually use S3 as code repositories, where they can save and share the code with encryption and security added on it. The local space created is called Bucket and the item stored in the bucket are called Objects.

###### S3 Intelligent-Tiering
*Data with changing access patterns*.
Greater or Equal to 3 AZ
###### S3 Standard-IA
*Infrequently accessed data*
Greater or Equal to 3 AZ
###### S3 One Zone-IA
*Recreatable, less accessed data*
Equal to 1 AZ
###### S3 Glacier
*Archive data*
Greater or Equal to 3 AZ
###### S3 Glacier Deep Archive
Long-term archive-data
Greater or Equal to 3 AZ
*Economical*: Pay as you go, No upfront investment, No commitment.
#### Amazon Glazier
*Amazon S3 Glacier* is a secure and durable service for low-cost data archiving and long-term backup. For infrequently accessed data. Self service administration, SDK for 	simple integration.
***Easy to Use***: Self service administration, SDKs for simple integration.

#### Amazon FSx for Windows File Server
Fully managed Windows file servers for business applications. Windows server with native support for Windows file system features.
Use the SMB Protocol. Provide File Storage that is accessible from Windows, Linux and MacOS compute instances and devices running on AWS or on-premises.
* Integration with Active Directory
* Offers Single-AZ and Multiple-AZ deployment, SSD and HDD storage
* File systems are encrypted
* Fully managed backups
* File system can dynamically scale to fit storage throughput needs

#### Amazon FSx for Lustre
Fully managed Lustre file system for compute-intensive workloads. Open source parallel file system. High intensive and high computing.
* Use it for workloads where speeds matters - Machine learning, HPC, video processing, financial modeling
* POSIX compliant
* Can be used with Amazon Sage Maker, Amazon Elastic Kubernetes and AWS Parallel Cluster Accessible from on-premises over Direct Connect and VPN connections.

#### AWS Storage Gateway
Is a hybrid cloud storage service that gives a user on-premise access to virtually unlimited cloud storage. Customers use Storage Gateway to simplify storage management and reduce costs for key hybrid cloud storage use cases. These include moving backups to the cloud, using on-premises file share backed by cloud storage and providing low latency access to data in AWS for non-premises applications. Communication is encrypted.

#### Data Transfer
* *Snowball* is a form of storage service. Customer moves on-premise data to the snowball and mail it back to AWS to be on S3 bucket
* *Amazon FSX*(Linux OS)*: 	

## AWS:- Networking Services
### 1. Virtual Private Cloud
VPC helps to isolate your infrastructure from the rest of the world and keep it secured and safe inside your control. ***VPC*** should be inside a ***Region*** and a ***subnet*** is created inside a ***VPC*** and that is where the EC2 instances are created.
##### Amazon creates;
- Default **VPC**
- Default **Subnets**
- Default **Routing Table**
- Default **Internet Gateway**
based on the region selected.
**Internet Gateway** is a horizontally scaled redundant, and highly available VPC component that allows communication between your VPC and the internet.
**NAT device** allows instances in private subnets to connect to the internet, other VPCs, or on-premises networks. These instances can communicate with services outside the VPC but they cannot receive unsolicited connection requests.

### 2. Firewall: Security Group & Network Access Control Lists
**Firewall** is a special network device that creates policies in it and these policies defines what traffic can come inside and leave the security boundary.
**Security Groups** acts as a firewall for associated Amazon EC2 instances, controlling both inbound and outbound traffic at the *instance level*.
* **EC2** can be attached up to 8 SG and SG can also be attached to multiple machines*.
* **Network Access Control Lists** is an optional layer of security for your VPC that acts as a firewall for associated subnets, controlling both inbound and outbound traffic at the subnet level. *Only one subnet can be attached to one NACL*.

### 3. Virtual Private Network
Single Site-to-Site (PTP)
Multiple Site-to-Site (PTMP)

### 4. AWS Direct Connect
Is a cloud service solution that makes it easy to establish a dedicated network connection from your premises to AWS. Private connection between AWS and your datacenter, office or colocation environment can be done using AWS Direct Connect.

### 5. VPC Peering
Cloud to cloud connection. VPC can be in the same of different region and they can also have different or same account.

### 6. AWS Transit Gateway
Connects VPCs and on-premises network through a central hub. This simplifies network and puts an end to complex peering relationships. It acts as a Cloud Router - each new connection is only once.

### 7. AWS Bastion Host (Hop station)
A server whose purpose is to provide access to a private network from an external network, such as the internet.

### Load Balancer, AutoScaling, CloudFront, Direct Connect, & Route 53
* High Availability: Has minimum loss of service. Use a Load Balancer to achieve HA.
* Application Load Balancer: when you need a flexible feature set for your web applications with HTTP and HTTPS traffic. Layer 7 (Application Layer)
* Network Load Balancer: when you need ultra-high performance, TLS offloading at scale, centralized certificate deployment, support TCP/UDP, and static IP addresses for your application.
* Gateway Load Balancer: when you need to deploy and manage a fleet of third-party virtual applications that support GENEVE. These appliance enable you to improve security, compliance, and policy controls. Uses the IP address for Load Balancing.
* Classic Load Balancer: when you have an existing application running in the EC2-Classic network. No more use.
* Fault Tolerance: Has loss of service when the primary host goes down.
* AutoScaling: Automatic monitoring, using alerts when there is a rise in the utilization of the initial servers.
* AutoScaling with LB: Elastic Load Balancing automatically distributes your incoming application traffic across all the EC2 instances that you are running. Elastic Load Balancing helps to manage incoming requests by optimally routing traffic so that no one instance is overwhelmed.
* CDN: CloudFront: is a fast content delivery network (CDN) service that securely delivers data, videos, applications, and API to customers globally with low latency, high transfer speeds, all within a developer-friendly environment. Delivers the content through edge location.
* AWS Direct Connect: is a cloud service solution that makes easy to establish a dedicated network connection from on-prem to AWS. Private connectivity between AWS and the on-prem datacenter, office and colocation environment can be established. This reduces network costs and increase bandwidth throughput.

#### Amazon Route 53:
* Simple Routing Policy
* Weighted Routing Policy
* Latency Routing Policy
* Failover Routing Policy
* Geo-Location Routing Policy
* Multivalued Routing Policy

## AWS:- Databases
Database is a collection of individual data items which is stored in a highly structured manner.
### Types of AWS Database Services
- Relational (Amazon Aurora, Amazon RDS)
    * Referential Integrity
    * ACID transactions
    * Schema-on-write
    * Lift and Shift
    * ERP
    * CRM
    * Finance

- Key-value (DynamoDB)
    * High throughput
    * Low latency read and writes
    * Endless scale
    * Real-time bidding
    * Shopping cart
    * Social
    * Product catalog
    * Customer preferences

- Document (DocumentDB)
    * Store documents and quickly
    * Access querying on any attribute
    * Content management
    * Personalization
    * Mobile

- In-Memory (ElastiCache)
    * Leaderboards
    * Real-time analytics
    * Caching

- Graph (Neptune)
    * Quickly and easily create and navigate relationships between data
    * Fraud detection
    * Social networking
    * Recommendation engine

- Time-series (Timestream)
    * Collect, store, and process data sequenced by time
    * IoT applications
    * Event tracking

- Ledger (QLDB)
    * Complete, immutable, and verifiable history of all changes to application data
    * System of record
    * Supply chain
    * Health care
    * Registration
    * Financial

- Wide Column (Keyspaces - managed Cassandra)
    * Scalable
    * Highly available and managed Apache Cassandra - compatible service
    * Build low-latency applications
    * Leverage open source
    * Migrate Cassandra to the cloud

### Amazon RDS
* RDMS which manages relational database for users
* Supports MySQL, PostgreSQL, Oracle, SQL servers
* Role is to look after software patching, updates, backups, recovery and automatic failure detection.
* Pay per use
* Backup can be created via Amazon Snapshot or automated backup
* Used to manage data of E-Commerce, Gaming, Apps, Websites
* Simple and fast deploy and scale
* Amazon Aurora (better performance, secured, high availability) using  PostgreSQL and MySQL

### DynamoDB
**DynamoDB** provides DynamoDB Accelerator (DAX) which is a fully managed, highly available in-memory cache. This will help us speed up the performance of the data retrieval that we require. DynamoDB also has a feature called DynamoDB streams that enables real-time capture of data changes using event notifications. This helps applications to perform analytics on real-time streaming data to build dashboards without impacting database performance. The stream events are asynchronous in nature to consuming applications like a Lambda function. Since the Customer’s transactional data is highly confidential & huge in volume, a robust, scalable, secure, performant data store like DynamoDB will be the best fit for our scenario.
* Fully managed NoSQL database service offered by AWS
* The record in every row is called an Item.
* TTL can be set to automatically delete items in the table once they expire.
* Operations such as CREATE, INSERT, UPDATE, QUERY, SCAN and DELETE are performed in a table via appropriate API.

**Questions:**
business critical application
Cloud-native application they seek to use fully managed services to increase agility, reduce time to market, and  minimize operational overhead
Key-value
RDS
DynamoDB
ElastiCache

### DynamoDB API
##### Data Plane:
Lets you perform CRUD action on data in a table.
- Creating Data:  PutItem, BatchWriteItem
- Reading Data: GetItem, BatchGetItem
- Updating Data: UpdateItem
- Deleting Data: DeleteItem, BatchWriteItem

##### Control Plane:
Lets you create and manage DynamoDB	table.
- Create Table: create a table which includes table name, primary key, throughput settings
- Describe Table: used to view the details of table
- Update Table: used to modify settings of table
- Delete Table: used to remove unused table
- List Table: used to return the name of DynamoDB table for the current AWS account and region
- Describe Limits: returns the current read and write capacity limits for the current AWS account and region.

### DynamoDB Streams
Is used to replicate the data from a table to table in other region.
API’s used are:
- List Stream: retrieves a list of stream descriptors for the current account and endpoint
- Describe Stream: retrieves detailed information about a given stream
- Get  Shared Iterator: retrieves shared iterator, which describes a location within the shared
- Get Records: retrieves the stream records within a given shared

### Difference between SQL and NoSQL
| Characteristics   |      SQL           |     NoSQL         |
| :---------------- | :----------------- | :---------------- |
| Workloads   | Adhoc queries, data warehousing, OLAP  |  Web-scale applications   |
| Data Model  | Well defined schema where data is normalized into tables, rows and columns  | Schema-less with a primary key and manages structured or semi-structured data  |
| Data Access | SQL | AWS Management Console or AWS CLI and perform adhoc tasks   |
| Performance   | Optimized for storage   | Optimized for compute    |
| Scaling    | Vertical Scaling          | Horizontal scaling (cluster of DBs)   |

## AWS:- Automation & Configuration Management
Is a IaC spectrum and open source
AWS CloudFormation gives you an easy way to model a collection of related AWS and third-party resources, provision them quickly and consistently, and manage them throughout their lifecycles, by treating infrastructure as code.
CloudFormation template describes your desired resources and their dependencies - making the launch and configuration together as a stack.

AWS OpsWorks is a configuration management service that provides managed instance of Chef and Puppet. Chef and Puppet are automatic platforms that allow you to use code to automate the configuration of your servers, including deployment, and management across Amazon EC2 instances or on-premise compute environment. OpsWorks lifecycle include;
* Setup: occurs after a started instance complete booting
* Configure: occurs when an instance enters or leaves online state
* Deploy: occurs when a deploy command is run
* Undeploy: occurs when you delete an app to remove an app from a set of application server instances
* Shutdown: occurs before the associated EC2 instances is actually terminated.

## AWS:- Audit & Monitoring
* **AWS CloudTrail:** helps to track user activity and API usage which allows for operational and risk auditing of your AWS infrastructure.
	[] * Monitoring and auditing of IT infrastructure for compliance
	* Log and monitor account activities and even history
	* Simplify compliance audits
	* Discovery/troubleshoot security and operational issues
	* Provide visibility into user/resources activities
	* Automatically respond to security threats.
	* Deliver reports to S3 buckets or CloudWatch logs and events
	* Track user activities and API requests throughout your AWS infrastructure
	* Filter logs to assist with operational analysis and troubleshooting
 When enabled, CloudTrail Insights. This optional feature allows CloudTrail to automatically detect unusual API activities in your AWS account. 
Amazon CloudWatch: is a service used in monitoring and management system for AWS infrastructure. Integrated with over 70 AWS service and helps in gaining system wide visibility into resource utilization, application performance, and operational health.
	* Gain system-wide visibility into resources utilization, application performance, and operational health
	* Collect monitoring and operational data as logs, metrics, and events
	* Provides insights into application performance
	* Reduce MTTR and improve TCO.
With CloudWatch, you can create alarms that automatically perform actions if the value of your metric has gone above or below a predefined threshold. 
The CloudWatch dashboard feature enables you to access all the metrics for your resources from a single location. For example, you can use a CloudWatch dashboard to monitor the CPU utilization of an Amazon EC2 instance, the total number of requests made to an Amazon S3 bucket, and more.
AWS Trusted Advisor is a web service that inspects your AWS environment and provides real-time recommendations in accordance with AWS best practices. Categories include Performance and Fault tolerance.

## AWS:- Application Services SNS, SES, SQS, & SWF
### Amazon Simple Notification Service (Amazon SNS)
Is a fully managed messaging service for both application-to-application (A2A) and application-to-person (A2P) communication.
* A2A pub/sub functionality provides topics for high-throughput, push-based, many-to-many messaging between distributed systems, micro servers and event-driven sever less applications.
* A2P functionality enables you to send messages to users at scale via SMS, mobile push, and email.

### Amazon Simple Email Service (SES)
Is a cost-effective, flexible, and scalable email service that enables developers to send mail from within any application.
### Amazon SWF
Helps developers build, run, and scale background jobs that have parallel or sequential steps. Also known as a fully managed state tracker and task coordinator in the cloud.

## AWS:- DevOps Tools
### AWS CodeCommit
Is a fully-managed source control service that hosts secure Git-based repositories. Helps team to collaborate on code in a highly scalable ecosystem. Eliminates the need to operate your own source control system.

### AWS CodeBuild
Is a fully managed continuous integration service that compiles source code, runs tests, and produces software packages that are ready to deploy. No need to provision, manage, and scale your own servers so it scales continuously  and processes multiple builds concurrently.

### AWS CodeDeploy
Is a fully managed deployment service that automates software deployments to a variety of compute services such as Amazon EC2, AWS Fargate, AWS Lambda, and your own on-premises server.

### AWS CodePipeline
Is a fully managed continuous delivery service that helps you automate your release pipelines for fast and reliable application and infrastructure updates. It automates the build, test, and deploy phases of your release process every time there is a code change, based on the release modem you define.
* Source
* Build
* Test
* Staging
* Production

**AWS CodeStar** is a cloud-based development service that provides the tools you need to quickly develop, build, and deploy application on AWS.

## AWS:- Security
### Shared Responsibility Model
AWS **controls the security of the cloud** and the **customer controls the security in the cloud**.
￼
#### Customers: Security in the cloud
Customers are responsible for the security of everything that they create and put in the AWS Cloud.
When using AWS services, you, the customer, maintain complete control over your content.
You are responsible for managing security requirements for your content, including which content you choose to store on AWS, which AWS services you use, and who has access to that content.
You also control how access rights are granted, managed, and revoked.
 
The security steps that you take will depend on factors such as the services that you use, the complexity of your systems, and your company’s specific operational and security needs.
Steps include;
    * Managing user accounts
    * Configuring security groups
    * Selecting, configuring, and patching the operating systems on Amazon EC2 instances
    * Patching software on Amazon EC2 instances
    * Setting permissions for Amazon S3 objects
    * Firewall and network configuration

**Data**:
***Encryption at Rest***
    * Client Side Encryption
    * Server Side Encryption

***Encryption in Transit***
    * Device to the website
    * Encrypted and then it will be sent on internet - SSL Certificate

#### AWS: Security of the cloud
AWS is responsible for security of the cloud.
AWS operates, manages, and controls the components at all layers of infrastructure.
This includes areas such as the host operating system, the virtualization layer, and even the physical security of the data centers from which services operate. 
AWS is responsible for protecting the global infrastructure that runs all of the services offered in the AWS Cloud.
This infrastructure includes AWS Regions, Availability Zones, and edge locations.
 
AWS manages the security of the cloud, specifically the physical infrastructure that hosts your resources, which include:
    * Physical security of data centers
    * Hardware and software infrastructure
    * Network infrastructure
    * Virtualization infrastructure
    * Maintaining network infrastructure
    * Implementing physical security controls at data centers
    * Maintaining servers that run Amazon EC2 instances
    * Protecting infrastructure (hardware, software, facilities, and networking)

Although you cannot visit AWS data centers to see this protection firsthand, AWS provides several reports from third-party auditors.
These auditors have verified its compliance with a variety of computer security standards and regulations.

### AWS Identity & Access Management
Securely manage identities and access to AWS services and resources. Also used to specify who or what can access services and resources in AWS.
IAM is uded to manage and scale workload and workforce access securely supporting your agility and innovation in AWS.
    * Preventive security control
    * Create and manage AWS users and groups
    * Use permissions to allow and deny access to AWS resources
    * Controls both centralized and fine grained-API resources and manage console
*** IAM deals with **Users**, **Groups**, **Roles** and **Policies**

#### IAM Components
> ##### IAM User (Sub Account)
**Root user** has a username and password. Example name@company. For best practices, the root account should not be used unless it is an emergency
**IAM user** has acccount id, username and password and they can have access to the root account.
    * User gets an Access key ID and Secret access key for API connects to AWS CLI.
    * User can have access to files in an S3 bucket
**Select AWS Access Type**
Selects how users will primarily access AWS
    * Access key - Programmatic access (Enables an ***access key ID*** and ***secret access key*** for the AWS API, CLI, SDK and other development tools)
    * Password - AWS Management Console access (Enables a ***password*** that allows users to sign-in to the AWS Management Console)
    * Console password - Autogenerated and Custom password
**Set Permissions**
    * Add users to group
    * Copy permissions from exiting user
    * Attach existing policies directly

> ##### IAM Group
An IAM user group is a collection of IAM users. User groups let you specify permissions for multiple users, which can make it easier to manage the permissions for those users.
    * Permissions can be assigned and users automatically get the same permissions.
    * A user group can contain many users, and a user can belong to multiple user groups.
    * User groups can't be nested; they can contain only users, not other user groups.
    * Policy name is used in assigning Permissions to Users or Groups

> ##### IAM Policies
An object in AWS that defines permissions or set of rules. For customized policies, you need to create or edit **JSON** file or use a **Visual editor** for the policies that need to be assigned.
Example: **AdministratorAccess** allows a group or user to have access to everything.
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "*",
            "Resource": "*"
        }
    ]
}
```

> ##### IAM Roles
An IAM role is an **IAM identity** that you can create in your account that has specific permissions.

##### IAM Best Practices
    * Grant least privileges
    * Manage permission with Groups
    * Restrict privileges access furter with conditions
    * Always enable AWS CloudTrail to be aware of API call logs.

##### IAM Delegation & Audit
    * Use IAM Roles along with Amazon EC2
    * Use Roles to share access
    * Try to reduce or better remove root use
**AWS managed policy can be applied to a group**
**Inline policy is used to add permissions to a specific user or specific group, hence the Group inline policy is used**.
**Permission boundary is used to control the maximum permissions a user can have.**

### AWS Account, Users and Service Scope
AWS Account (IAM User) = [Global] [Billing] [IAM] [Route 53]
Region_1 Region_2      = [S3] [DynamoDB] [VPC] [ELB]
AZ_1 AZ_2              = [EC2] [RDS] [EBS]

### AWS Organizations 
To consolidate and manage multiple AWS accounts within a central location.
In AWS Organizations, you can centrally control permissions for the accounts in your organization by using service control policies (SCPs). SCPs enable you to place restrictions on the AWS services, resources, and individual API actions that users and roles in each account can access.
    * Global service
    * Allow to manage multiple AWS accounts
    * Main account is the **Management account**
    * Member accounts can only be part of one organization
    * Consolidated Billing across all accounts
    * Pricing benefits
    * Shared reserved instances and Savings Plans discounts
    * API available to automate AWS account creation.
#### Advantages
    * Multi-Account vs One Account Multi VPC
    * Use tagging standards for billing purposes
    * Enable CloudTrails on all accounts, and send logs to the central S3 account
    * Send CloudWatch logs to the central logging account
    * Establish Cross Account Roles for Admin purposes
#### Security: Service Control Policies (SCP)
    * IAM policies applied to OU or Accounts to restrict Users and Roles
    * SCP do not apply to the managemen account
    * Explicit allow is a must if specific permission needs to be given
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowsAllActions",
      "Effect": "Allow",
      "Action": "*",
      "Resource": "*"
    }
    {
      "Sid": "DenyDynamoDB",
      "Effect": "Deny",
      "Action": "dynamodb:*",
      "Resource": "*"
    }
  ]
}
```
#### Amazon Cognito
Implement secure, frictionless customer identity and access management that scales.
Amazon Cognito provides an identity store that scales to millions of users, supports social and enterprise identity federation, and offers advanced security features to protect your consumers and business.
    * Deliver frictionless customer identity and access management (CIAM) with a cost-effective and customizable platform.
    * Add security features such as adaptive authentication, support compliance, and data residency requirements.
    * Scale to millions of users with a fully managed, high-performant, and reliable identity store.
    * Federate sign-in using OIDC or SAML 2.0 and connect to a broad group of AWS services and products.

##### AWS Cognito User Pools (CUP)
    * Create serverless database of user for your mobile apps
    * Simple login: Username (or email)/password combination
    * Possibility to verify emails/phone numbers and add MFA
    * Can enable Federated Identities (Facebook, Google, SAML)
    * Sends back a JSON Web Token (JWT)
    * Can be integrated with API Gateway for authentication



### AWS Artifact 
Is a service that provides on-demand access to AWS security and compliance reports and select online agreements. AWS Artifact consists of two main sections: AWS Artifact Agreements and AWS Artifact Reports.

### AWS Shield
AWS Shield is a service that protects applications against DDoS attacks. AWS Shield provides two levels of protection: Standard and Advanced.
A denial-of-service (DoS) attack is a deliberate attempt to make a website or application unavailable to users.

### AWS Shield Advanced
AWS Shield Advanced is a paid service that provides detailed attack diagnostics and the ability to detect and mitigate sophisticated DDoS attacks. 

### AWS Key Management Service (AWS KMS)
Enables you to perform encryption operations through the use of cryptographic keys. A cryptographic key is a random string of digits used for locking (encrypting) and unlocking (decrypting) data. You can use AWS KMS to create, manage, and use cryptographic keys. You can also control the use of keys across a wide range of services and in your applications.

#### AWS Key Management Service
AWS KMS makes it easy for you to create and manage cryptographic keys and control their use across a wide range of AWS Services in your applications.
    * AWS KMS is secured and resilient service that uses hardware security modules that have been validated under FIPS 140-2
    * Primary key of AWS KMS is to encrypt the data when the data is at rest.
    * Storage can be on a Block or File storage
    * Integration with CloudTrail, hence provides logs of all key usage and help meet regulatory and compliance needs.
    * Two types of keys are used - CMK (Custom Managed Keys) and AWS Managed Keys

### AWS WAF
Is a web application firewall that lets you monitor network requests that come into your web applications. AWS WAF works together with *Amazon CloudFront* and an *Application Load Balancer*. Recall the network access control lists that you learned about in an earlier module. AWS WAF works in a similar way to block or allow traffic.

### Amazon Inspector
Amazon Inspector helps to improve the security and compliance of applications by running automated security assessments. To perform automated security assessments, they decide to use Amazon Inspector.

### Amazon GuardDuty
Is a service that provides intelligent threat detection for your AWS infrastructure and resources. It monitors for malicious activity and unauthorized	behavior to protect your AWS account, workloads and data stored in Amazon S3.

### AWS Secret Manager
Helps to protect secrets needed to access your application, services and IT resources. This enables you to easily *rotate*, *manage*, *retrieve database credentials*, *API Keys*, and other secrets throughout their lifecycle.

### AWS IAM Role
An IAM role is an IAM identity that you can create in your account that has specific permissions and also assign to an AWS service. E.g EC2

### Policy Types
>Identity-based policies –
Attach managed and inline policies to IAM identities (users, groups to which users belong, or roles). Identity-based policies grant permissions to an identity.

>Resource-based policies –
Attach inline policies to resources. Resource-based policies grant permissions to the principal that is specified in the policy. Principals can be in the same account as the resource or in other accounts.

>Permissions boundaries –
Use a managed policy as the permissions boundary for an IAM entity (user or role). That policy defines the maximum permissions that the identity-based policies can grant to an entity, but does not grant permissions. Permissions boundaries do not define the maximum permissions that a resource-based policy can grant to an entity.

>Organizations SCPs –
Use an AWS Organizations service control policy (SCP) to define the maximum permissions for account members of an organization or organizational unit (OU). SCPs limit permissions that identity-based policies or resource-based policies grant to entities (users or roles) within the account, but do not grant permissions.

>Access control lists (ACLs) –
Use ACLs to control which principals in other accounts can access the resource to which the ACL is attached. ACLs are similar to resource-based policies, although they are the only policy type that does not use the JSON policy document structure. ACLs are cross-account permissions policies that grant permissions to the specified principal. ACLs cannot grant permissions to entities within the same account.

>Session policies –
Pass advanced session policies when you use the AWS CLI or AWS API to assume a role or a federated user. Session policies limit the permissions that the role or user's identity-based policies grant to the session. Session policies limit permissions for a created session, but do not grant permissions.

### Permissions
* Add Permissions
* Add Inline Policy

### AWS Power User
A Power user can have access to every service but limited to IAM.

## AWS:- Pricing and Support
AWS Partner Network: is the global community of Partners who leverage Amazon Web Services to build solutions and services to customers.
- Build, market, and sell with AWS Partner Network
- Build AWS expertise
- Gain go-to-market support
- Collaborate and co-sell with AWS Sales

### AWS Pricing Model
Partial Upfront - Pay as you go
All Upfront - Pay less when you reserve
Pay even less per unit by using more

## AWS:- Five Pillars of the Well-Architected Framework
	- Operational Excellence: run, manage, and monitor production workload to deliver business value and continuous improvement on support process and events
	- Security: protecting information systems and assets from outside world with risk assessment, unplanned failures and mitigation strategies
	- Reliability: auto recover workload from infrastructure, power or system failures with dynamic resource management to meet operational threshold
	- Performance Efficiency: use computing resources efficiently to support on demand changes for delivering workload with maximum performance to meet the SLA
	- Cost Optimization: avoid and eliminate unnecessary cost or replace resources with cost-effective resources without impacting the best practices and business needs.

### Concepts Of Well Architected Framework
* Resiliency: is the ability to recover from disruptions and mitigate disruptions. HA of your infrastructure.
* Consistency: involves more than one system storing information, to return the same result when queried. Consistent performance.
* Durability: is the  system’s ability to perform even upon the occurrence of unexpected events. Able to tolerate unexpected events
* Latency: is typically the measure of delay between request and response. Create services to be closer to your users

Three (3) Tiers of Architecture
* Web
* Application
* Database

### AWS Marketplace
Is a digital catalog that includes thousands of software listings from independent software vendors. 
￼
