# Profile API
This is a demo project using python and AWS API Gateway with AWS Lambda Proxy Integration

## Docker

> docker build -t lambda .

> docker run -p 9000:8080 lambda

> curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{}'

OR 

Start
> docker-compose build
> docker-compose up

Shutdown
> docker-compose down 

## Testing

### Unit Tests
>  python -m pytest tests

## Deployment 
The project uses terraform to deploy the code

TODO: Add terraform scripts and command to deploy