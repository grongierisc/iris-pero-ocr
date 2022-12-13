# OCR DEMO

This is a demo of the OCR functionality of the pero-ocr library.

It used in the iris application server in python.

## Demo

This is an example of input data :

![input](https://github.com/grongierisc/iris-pero-ocr/blob/master/misc/sample/United_States_Declaration_of_Independence.jpg?raw=true)

This is the result of the OCR :

In this example you have the following information:

- The text is in the `TextEquiv` tag
- The confidence is in the `conf` attribute of the `TextEquiv` tag
- The coordinates of the text are in the `Coords` tag

```xml
<PcGts xmlns="http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15/pagecontent.xsd">
  <Metadata>
    <Creator>Pero OCR</Creator>
    <Created>2022-12-13T08:47:12.207893+00:00</Created>
    <LastChange>2022-12-13T08:47:12.207893+00:00</LastChange>
  </Metadata>
  <Page imageFilename="/irisdev/app/misc/in/United_States_Declaration_of_Independence.jpg" imageWidth="3923" imageHeight="4656">
    <TextRegion id="r004">
      <Coords points="977,121 932,121 932,283 1189,277 1178,114 977,121"/>
      <TextLine id="r004-l002" index="0" custom="heights_v2:[123.7,39.0]">
        <Coords points="932,121 932,283 1189,277 1178,114 1130,118 1100,117 1048,121 1019,121 977,121 932,121"/>
        <Baseline points="932,244 977,244 1019,244 1058,244 1100,241 1138,241 1186,238"/>
        <TextEquiv conf="1.000">
          <Unicode>IN</Unicode>
        </TextEquiv>
      </TextLine>
    </TextRegion>
    <TextRegion id="r008">
      <Coords points="1461,107 1241,107 1241,287 2116,290 2549,281 2986,287 3211,277 3203,98 2978,107 2552,101 2114,111 1461,107"/>
      <TextLine id="r008-l001" index="0" custom="heights_v2:[133.8,45.8]">
        <Coords points="1241,107 1241,287 1464,287 1681,284 1896,287 2116,290 2549,281 2986,287 3211,277 3203,98 2978,107 2552,101 2327,107 2114,111 1461,107 1241,107"/>
        <Baseline points="1241,241 1463,241 1682,238 1897,241 2116,244 2331,241 2550,235 2765,238 2984,241 3209,231"/>
        <TextEquiv conf="0.910">
          <Unicode>CONGRESS, JULY 4, 1776.</Unicode>
        </TextEquiv>
      </TextLine>
    </TextRegion>
    <TextRegion id="r001">
      <Coords points="591,452 208,455 209,611 1723,602 2100,608 2855,595 3617,598 3618,442 2855,439 2098,452 1725,446 591,452"/>
      <TextLine id="r001-l003" index="0" custom="heights_v2:[113.8,42.1]">
        <Coords points="208,455 209,611 592,608 968,605 1218,605 1723,602 2100,608 2855,595 3231,595 3617,598 3618,442 2855,439 2477,446 2098,452 1725,446 1346,449 1159,449 591,452 208,455"/>
        <Baseline points="209,569 592,566 968,563 1347,563 1723,559 2100,566 2479,559 2855,553 3231,553 3617,556"/>
        <TextEquiv conf="0.289">
          <Unicode>Dhe unaniwons Declaratton of te Heten maiss States of TNmerica</Unicode>
        </TextEquiv>
      </TextLine>
    </TextRegion>
    <TextRegion id="r000">
      <Coords points="161,3474 161,3539 423,3539 633,3536 958,3468 1354,3472 1764,3581 1944,3571 2246,3730 2653,3718 2718,3633 2855,3608 3238,3557 3514,3554 3739,3462 3762,3397 3761,3333 3735,3139 3743,2696 3730,2177 3735,1920 3723,1727 3736,1341 3717,1014 3724,943 3719,818 3697,693 1012,712 795,776 421,776 183,786 173,848 168,1032 173,2392 160,2713 161,3474"/>
      <TextLine id="r000-l004" index="0" custom="heights_v2:[40.2,18.4]">
        <Coords points="2796,699 2501,703 2205,706 1909,709 1611,709 1460,709 1012,712 1013,771 1315,768 1611,768 1910,768 2206,764 2502,761 2800,758 3096,758 3392,755 3698,752 3697,693 3392,696 3096,699 2802,699 2796,699"/>
        <Baseline points="1013,752 1315,749 1611,749 1910,749 2206,746 2501,743 2800,739 3096,739 3392,736 3697,733"/>
        <TextEquiv conf="0.281">
          <Unicode>hen n lí loune z human venl, i kemu nematy k mpeopě toíohohhehttcal bandí uhích have connechdí tem vith ancthet, andíl</Unicode>
        </TextEquiv>
      </TextLine>
      <TextLine id="r000-l005" index="1" custom="heights_v2:[40.4,19.2]">
        <Coords points="421,776 421,836 794,836 1157,839 1521,839 1884,836 2244,833 2608,829 2971,826 3335,823 3704,813 3703,754 3333,763 2970,767 2607,770 2244,773 1884,776 1520,779 1157,779 795,776 421,776"/>
        <Baseline points="421,817 794,817 1157,820 1521,820 1884,817 2244,813 2608,810 2971,807 3334,804 3704,794"/>
        <TextEquiv conf="0.211">
          <Unicode>o hi ſhwes f he eail, fie rehatal andequal flohon &amp; ufch lhe laav  . kalut and   Aloil ped entilt ttem, a dant rafech to the ofunin o manknd tequies fhat thep</Unicode>
        </TextEquiv>
      </TextLine>
     <!-- Truncated for readme-->
      <TextLine id="r019-l105" index="9" custom="heights_v2:[47.5,21.7]">
        <Coords points="3209,4269 3214,4336 3257,4333 3296,4333 3332,4333 3373,4337 3411,4337 3452,4336 3488,4333 3527,4333 3575,4333 3575,4264 3527,4264 3488,4264 3446,4267 3411,4267 3373,4267 3338,4264 3296,4264 3257,4264 3209,4267 3209,4269"/>
        <Baseline points="3212,4315 3257,4312 3296,4312 3334,4312 3373,4315 3411,4315 3450,4315 3488,4312 3527,4312 3575,4312"/>
        <TextEquiv conf="0.283">
          <Unicode>imuiaa</Unicode>
        </TextEquiv>
      </TextLine>
      <TextLine id="r019-l108" index="10" custom="heights_v2:[40.9,20.2]">
        <Coords points="3198,4406 3251,4409 3294,4409 3339,4412 3394,4415 3398,4354 3343,4351 3298,4348 3251,4348 3202,4345 3198,4406"/>
        <Baseline points="3199,4386 3251,4389 3296,4389 3341,4392 3395,4395"/>
        <TextEquiv conf="0.370">
          <Unicode>Qlver</Unicode>
        </TextEquiv>
      </TextLine>
      <TextLine id="r019-l114" index="11" custom="heights_v2:[39.2,19.1]">
        <Coords points="3181,4469 3225,4466 3263,4466 3305,4466 3327,4466 3352,4465 3386,4462 3424,4462 3472,4462 3472,4404 3424,4404 3386,4404 3341,4407 3305,4407 3263,4407 3225,4407 3177,4411 3181,4469"/>
        <Baseline points="3180,4450 3225,4447 3263,4447 3305,4447 3344,4447 3386,4443 3424,4443 3472,4443"/>
        <TextEquiv conf="0.312">
          <Unicode>Vbalřew/</Unicode>
        </TextEquiv>
      </TextLine>
    </TextRegion>
    <TextRegion id="r020">
      <Coords points="3685,4399 3607,4399 3607,4465 3685,4465 3685,4399"/>
      <TextLine id="r020-l112" index="0" custom="heights_v2:[44.3,21.4]">
        <Coords points="3607,4399 3607,4465 3685,4465 3685,4399 3607,4399"/>
        <Baseline points="3607,4443 3685,4443"/>
        <TextEquiv conf="0.486">
          <Unicode>17.</Unicode>
        </TextEquiv>
      </TextLine>
    </TextRegion>
  </Page>
</PcGts>
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
