import streamlit as st
import streamlit.components.v1 as components


st.markdown("""
### Problem Statement: Open Weather Challenge

The goal of this challenge is to design and implement a service that fetches daily weather forecast data for a specified location and sends it via email to users. The solution should integrate the Weather API provided by OpenWeather to retrieve forecast information based on latitude and longitude and leverage cloud services to create a scalable and efficient system.

### Requirements:
1. **Weather Data**: Use the OpenWeather API to fetch the latest weather forecast for a given location (specified by latitude and longitude).
2. **Email Notification**: Send the fetched weather forecast as an email to the intended recipients.
3. **Implementation Language**: Develop the solution using Python for both fetching weather data and sending emails.
4. **Cloud Services**: Incorporate AWS or GCP services for any additional infrastructure needs, ensuring scalability, reliability, and cost-effectiveness.
5. **Documentation**: Provide clear documentation of the design and implementation, including steps to set up and run the service.

### Key Deliverables:
1. **Python Scripts**: Code for fetching weather data from the OpenWeather API and sending emails.
2. **Cloud Architecture**: Recommendations and/or implementation of cloud services (AWS or GCP) used to support the service, such as:
   - Task scheduling (e.g., AWS CloudWatch, Google Cloud Scheduler).
   - Serverless computing (e.g., AWS Lambda, Google Cloud Functions).
   - Email service integration (e.g., AWS SES, SMTP).
3. **Design Documentation**: A detailed explanation of the architecture, dependencies, and steps to deploy and execute the solution. 

### Objective:
Deliver a robust and scalable solution that ensures daily weather forecasts are sent reliably via email, meeting the specified constraints and requirements.

""")

st.markdown("""------""")

st.title("Architecture Diagram for Weather Alert System")
with open("./src/WeatherForecast.txt", "r") as file:
   html_content = file.read()
components.html(html_content, width=800, height=600, scrolling=True)
st.markdown("""------""")
st.title("Another solution using snowflake notebook ")
st.markdown(""" With snowflake we can schedule the notebook to run at specific time and send the email to the users. Below is the schedule for the same.""")
st.image("./src/Snowflake_Notebook_Schedule.JPG")

st.markdown("""------""")
st.title("DevOps Pipeline for Weather Alert System")

def render_mermaid_diagram():
    st.subheader("VPC Architecture Diagram")
    mermaid_code = """
    flowchart TD
        subgraph VPC
            IGW[Internet Gateway]
            subgraph PublicSubnets[Public Subnets]
                NAT[NAT Gateway]
                ALB[Application Load Balancer]
            end
            subgraph PrivateSubnets[Private Subnets]
                Lambda[Lambda Functions]
                ApiGW[API Gateway]
            end
            subgraph SecurityGroups[Security Groups]
                ALBSG[ALB Security Group]
                LambdaSG[Lambda Security Group]
            end
        end
        
        Internet((Internet)) --> IGW
        IGW --> ALB
        ALB --> ApiGW
        ApiGW --> Lambda
        Lambda --> NAT
        NAT --> IGW
    """
    st.markdown(f"```mermaid\n{mermaid_code}\n```", unsafe_allow_html=True)

# Function to render Terraform configuration files
def render_terraform_files():
    st.subheader("Terraform Configuration Files")

    # Display providers.tf
    st.text_area("providers.tf", """
    provider "aws" {
      region = var.aws_region
    }

    terraform {
      required_version = ">= 1.0"
      required_providers {
        aws = {
          source  = "hashicorp/aws"
          version = "~> 5.0"
        }
      }
      backend "s3" {
        # Configure your backend here
      }
    }
    """, height=200)

    # Display variables.tf
    st.text_area("variables.tf", """
    variable "aws_region" {
      description = "AWS region to deploy resources"
      type        = string
      default     = "us-west-2"
    }

    variable "environment" {
      description = "Environment name"
      type        = string
      default     = "dev"
    }

    variable "vpc_cidr" {
      description = "CIDR block for VPC"
      type        = string
      default     = "10.0.0.0/16"
    }
    """, height=200)

    # Display vpc.tf
    st.text_area("vpc.tf", """
    resource "aws_vpc" "main" {
      cidr_block           = var.vpc_cidr
      enable_dns_hostnames = true
      enable_dns_support   = true

      tags = {
        Name        = "${var.environment}-vpc"
        Environment = var.environment
      }
    }

    resource "aws_internet_gateway" "main" {
      vpc_id = aws_vpc.main.id

      tags = {
        Name = "${var.environment}-igw"
      }
    }
    """, height=200)


def render_deployment_steps():
    st.subheader("Deployment Steps")

    st.write("""
    1. **Initialize Terraform**:
    ```bash
    terraform init
    ```
    
    2. **Plan the deployment**:
    ```bash
    terraform plan -out=tfplan
    ```
    
    3. **Apply the configuration**:
    ```bash
    terraform apply tfplan
    ```
    """)

# Function to list key design choices
def render_design_choices():
    st.subheader("Key Design Choices")

    st.write("""
    - **Networking**:
      - VPC with public and private subnets across 2 AZs
      - NAT Gateway for private subnet internet access
      - Proper route tables and internet gateway configuration

    - **Security**:
      - Lambda functions in private subnets
      - Minimal security group rules
      - IAM roles with least privilege

    - **Scalability**:
      - Multi-AZ setup for high availability
      - Serverless architecture for automatic scaling
      - API Gateway for request management
    """)

# Function to list post-deployment tasks
def render_post_deployment():
    st.subheader("Post-Deployment")

    st.write("""
    - Update Lambda function code via CI/CD pipeline
    - Configure API Gateway methods and integrations
    - Set up monitoring and logging
    """)

# Function to display best practices
def render_best_practices():
    st.subheader("Best Practices")

    st.write("""
    - Use workspace for different environments
    - Implement proper tagging strategy
    - Use remote state with state locking
    - Encrypt sensitive data
    - Use variables for reusability
    """)


render_mermaid_diagram()


render_terraform_files()

render_deployment_steps()


render_design_choices()


render_post_deployment()

# Render best practices
render_best_practices()

st.markdown(
    '''
    <style>
    .streamlit-expanderHeader {
        background-color: blue;
        color: white; # Adjust this for expander header color
    }
    .streamlit-expanderContent {
        background-color: blue;
        color: white; # Expander content color
    }
    </style>
    ''',
    unsafe_allow_html=True
)

footer="""<style>

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: #2C1E5B;
color: white;
text-align: center;
}
</style>
<div class="footer">
<p>Developed with ❤️ by <a style='display: inline; text-align: center;' href="https://www.linkedin.com/in/mahantesh-hiremath/" target="_blank">MAHANTESH HIREMATH</a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)  