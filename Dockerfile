FROM ubuntu:xenial-20190515
RUN apt update
RUN apt install -y python3
RUN apt install -y python3-pip
RUN pip3 install flask
RUN mkdir PROJECTS
RUN cd /PROJECTS
COPY . /PROJECTS/
RUN pip3 install -r /PROJECTS/requirements.txt
CMD ["python3", "/PROJECTS/app.py", "0.0.0.0.5000"]
