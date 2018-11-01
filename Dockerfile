FROM python:3.6.6
ENV PYTHONUNBUFFERED 1

##########################################################################
## Install the container
## Copy files one by one and split commands to use docker cache
##########################################################################

RUN mkdir /code
WORKDIR /code

COPY requirements.txt /code/

#########################################################################
## Install packages
#########################################################################

RUN pip install --quiet -r /code/requirements.txt

#########################################################################
## Copy everything into the container
#########################################################################

COPY . /code

#########################################################################
## Set the entrypoint
#########################################################################

ENTRYPOINT ["/code/entrypoint.sh"]
