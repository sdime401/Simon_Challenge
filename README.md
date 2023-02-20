SED Challenge Answers: 

Infrastructure

Even though I could have used Ansible which is a configuration management tool to deploy the instance, based on the requirement I have opted to use CloudFormation instead, which is an infrastructure as code (IaC) tool to provision my resources. Even though many today consider both Ansible and CloudFormation as IaC, they shine in two different ways. Ansible will be powerful when it comes to configuration management on nodes, while CloudFormation would shine when it comes to provision resources. 
For the remainder of the challenge, I will be using CloudFormation to provision the webserver that will serve the static content. 

To secure the application, I have created an application Load Balancer security group resource that will accept requests from customers only on ports 80 and 443(HTTP and HTTPS respectively). The load balancer will in this case forward traffic to available resources in the target group that was created. Then I forwarded HTTPS requests from the load balancer to the target resource I have created. HTTP will be redirected to HTTPS. An SSL certificate was then requested through AWS Certificate Manager for a domain that I own(myaws2022lab.com). 

A record is created in Route 53 hosted zone to point to the application load balancer resource previously created. 

Develop and Apply Automated tests Develop and apply automated tests to validate the correctness of the server configuration.

For this part, I built a full CI/CD pipeline that would automatically build, test, and deploy the CloudFormation template to a test environment.

Process: 
- push app code to GitHub, which is our code repository
- At the build stage, I use CodeBuild to build the CloudFormation template and test it
- Deploy the template to the test environment with CodeDeploy(us-east-1)

For the build stage, AWS Codebuild launches a docker instance in the backend that will allow you to run your buildspec (commands that will be passed to the app). CFN-LINT or YAMLINT could be used for the CloudFormation template validation. I have used CFN-LINT for this project. 

Part 2 Coding Challenge(Open the following pythonfile: Simon_Code_Challenge.py:

  The code verifies whether credit card numbers are valid or not based on certain requirements. The Docstring present in the function gives an overview of what the function will do and paramaters that comes into play.


