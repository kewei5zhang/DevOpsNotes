# Homework
1. HelloWorld API extention: Update API request interface
- Notice your lambda function looks up four attributes from the api call: `name`, `city`, `day` and `time`. Try to update your API so that:
    - the API expects all four attributes passed in from API call body, and not query parameter or header.
    - only `name` and `city` is required from API call. When any of these two are not provided, the API should return error message indicating the correct API call parameters.
    - when `day` and `time` are not provided from API call, dynamically lookup day and time from code (use AEST timezone) and use the result in the response

2.  HelloWorld API extention: Support data read and write in your API
- Rename the exsiting `/helloworld` resource to `/register` resource, and support following when the API gets a PUT request on `/register`:
    - the API expects two required body attribute `name` and `city`, and put a unique record in dynamodb. (might need to introduce a primary key `ID` and generate this uniquely via code)
    - when the incoming request does not supply any of the required attribute, the API should return error message indicating the correct API call parameters.
- Create a new resource `/lookup` in the API, and support following when the API gets a GET request on `/lookup`:
    - the API expects one required body attribute `name`, and return all matched records (case insensitive) from dynamodb that matches the input name.

3. (Optional) HelloWorld API extention: Deploy your API using SAM

- You have been using AWS console to create and update your API Gateway and Lambda function.
- It's time to start using AWS SAM to build and deploy the API.
- Ref: https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-getting-started-hello-world.html
- Consider following: use `sam local invoke` to test your function during development
