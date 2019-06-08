FROM python:3.7.2-stretch

# Install Google Chrome And unzip
ARG CHROME_VERSION="google-chrome-stable=72.0.3626.119-1"
# The following command is a copy from what selenium official dockerfile does:
# It downloads a key,
# Echo the source into the source list
# Installs chrome and unzip(both at the same install to reduce overhead)
# Removes unneeded files for the installation
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
  && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list \
  && apt-get update -qqy \
  && apt-get -qqy install \
    ${CHROME_VERSION:-google-chrome-stable} \
    unzip \
  && rm /etc/apt/sources.list.d/google-chrome.list \
  && rm -rf /var/lib/apt/lists/* /var/cache/apt/*

# Install ChromeDriver
ARG CHROME_DRIVER_VERSION_TAG="2.46"
# The following command is a copy from what selenium official dockerfile does:
# It sets the actual version wanted in a variable for the command(changes it if its latest)
# Downloads the zip
# Removes chromedriver if already exists
# Unzips the new chromedriver
# Sets chromedriver as executable(skipped several uninteresting commands)
# Copies chromedriver into the default path which selenium looks for it
# (this is extremely important because if its not there it doesnt count)
RUN CHROME_DRIVER_VERSION=$(if [ ${CHROME_DRIVER_VERSION_TAG:-latest} = "latest" ]; then echo $(wget -qO- https://chromedriver.storage.googleapis.com/LATEST_RELEASE); else echo $CHROME_DRIVER_VERSION_TAG; fi) \
  && echo "Using chromedriver version: "$CHROME_DRIVER_VERSION \
  && wget --no-verbose -O /tmp/chromedriver_linux64.zip https://chromedriver.storage.googleapis.com/$CHROME_DRIVER_VERSION/chromedriver_linux64.zip \
  && rm -rf /opt/selenium/chromedriver \
  && unzip /tmp/chromedriver_linux64.zip -d /opt/selenium \
  && rm /tmp/chromedriver_linux64.zip \
  && mv /opt/selenium/chromedriver /opt/selenium/chromedriver-$CHROME_DRIVER_VERSION \
  && chmod 755 /opt/selenium/chromedriver-$CHROME_DRIVER_VERSION \
  && ln -fs /opt/selenium/chromedriver-$CHROME_DRIVER_VERSION /usr/bin/chromedriver

ADD ./source ./source
RUN pip install -r ./source/requirements
WORKDIR ./
ENTRYPOINT ["./run_tests.sh"]
