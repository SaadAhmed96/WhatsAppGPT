FROM public.ecr.aws/lambda/python:3.8

# Copy the Python files and requirements.txt to the container
COPY model.py  model.py
COPY utils.py utils.py
COPY requirements.txt  .

RUN  pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

# Copy function code
COPY app.py ${LAMBDA_TASK_ROOT}

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD [ "app.handler" ]