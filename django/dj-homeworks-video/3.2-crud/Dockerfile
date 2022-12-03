FROM python:3.9

RUN pip install --upgrade pip

COPY ./stocks_products/requirements.txt /src/stocks_products/requirements.txt

RUN python3 -m pip install -r /src/stocks_products/requirements.txt

COPY . /src

WORKDIR /src/stocks_products

RUN mkdir static
