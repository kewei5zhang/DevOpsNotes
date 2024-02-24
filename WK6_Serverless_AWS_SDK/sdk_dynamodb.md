# Write to DynamoDB in your HelloWorld API

## The Scenario

In this example, you use a Node.js modules to write one item in a DynamoDB table by using these methods of the `PutItemCommand` client class:

-   [PutItemCommand]([https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/DynamoDB.html#putItem-property](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/clients/client-dynamodb/classes/putitemcommand.html#constructor))

## Create a DynamoDB table

1. In AWS console, go to "DynamoDB" service.
2. Click "Create table" on the main page, and fill in following information:
	- Table name: HelloWorldTable
	- Partition key: name
	- keep the partition key type as "String"
	- click "Create table"

## Enable writing to DynamoDB in your Lambda permission

1. Go to your Lambda function, under "Configuration" - "Permission", click the IAM role associated to your Lambda function.
2. Add "AmazonDynamoDBFullAccess" policy to the IAM role.

## Write to DynamoDB in your Lambda function

1. Add following code to the start your `GetStartedLambdaProxyIntegration` Lambda Function.

```

// Load the AWS SDK for Node.js
import { DynamoDBClient, PutItemCommand } from "@aws-sdk/client-dynamodb";
// Create the DynamoDB service object
const client = new DynamoDBClient({
  region: "ap-southeast-2"
});

```
2. Add following code before the return statement of your `GetStartedLambdaProxyIntegration` Lambda Function.
```
    let params = {
      TableName: 'HelloWorldTable',
      Item: {
        'name' : {S: name},
        'city' : {S: city}
      }
    };
    console.log("params: ", params)
    const putItemCommand = new PutItemCommand(params); 

    try {
        const data = await client.send(putItemCommand);
        console.log("Item added successfully:", JSON.stringify(data, null, 2));
      } catch (err) {
        console.error("Error adding item:", err);
    };
 ```

## Test that you are successfully writing to DynamoDB table
Use CURL to hit your API:
`curl 'https://cjijhjep3e.execute-api.ap-southeast-2.amazonaws.com/test/helloworld?name=Holly&city=Melbourne'`
Check your DynamoDB table and validate you have a new item being added to the table.
