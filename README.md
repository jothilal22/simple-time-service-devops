# simple-time-service-devops
A tiny web service that tells you the current time and your IP address.
This project was built as part of a DevOps-focused challenge to show off containerization, cloud deployment, and Terraform skills.


## What It Does
When you hit the root endpoint `/`, it responds with a JSON object like this:

```json
{
  "timestamp": "2025-04-18T12:34:56Z",
  "ip": "192.168.1.1"
}
