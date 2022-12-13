# OCR DEMO

This is a demo of the OCR functionality of the pero-ocr library.

It used in the iris application server in python.

## Demo

This is an example of input data :

TO BE POSTED

This is the result of the OCR :

In this example you have the following information:

- The text is in the `TextEquiv` tag
- The confidence is in the `conf` attribute of the `TextEquiv` tag
- The coordinates of the text are in the `Coords` tag

```xml
to be posted
```

## Installation

```bash
git clone https://github.com/grongierisc/iris-pero-ocr
```

/!\ This demo requires the models to be installed /!\

To install the model download the model from the realase page and extract it in the misc/pero-ocr-fix-computation-on-cpu of the project.

https://github.com/grongierisc/iris-pero-ocr/releases/download/v1.0.0/OCR_350000.pt.cpu

https://github.com/grongierisc/iris-pero-ocr/releases/download/v1.0.0/ParseNet_296000.pt.cpu

/!\ Both models are required /!\

This is the expected misc folder structure : 

```
misc
├── config_file.ini
├── in
├── out
└── pero-ocr-fix-computation-on-cpu
    ├── OCR_350000.pt.cpu
    ├── ParseNet_296000.pt.cpu
    └── ocr_engine.json
```

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
