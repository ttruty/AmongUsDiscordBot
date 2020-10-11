FROM python:3.8-slim-buster

RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential
COPY . /
RUN pip3 install -r requirements.txt
ENV DISCORD_TOKEN=XXXXXXXXXXXXXXXXXXX
ENV GIPHY_KEY=XXXXXXXXXXXXXXXXX

ENTRYPOINT ["python"]
CMD ["bot.py"]