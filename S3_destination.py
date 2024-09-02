import requests

url = "https://api.airbyte.com/v1/destinations"

payload = {
    "configuration": {
        "destinationType": "s3",
        "s3_bucket_region": "us-east-2",
        "format": { "format_type": "Parquet" },
        "access_key_id": "AKIATY7PXHP3N62QR73X",
        "s3_bucket_name": "bucketbns",
        "s3_bucket_path": "projectX/data/"
    },
    "name": "S3",
    "workspaceId": "e3e1519d-a388-494e-9868-3915ed1c653d"
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJ6Z1BPdmhDSC1Ic21OQnhhV3lnLU11dlF6dHJERTBDSEJHZDB2MVh0Vnk0In0.eyJleHAiOjE3MjE4MzA4MjgsImlhdCI6MTcyMTgzMDY0OCwianRpIjoiMDdjZTIxOTItOTZiOC00MDBhLWFjNzgtYjYwYjlmMTg0NGRmIiwiaXNzIjoiaHR0cHM6Ly9jbG91ZC5haXJieXRlLmNvbS9hdXRoL3JlYWxtcy9fYWlyYnl0ZS1hcHBsaWNhdGlvbi1jbGllbnRzIiwiYXVkIjoiYWNjb3VudCIsInN1YiI6IjM5ZWU4ZTY5LWUxZTEtNDZiZS1hYTRjLWFiMWM5ODk3ODFlNCIsInR5cCI6IkJlYXJlciIsImF6cCI6IjEwODRlMGM5LTk2OWQtNDY2MS1iZDk3LWJkZGYwMzliYzkyOCIsImFjciI6IjEiLCJyZWFsbV9hY2Nlc3MiOnsicm9sZXMiOlsib2ZmbGluZV9hY2Nlc3MiLCJ1bWFfYXV0aG9yaXphdGlvbiIsImRlZmF1bHQtcm9sZXMtX2FpcmJ5dGUtYXBwbGljYXRpb24tY2xpZW50cyJdfSwicmVzb3VyY2VfYWNjZXNzIjp7ImFjY291bnQiOnsicm9sZXMiOlsibWFuYWdlLWFjY291bnQiLCJtYW5hZ2UtYWNjb3VudC1saW5rcyIsInZpZXctcHJvZmlsZSJdfX0sInNjb3BlIjoib3BlbmlkIGVtYWlsIHByb2ZpbGUiLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsImNsaWVudEhvc3QiOiIxNzIuMjMuMS4xMSIsInVzZXJfaWQiOiIzOWVlOGU2OS1lMWUxLTQ2YmUtYWE0Yy1hYjFjOTg5NzgxZTQiLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJzZXJ2aWNlLWFjY291bnQtMTA4NGUwYzktOTY5ZC00NjYxLWJkOTctYmRkZjAzOWJjOTI4IiwiY2xpZW50QWRkcmVzcyI6IjE3Mi4yMy4xLjExIiwiY2xpZW50X2lkIjoiMTA4NGUwYzktOTY5ZC00NjYxLWJkOTctYmRkZjAzOWJjOTI4In0.Q71IJC3eA6Lj4eN4DrjAEdIMZrIm9YJxOm6Yf9PmXcva2OKvYdMFd-AFqa-lqVAiGRMI7QPQhr0FCC3DytL48X9NB1AJig2Q5zzyclPXjf4VGbeo9LLNU7Rp2jcsNVg3h2GI9mbcb5H6xw1tshH0yPmKxv8ukN229H1Bm3Pyo0RU_NsBl-eHB6wdGGjRdLaOhzPOfW-SpDcTrqNjTF_C6IcLAVNotYNOnbWIivo8UGyphbgNnFQirhf43Et4kJnwO_X6G8DqxblDBsYDnPELJHLpy1Fly1uoerXupIs_RzZPwKn8WlmlQCX5uUVT4sSJJ6SItPimcvlXo8Prmi1V3g"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)
