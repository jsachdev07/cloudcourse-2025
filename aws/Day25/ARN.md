# Amazon Resource Name (ARN) in AWS

In **AWS (Amazon Web Services)**, an **ARN (Amazon Resource Name)** is a **unique identifier** used to identify resources across all AWS services.

---

## 🔹 ARN Format

arn:partition:service:region:account-id:resource


### Breakdown:

| Component     | Description |
|---------------|-------------|
| `arn`         | Literal prefix indicating it's an ARN. |
| `partition`   | AWS partition: `aws` (standard), `aws-us-gov` (GovCloud), `aws-cn` (China). |
| `service`     | The AWS service name (e.g., `s3`, `ec2`, `lambda`). |
| `region`      | AWS Region (e.g., `us-east-1`, `eu-west-1`). |
| `account-id`  | AWS Account ID (12-digit number). |
| `resource`    | The resource identifier (name, path, or ID, varies by service). |

---

## 🔹 Example ARNs

- **S3 Bucket**:
arn:aws:s3:::my-bucket


- **EC2 Instance**:
arn:aws:ec2:us-east-1:123456789012:instance/i-1234567890abcdef0



- **Lambda Function**:
arn:aws:lambda:us-west-2:123456789012:function:my-function


---

## 🔹 Why ARNs Are Important

ARNs are used in:

- ✅ **IAM policies** to define permissions
- ✅ **CloudFormation** templates
- ✅ **Monitoring and logging**
- ✅ **Cross-service communication** (e.g., Lambda triggers)

---