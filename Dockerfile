ARG PYTHON_VERSION=3.9-slim-buster
FROM python:${PYTHON_VERSION} as python

ARG BUILD_ENVIRONMENT=pre

ENV APP_HOME=/home/bling_qa
ENV RUN_TEST_FROM=JENKINS
ENV BUILD_ENV ${BUILD_ENVIRONMENT}

# Install chrome
RUN set -ex; \
    apt-get update; \
    apt-get install -y gnupg wget curl unzip --no-install-recommends; \
    wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | \
    gpg --no-default-keyring --keyring gnupg-ring:/etc/apt/trusted.gpg.d/google.gpg --import; \
    chmod 644 /etc/apt/trusted.gpg.d/google.gpg; \
    echo "deb https://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list; \
    apt-get update -y; \
    apt-get install -y google-chrome-stable; \
    CHROME_VERSION=$(google-chrome --product-version | grep -o "[^\.]*\.[^\.]*\.[^\.]*"); \
    CHROMEDRIVER_VERSION=$(curl -s "https://chromedriver.storage.googleapis.com/LATEST_RELEASE_$CHROME_VERSION"); \
    wget -q --continue -P /chromedriver "https://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip"; \
    unzip /chromedriver/chromedriver* -d /usr/local/bin/


# Requirements are installed here to ensure they will be cached.
COPY ./setup/requirements.txt ${APP_HOME}/setup/requirements.txt
RUN pip install -r ${APP_HOME}/setup/requirements.txt

RUN mkdir -p ${APP_HOME}

WORKDIR ${APP_HOME}
COPY . ${APP_HOME}

RUN ["chmod", "+x", "./docker-entrypoint"]

ENTRYPOINT ["./docker-entrypoint"]