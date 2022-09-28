FROM python:alpine
WORKDIR /VieliTech/Regulator

COPY . .

COPY regulator /usr/local/bin

RUN pip3 install --no-cache -r requirements.txt

# Usado para manter o log do python
ENV PYTHONUNBUFFERED 1

CMD tail -f /dev/null
