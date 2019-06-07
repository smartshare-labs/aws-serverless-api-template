### Serverless Lambda Template

This is the template we use when developing new serverless python code on AWS. It includes a number of basic but simple improvements to the standard `aws-python3` template that serverless offers out of the box:

- `./common`: Common configurations for improved readability in yml files
- `./local_server`: A dockerized flask application which is useful if you're building an API. This can be connected to our `local_mysql` container.
- `./modules`: Reusable, tested python code for common things such as database I/O.
- `./functions`: This is where your lambda handlers should go. We include an example of one function that calls into one of our modules.
 
---

### Usage

To get started, you need to have serverless installed: `npm install -g serverless`

Then, to create a new project using our template, run:

`sls create --template-url https://github.com/smartshare-labs/aws-serverless-api-template --path NEW_PROJECT_PATH`

Note: A good rule of thumb when developing is to keep core application logic out of your lambda handlers. This is the pattern we try to employ with the `./modules` folder. Keeping your complexity in tested, reusable modules such as these allows for simple integration testing of the lambda handlers themselves.

---

### Using the local flask server

We assume you already have docker installed.

---

### Testing