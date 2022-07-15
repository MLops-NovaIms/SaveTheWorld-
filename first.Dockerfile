FROM python:latest

LABEL version=0.0.1 maintainer="jjmerelo@gmail.com"
RUN useradd -ms /bin/bash novamlops 
USER novamlops
WORKDIR /home/novamlops
ENV PATH=~"/home/novamlops/.poetry/bin:/home/novamlops/.local/bin:${PATH}"

COPY --chown=novamlops pyproject.toml poetry.lock .
RUN mkdir colares_project
COPY --chown=novamlops colares_project/ colares_project/
RUN pip install poetry \
    && poetry install \
    && poetry run testcsv \
    && rm -rf colares_project/ pyproject.toml poetry.lock

ENTRYPOINT cat Export_test.csv