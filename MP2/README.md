# Programming Assignment: Machine Problem 2: AWS Load Balancer
**1. Overview**

AWS Elastic Load Balancing (ELB) spreads user traffic across many instances of your applications. A load balancer decreases the possibility of performance issues in your applications by distributing the load. It also helps with the reliability and scalability of your product, which may be running on several virtual machines. AWS EC2 enables you to create virtual machines on AWS infrastructure that run various operating systems, including multiple flavors of Linux, Windows Server, and macOS.

In this MP, we will launch a load balancer to balance requests between 2 web servers hosted on Amazon EC2. 

**2. Requirements**

You need to use the terminal or command prompt on your computer to ssh into the AWS instances. For Mac and Linux users, ssh is already available in the terminal. For Windows users, you can install and use PuTTY.

**3. Procedure**

**Step 1: web application on AWS EC2**

Launch two identical EC2 instances. We suggest using the latest Amazon Linux AMI as the operating system and the smallest EC2 instance possible (e.g., Nano or Micro) to make the cost of your instances as small as possible (or free.) Refer to the link below for the specific steps. 

https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html

Ensure you can connect to the 2 EC2 instances using terminal (or the embedded terminal in the EC2 console on your browser) via ssh.
You must now write a simple web server application that stores and retrieves a seed value (default 0). This program will then run on each EC2 server. Specifically, your server should maintain the seed number and allow clients to access and update it. The application handles the following two HTTP REST requests:

HTTP POST "/" with JSON body {"num": 100} where 100 can be any integer.

Your program should update the seed value with the given number.

HTTP GET "/"
 
Your program should return the integer seed value in string format. The response body for the above case will be: "100"

The web application will run on a specific port and be deployed in both EC2 instances. 

To access the servers publicly and make them reachable for the load balancer, you need to set an inbound firewall rule on the EC2 instances.

You can use your preferred programming languages or development environments to implement this server. However, we will only assist you with Python using Flask. You need to install the required dependencies (install pip and then Flask along with its required dependencies if you are using Python) in both EC2 instances and then start the server. Refer to the sections of Environment and HTTP Methods in Tutorialspoint's Flask tutorial for more details.

**Step 2: load balancing web servers**

You will launch an AWS Application Load Balancer, which will allow you to distribute HTTP requests between the two instances you just initiated. To get started, you might want to look at the following document. 
https://docs.aws.amazon.com/elasticloadbalancing/latest/application/application-load-balancer-getting-started.html

Connect your load balancer to a target group with the previously launched EC2 instances. Make sure to map the webserver port to the load balancer correctly.

When configuring the load balancer, ensure not to use the default security group. Enable the HTTP protocol and allow traffic to be routed from anywhere when creating a custom security group. You will not pass this assignment unless our autograder can connect to your system via the internet.

To make the server code operate in the load balancer, you must edit the target group's health check ping path to "/".

To check if your load balancer is running correctly, first make sure that the two EC2 instances are healthy in the target group, and then go to the DNS address listed in the AWS load balancer's description and look for the seed value.

If you encounter any other issues, use Google Search, AWS documentation, or Campuswire. 

**Step 3: how to submit your assignment**

Edit the variable payload in test.py (see the attached file below) and add relevant connection information. You can get your submission token from this page. Look at the section like the below example at the bottom of this assignment page:


Run test.py on your local machine (or any of the two EC2 instances). You will receive the autograder's feedback for the current submission, and your grade on Coursera will be updated automatically.

**Step 4: shutdown all AWS services**

Make sure to shutdown your EC2 instances. Otherwise, Amazon will keep charging you!
