# Tutorial: Build a Hello World REST API with Lambda proxy integration

[Lambda proxy integration](https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html) is a lightweight, flexible API Gateway API integration type that allows you to integrate an API method – or an entire API – with a Lambda function. The Lambda function can be written in [any language that Lambda supports](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html). Because it's a proxy integration, you can change the Lambda function implementation at any time without needing to redeploy your API.

In this tutorial, you do the following:

-   Create a "Hello, World!" Lambda function to be the backend for the API.

-   Create and test a "Hello, World!" API with Lambda proxy integration.


**Topics**

## Create a "Hello, World!" Lambda function

This function returns a greeting to the caller as a JSON object in the following format:

```
{
    "greeting": "Good {time}, {name} of {city}.[ Happy {day}!]"
}
```

**Create a "Hello, World!" Lambda function in the Lambda console**

1.  Sign in to the Lambda console at [https://console.aws.amazon.com/lambda](https://console.aws.amazon.com/lambda)

-   Choose **Functions** in the navigation pane.

-   Choose **Create function**.

-   Choose **Author from scratch**.

-   Under **Basic information**, do the following:

    1.  In **Function name**, enter `GetStartedLambdaProxyIntegration`.

    2.  From the **Runtime** dropdown list, choose a supported Node.js runtime.

    3.  Under **Permissions**, expand **Choose or create an execution role**. From the **Execution role** dropdown list, choose **Create new role from AWS policy templates**.

    4.  In **Role name**, enter `GetStartedLambdaBasicExecutionRole`.

    5.  Leave the **Policy templates** field blank.

    6.  Choose **Create function**.

-   Under **Function code**, in the inline code editor, copy/paste the following code:


1.  ```
    'use strict';
    console.log('Loading hello world function');

    export const handler = async (event) => {
        let name = "you";
        let city = 'World';
        let time = 'day';
        let day = '';
        let responseCode = 200;
        console.log("request: " + JSON.stringify(event));

        if (event.queryStringParameters && event.queryStringParameters.name) {
            console.log("Received name: " + event.queryStringParameters.name);
            name = event.queryStringParameters.name;
        }

        if (event.queryStringParameters && event.queryStringParameters.city) {
            console.log("Received city: " + event.queryStringParameters.city);
            city = event.queryStringParameters.city;
        }

        if (event.headers && event.headers['day']) {
            console.log("Received day: " + event.headers.day);
            day = event.headers.day;
        }

        if (event.body) {
            let body = JSON.parse(event.body)
            if (body.time)
                time = body.time;
        }

        let greeting = `Good ${time}, ${name} of ${city}.`;
        if (day) greeting += ` Happy ${day}!`;

        let responseBody = {
            message: greeting,
            input: event
        };

        // The output from a Lambda proxy integration must be
        // in the following JSON object. The 'headers' property
        // is for custom response headers in addition to standard
        // ones. The 'body' property  must be a JSON string. For
        // base64-encoded payload, you must also set the 'isBase64Encoded'
        // property to 'true'.
        let response = {
            statusCode: responseCode,
            headers: {
                "x-custom-header" : "my custom header value"
            },
            body: JSON.stringify(responseBody)
        };
        console.log("response: " + JSON.stringify(response))
        return response;
    };
    ```

2.  Choose **Deploy**.


## Create a "Hello, World!" API

Now create an API for your "Hello, World!" Lambda function by using the API Gateway console.

**Build a "Hello, World!" API**

1.  Sign in to the API Gateway console at [https://console.aws.amazon.com/apigateway](https://console.aws.amazon.com/apigateway)

2.  If this is your first time using API Gateway, you see a page that introduces you to the features of the service. Under **REST API**, choose **Build**. When the **Create Example API** popup appears, choose **OK**.

    If this is not your first time using API Gateway, choose **Create API**. Under **REST API**, choose **Build**.

3.  Create an empty API as follows:

    1.  Under **Create new API**, choose **New API**.

    2.  Under **Settings**:

        -   For **API name**, enter `LambdaSimpleProxy`.

        -   If desired, enter a description in the **Description** field; otherwise, leave it empty.

        -   Leave **Endpoint Type** set to **Regional**.


    3.  Choose **Create API**.

4.  Create the `helloworld` resource as follows:

    1.  Choose the root resource (**/**) in the **Resources** tree.

    2.  Choose **Create Resource** from the **Actions** dropdown menu.

    3.  Leave **Configure as proxy resource** unchecked.

    4.  For **Resource Name**, enter `helloworld`.

    5.  Leave **Resource Path** set to **/helloworld**.

    6.  Leave **Enable API Gateway CORS** unchecked.

    7.  Choose **Create Resource**.

5.  In a proxy integration, the entire request is sent to the backend Lambda function as-is, via a catch-all `ANY` method that represents any HTTP method. The actual HTTP method is specified by the client at run time. The `ANY` method allows you to use a single API method setup for all of the supported HTTP methods: `DELETE`, `GET`, `HEAD`, `OPTIONS`, `PATCH`, `POST`, and `PUT`.

    To set up the `ANY` method, do the following:

    1.  In the **Resources** list, choose **/helloworld**.

    2.  In the **Actions** menu, choose **Create method**.

    3.  Choose **ANY** from the dropdown menu, and choose the checkmark icon

    4.  Leave the **Integration type** set to **Lambda Function**.

    5.  Choose **Use Lambda Proxy integration**.

    6.  From the **Lambda Region** dropdown menu, choose the region where you created the `GetStartedLambdaProxyIntegration` Lambda function.

    7.  In the **Lambda Function** field, type any character and choose `GetStartedLambdaProxyIntegration` from the dropdown menu.

    8.  Leave **Use Default Timeout** checked.

    9.  Choose **Save**.

    10.  Choose **OK** when prompted with **Add Permission to Lambda Function**.


## Deploy and test the API

**Deploy the API in the API Gateway console**

1.  Choose **Deploy API** from the **Actions** dropdown menu.

2.  For **Deployment stage**, choose **[new stage]**.

3.  For **Stage name**, enter `test`.

4.  If desired, enter a **Stage description**.

5.  If desired, enter a **Deployment description**.

6.  Choose **Deploy**.

7.  Note the API's **Invoke URL**.


### Use browser and cURL to test an API with Lambda proxy integration

You can use a browser or [cURL](https://curl.haxx.se/)

to test your API.

To test `GET` requests using only query string parameters, you can type the URL for the API's `helloworld` resource into a browser address bar. For example: **https://r275xc9bmd.execute-api.ap-southeast-2.amazonaws.com/test/helloworld?name=Holly&city=Melbourne**

For other methods, you must use more advanced REST API testing utilities, such as [POSTMAN](https://www.postman.com/)

or [cURL](https://curl.haxx.se/)

. This tutorial uses cURL. The cURL command examples below assume that cURL is installed on your computer.

**To test the deployed API using cURL:**

1.  Open a terminal window.

2.  Copy the following cURL command and paste it into the terminal window, replacing `` `r275xc9bmd` `` with your API's API ID and `` `ap-southeast-2` `` with the region where your API is deployed.


```
curl -v -X POST \
  'https://r275xc9bmd.execute-api.ap-southeast-2.amazonaws.com/test/helloworld?name=Holly&city=Melbourne' \
  -H 'content-type: application/json' \
  -H 'day: Thursday' \
  -d '{ "time": "evening" }'
```

Note

If you're running the command on Windows, use this syntax instead:

1.  ```
    curl -v -X POST "https://r275xc9bmd.execute-api.us-east-1.amazonaws.com/test/helloworld?name=Holly&city=Melbourne" -H "content-type: application/json" -H "day: Thursday" -d "{ \"time\": \"evening\" }"
    ```


You should get a successful response with a payload similar to the following:

```
{
  "message":"Good evening, Holly of Melbourne. Happy Thursday!",
  "input":{
    "resource":"/helloworld",
    "path":"/helloworld",
    "httpMethod":"POST",
    "headers":{"Accept":"*/*",
    "content-type":"application/json",
    "day":"Thursday",
    "Host":"r275xc9bmd.execute-api.us-east-1.amazonaws.com",
    "User-Agent":"curl/7.64.0",
    "X-Amzn-Trace-Id":"Root=1-1a2b3c4d-a1b2c3d4e5f6a1b2c3d4e5f6",
    "X-Forwarded-For":"72.21.198.64",
    "X-Forwarded-Port":"443",
    "X-Forwarded-Proto":"https"},
    "multiValueHeaders":{"Accept":["*/*"],
    "content-type":["application/json"],
    "day":["Thursday"],
    "Host":["r275xc9bmd.execute-api.us-east-1.amazonaws.com"],
    "User-Agent":["curl/0.0.0"],
    "X-Amzn-Trace-Id":["Root=1-1a2b3c4d-a1b2c3d4e5f6a1b2c3d4e5f6"],
    "X-Forwarded-For":["11.22.333.44"],
    "X-Forwarded-Port":["443"],
    "X-Forwarded-Proto":["https"]},
    "queryStringParameters":{"city":"Melbourne",
    "name":"Holly"
  },
  "multiValueQueryStringParameters":{
    "city":["Melbourne"],
    "name":["Holly"]
  },
  "pathParameters":null,
  "stageVariables":null,
  "requestContext":{
    "resourceId":"3htbry",
    "resourcePath":"/helloworld",
    "httpMethod":"POST",
    "extendedRequestId":"a1b2c3d4e5f6g7h=",
    "requestTime":"20/Mar/2019:20:38:30 +0000",
    "path":"/test/helloworld",
    "accountId":"123456789012",
    "protocol":"HTTP/1.1",
    "stage":"test",
    "domainPrefix":"r275xc9bmd",
    "requestTimeEpoch":1553114310423,
    "requestId":"test-invoke-request",
    "identity":{"cognitoIdentityPoolId":null,
      "accountId":null,
      "cognitoIdentityId":null,
      "caller":null,
      "sourceIp":"test-invoke-source-ip",
      "accessKey":null,
      "cognitoAuthenticationType":null,
      "cognitoAuthenticationProvider":null,
      "userArn":null,
      "userAgent":"curl/0.0.0","user":null
    },
    "domainName":"r275xc9bmd.execute-api.us-east-1.amazonaws.com",
    "apiId":"r275xc9bmd"
  },
  "body":"{ \"time\": \"evening\" }",
  "isBase64Encoded":false
  }
}
```

If you change `POST` to `PUT` in the preceding method request, you should get the same response.

To test the `GET` method, copy the following `cURL` command and paste it into the terminal window, replacing `` `r275xc9bmd` `` with your API's API ID and `` `us-east-1` `` with the region where your API is deployed.

```
curl -X GET \
  'https://r275xc9bmd.execute-api.us-east-1.amazonaws.com/test/helloworld?name=Holly&city=Melbourne' \
  -H 'content-type: application/json' \
  -H 'day: Thursday'
```

You should get a response similar to the result from the preceding `POST` request, except that the `GET` request does not have any payload. So the `body` parameter will be `null`.
