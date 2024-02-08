FROM public.ecr.aws/lambda/python:3.11

RUN mkdir -p /app
COPY ./main.py /app
COPY scrapebot /app/scrapebot
COPY ./requirements.txt /app
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
WORKDIR /app
EXPOSE 8081
CMD [ "main.py" ]
ENTRYPOINT [ "python" ]