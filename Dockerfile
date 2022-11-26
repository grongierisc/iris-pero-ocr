ARG IMAGE=intersystemsdc/iris-community:latest
FROM $IMAGE

# use the root user to install packages
USER root   

ARG DEBIAN_FRONTEND=noninteractive
# Update package and install sudo
RUN apt-get update && apt-get install -y \
	git \
	nano \
    python3-opencv \
	sudo && \
	/bin/echo -e ${ISC_PACKAGE_MGRUSER}\\tALL=\(ALL\)\\tNOPASSWD: ALL >> /etc/sudoers && \
	sudo -u ${ISC_PACKAGE_MGRUSER} sudo echo enabled passwordless sudo-ing for ${ISC_PACKAGE_MGRUSER}

# create a directory for the application     
WORKDIR /irisdev/app
RUN chown ${ISC_PACKAGE_MGRUSER}:${ISC_PACKAGE_IRISGROUP} /irisdev/app
USER ${ISC_PACKAGE_MGRUSER}

# Copy the source code
COPY . .
COPY iris.script /tmp/iris.script

RUN pip3 install torch==1.13.0+cpu torchvision==0.10.0+cpu -f https://download.pytorch.org/whl/torch_stable.html
# install required packages
RUN pip3 install -r requirements.txt

# environment variables for embedded python
ENV IRISUSERNAME "SuperUser"
ENV IRISPASSWORD "SYS"
ENV IRISNAMESPACE "IRISAPP"

# create the namespace and install the application
RUN iris start IRIS \
	&& iris session IRIS < /tmp/iris.script \
    && /usr/irissys/bin/irispython src/python/register.py \
    && iris stop IRIS quietly



