FROM python:3.10-alpine

RUN apk update
RUN pip install --no-cache-dir pipenv 

WORKDIR /usr/src/app
COPY Pipfile Pipfile.lock bootstrap.sh ./
COPY exchange ./exchange

RUN pipenv install --system --deploy

CMD flask run --host 0.0.0.0

EXPOSE 3000
ENTRYPOINT [ "/usr/src/app/bootstrap.sh" ]