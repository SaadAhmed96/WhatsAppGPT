# WhatsApp Chatbot with AI-Powered Contextual Responses using ChatGPT API, LangChain, and Pinecone 

The WhatsApp Chatbot project is a powerful integration that combines the capabilities of ChatGPT API, Twilio, LangChain and Pinecone to deliver intelligent and contextually relevant responses. 

By leveraging the potential of natural language processing and vector databases, this project enables users to interact seamlessly with the chatbot through WhatsApp messaging. 

Here's an overview of the project's logical flow:

• User sends a message to the WhatsApp number. 
• Twilio's webhook directs the message to a Lambda function for processing. 
• The Lambda function parses the message and generates embeddings. 
• The embeddings are used to search Pinecone's vector index for similar text. 
• The retrieved contextual information is incorporated into the ChatGPT model. 
• ChatGPT generates a response based on the user's query and the extracted context. 
• The response is sent back to the user through the WhatsApp interface.

This project showcases the potential of AI-powered chatbots to provide personalized and informed interactions, allowing users to obtain accurate and contextually relevant answers to their questions.

## How to Run the WhatsApp Chatbot Project

**Note:**
- Docker and AWS CLI must be installed on your system. It is also recommended to use Anaconda for environment management.

### Step 1: Clone the Repository

Clone the project repository by executing the following command in your terminal:

```
git clone https://github.com/SaadAhmed96/WhatsAppGPT.git
```

### Step 2: Install Dependencies

Navigate to the `WhatsAppGpt` directory and install all the required dependencies by running the following command:

```
pip install -r requirements.txt
```

Create a new conda environment before executing the above command, if desired.

### Step 3: Configure Environment Variables

Create a `.env` file using the following command:

```
nano .env
```

Inside the `.env` file, add the following variables:

```
TWILIO_ACCOUNT_SID=""
TWILIO_AUTH_TOKEN=""
TWILIO_NUMBER=""
OPENAI_API_KEY=""
PINECONE_API_KEY=""
PINECONE_API_ENV=""
PINECONE_INDEX_NAME=""
```

Replace the `""` marks with the corresponding values obtained from the steps below:

#### Obtaining Values for Environment Variables:

For `TWILIO_ACCOUNT_SID` and `TWILIO_AUTH_TOKEN`:

1. Sign up for a Twilio account at https://www.twilio.com/try-twilio.
2. Once logged in, navigate to the Console.
3. Locate or create a project in the Dashboard.
4. In the project Dashboard, find your Account SID and Auth Token under the "Project Info" section.

For `TWILIO_NUMBER`:

1. After obtaining the Twilio Account SID and Auth Token, go to the Twilio Console.
2. Select the project you created or want to use.
3. Navigate to the "Phone Numbers" section in the sidebar.
4. Choose a phone number from the list or purchase a new one.
5. Copy the desired phone number, including the country code, as the value for `TWILIO_NUMBER`.

For `OPENAI_API_KEY`:

1. Go to the OpenAI website at https://openai.com/.
2. Sign in or create an account if needed.
3. Access the API keys or credentials section of your account.
4. Generate a new API key or locate an existing one.
5. Copy the API key and use it as the value for `OPENAI_API_KEY`.

For `PINECONE_API_KEY` and `PINECONE_API_ENV`:

1. Visit the Pinecone website at https://www.pinecone.io/.
2. Log in or create an account.
3. Go to your account settings or profile section.
4. Locate the API key section and generate a new API key if necessary.
5. Copy the API key as the value for `PINECONE_API_KEY`.
6. Determine the environment you want to use (e.g., production, development) and set it as the value for `PINECONE_API_ENV`.

For `PINECONE_INDEX_NAME`:

1. Access the Pinecone Console or API.
2. Choose the desired environment (e.g., production, development).
3. Locate or create an index where you want to store your data.
4. Copy the name of the index and set it as the value for `PINECONE_INDEX_NAME`.

Remember to keep your keys and tokens secure and avoid sharing them publicly.

### Step 5: Create Vectors for Query Data

To create vectors for the PDF data used to respond to user questions, run the following Python script:

```
python3 upload_vectors_data.py
```

Please note that this script may take some time to initially download packages and models. It may also encounter errors and suggest installing additional Python packages. In such cases, install the suggested packages and run the script again.

### Step 6: Create an AWS Account

To create an Amazon Elastic Container Registry (ECR) repository using the AWS Management Console, follow these steps:

1. Sign in to the AWS Management Console at https://console.aws.amazon.com.
2. Navigate to the Amazon ECR service.
3. In the ECR console, click on the "Repositories" option in the sidebar.
4. Click the "Create repository" button.
5. Provide a unique name for your repository in the "Repository name" field.
6. Review the configuration settings, and once you're satisfied, click the "Create repository" button to create the ECR repository.
7. After the repository is created, you will be redirected to the repository's overview page. Here, you can find details such as the repository URI, which you can use for pushing commands.

Also, configure the AWS CLI on your system to use the push commands later. Follow the instructions at https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html to set up the AWS CLI.

### Step 7: Push Docker Image to Amazon ECR

In the AWS ECR Console, click on your repository and locate the `View push commands` button. Click on it and follow the instructions provided to push the Docker image.

### Step 8: Create a Lambda Function

To create a Lambda function, open the Lambda Console in AWS and click on "Create function". Choose the container image option and select the image from the repository you just created.

Create the function and then go to the "Basic configuration" section. Set the RAM to 512MB and the timeout to 1 minute and 30 seconds. Use the "Environment variables" tab to add all the environment variables mentioned in your `.env` file.

Once done, navigate to the "Create Function URL" and grant access to everyone for the function. Select CORS and save the function.

Finally, go to Twilio and navigate to the Messaging section inside WhatsApp Senders. Open the desired number and use the function URL to update the Endpoint hook in Twilio, allowing it to use the logic of your Lambda function.

Congratulations! You have successfully set up and configured the WhatsApp Chatbot project. Users can now interact with the chatbot via WhatsApp messaging, and the responses will be powered by ChatGPT API and contextual information obtained from Pinecone's vector index.

References:

For a detailed step by step guide to run a FASTAPI on Lambda Using Container please refer to this helpful video:

https://www.youtube.com/watch?v=VYk3lwZbHBU&ab_channel=TalhaAnwar

Twilio Blog on creating a WhatsApp bot also helped a lot for this project
https://www.twilio.com/blog/ai-chatbot-whatsapp-python-twilio-openai