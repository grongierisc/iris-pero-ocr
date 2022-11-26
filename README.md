# OCR DEMO

This is a demo of the OCR functionality of the pero-ocr library.

It used in the iris application server in python.

## Installation

```bash
git clone <this repo>
```

/!\ This demo requires the models to be installed /!\

To install the model download the model from the realase page and extract it in the misc/pero-ocr-fix-computation-on-cpu of the project.

https://github.com/grongierisc/iris-pero-ocr/releases/download/v1.0.0/OCR_350000.pt.cpu
https://github.com/grongierisc/iris-pero-ocr/releases/download/v1.0.0/ParseNet_296000.pt.cpu

/!\ Both models are required /!\

Then docker-compose up

```bash
docker-compose up
```

## Usage

Put any sample image in the `samples` folder and copy them in misc/in folder and they will be processed by the OCR.

The results will be in the misc/out folder.

You will find the xml files with the results and the images with the detected text.

You can monitor the progress in the logs here [http](http://localhost:53795/csp/irisapp/EnsPortal.ProductionConfig.zen?NAMESPACE=IRISAPP&NAMESPACE=IRISAPP&)

login with _SYSTEM and SYS

## How it works in IRIS

The OCR is an Business Service that parse all the files in the misc/in folder and put the results in a message queue.

The message queue is consumed by a Business Operation that put the results in the misc/out folder.

Code is in the src/python/pero-ocr folder.
