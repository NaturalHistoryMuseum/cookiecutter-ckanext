FROM naturalhistorymuseum/ckantest:0.1

WORKDIR /base/src/{{ cookiecutter.slug }}

# copy over the source
COPY . .

# install the base + test dependencies
RUN pip install -e .[test]

# this entrypoint ensures our service dependencies (postgresql, solr and redis) are running before
# running the cmd
ENTRYPOINT ["/bin/bash", "/opt/waits/basic.sh"]

# run the tests with coverage output
CMD ["pytest", "--cov=ckanext.{{ cookiecutter.short_name }}", "--ckan-ini=test.ini", "tests"]
