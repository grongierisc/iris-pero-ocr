# OCR DEMO

This is a demo of the OCR functionality of the pero-ocr library.

It used in the iris application server in python.

## Demo

This is an example of input data :

![input](https://github.com/grongierisc/iris-pero-ocr/blob/master/misc/sample/39767739_Page_0.jpg?raw=true)

This is the result of the OCR :

In this example you have the following information:

- The text is in the `TextEquiv` tag
- The confidence is in the `conf` attribute of the `TextEquiv` tag
- The coordinates of the text are in the `Coords` tag

```xml
<PcGts xmlns="http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15/pagecontent.xsd">
  <Metadata>
    <Creator>Pero OCR</Creator>
    <Created>2022-11-26T22:08:51.997106+00:00</Created>
    <LastChange>2022-11-26T22:08:51.997106+00:00</LastChange>
  </Metadata>
  <Page imageFilename="/irisdev/app/misc/in/39767739_Page_0.jpg" imageWidth="4132" imageHeight="5848">
    <TextRegion id="r005">
      <Coords points="815,828 549,833 550,916 1325,906 2875,906 3120,718 3120,617 2955,484 2548,489 1160,484 995,612 815,828"/>
      <TextLine id="r005-l001" index="0" custom="heights_v2:[76.1,28.7]">
        <Coords points="2548,489 2350,489 2319,488 1160,484 1160,589 1365,589 1560,589 1760,589 1955,589 2154,589 2350,594 2551,594 2745,589 2955,589 2955,484 2548,489"/>
        <Baseline points="1160,560 1365,560 1560,560 1760,560 1955,560 2155,560 2350,565 2550,565 2745,560 2955,560"/>
        <TextEquiv conf="0.965">
          <Unicode>Advokátní kancelář Mgr. Lukáš Kock</Unicode>
        </TextEquiv>
      </TextLine>
      <TextLine id="r005-l002" index="1" custom="heights_v2:[73.2,28.2]">
        <Coords points="3120,617 2875,617 2640,617 2407,612 2168,617 1940,617 1705,617 1472,612 1235,612 995,612 995,713 1235,713 1469,713 1705,718 1940,718 2171,718 2404,713 2640,718 2875,718 3120,718 3120,617"/>
        <Baseline points="995,685 1235,685 1470,685 1705,690 1940,690 2170,690 2405,685 2640,690 2875,690 3120,690"/>
        <TextEquiv conf="0.826">
          <Unicode>Rumunská 1, Praha 2 - Královské Vinohrady</Unicode>
        </TextEquiv>
      </TextLine>
      <TextLine id="r005-l004" index="2" custom="heights_v2:[61.6,20.7]">
        <Coords points="549,833 550,916 815,911 938,911 1325,906 1580,906 1840,906 2095,906 2350,906 2605,906 2875,906 2875,823 2605,823 2350,823 2095,823 1840,823 1580,823 1325,823 1069,828 815,828 549,833"/>
        <Baseline points="550,895 815,890 1070,890 1325,885 1580,885 1840,885 2095,885 2350,885 2605,885 2875,885"/>
        <TextEquiv conf="0.653">
          <Unicode>Mgr. Lukáš Kock, advokát kock(akkock.cz www.akkock.cz</Unicode>
        </TextEquiv>
      </TextLine>
    </TextRegion>
    <TextRegion id="r014">
      <Coords points="3130,816 3065,816 3065,910 3555,910 3555,816 3130,816"/>
      <TextLine id="r014-l003" index="0" custom="heights_v2:[69.3,24.5]">
        <Coords points="3065,816 3065,910 3130,910 3190,910 3250,910 3310,910 3365,910 3425,910 3485,910 3555,910 3555,816 3485,816 3425,816 3365,816 3310,816 3250,816 3190,816 3130,816 3065,816"/>
        <Baseline points="3065,885 3130,885 3190,885 3250,885 3310,885 3365,885 3425,885 3485,885 3555,885"/>
        <TextEquiv conf="0.946">
          <Unicode>tel: 724000123</Unicode>
        </TextEquiv>
      </TextLine>
    </TextRegion>
    <TextRegion id="r011">
      <Coords points="3030,1135 2712,1135 2716,1231 2824,1226 2925,1231 3045,1347 3045,1448 3655,1448 3655,1135 3030,1135"/>
      <TextLine id="r011-l005" index="0" custom="heights_v2:[69.7,26.4]">
        <Coords points="2712,1135 2716,1231 2824,1226 2925,1231 3030,1231 3130,1231 3235,1231 3335,1231 3440,1231 3540,1231 3655,1231 3655,1135 3540,1135 3440,1135 3335,1135 3235,1135 3130,1135 3030,1135 2712,1135"/>
        <Baseline points="2715,1205 2825,1200 2925,1205 3030,1205 3130,1205 3235,1205 3335,1205 3440,1205 3540,1205 3655,1205"/>
        <TextEquiv conf="0.974">
          <Unicode>Městský soud v Praze</Unicode>
        </TextEquiv>
      </TextLine>
      <TextLine id="r011-l006" index="1" custom="heights_v2:[69.8,28.2]">
        <Coords points="3240,1343 3315,1343 3380,1343 3445,1343 3510,1343 3577,1343 3652,1338 3645,1240 3570,1245 3510,1245 3445,1245 3380,1245 3315,1245 3240,1245 3240,1343"/>
        <Baseline points="3240,1315 3315,1315 3380,1315 3445,1315 3510,1315 3575,1315 3650,1310"/>
        <TextEquiv conf="1.000">
          <Unicode>Slezská 9</Unicode>
        </TextEquiv>
      </TextLine>
      <TextLine id="r011-l007" index="2" custom="heights_v2:[72.7,28.0]">
        <Coords points="3045,1448 3120,1448 3185,1448 3250,1448 3315,1448 3380,1448 3445,1448 3510,1448 3575,1448 3655,1448 3655,1347 3575,1347 3510,1347 3445,1347 3380,1347 3315,1347 3250,1347 3185,1347 3120,1347 3045,1347 3045,1448"/>
        <Baseline points="3045,1420 3120,1420 3185,1420 3250,1420 3315,1420 3380,1420 3445,1420 3510,1420 3575,1420 3655,1420"/>
        <TextEquiv conf="0.996">
          <Unicode>120 00 Praha 2</Unicode>
        </TextEquiv>
      </TextLine>
    </TextRegion>
    <TextRegion id="r012">
      <Coords points="2883,1648 2775,1648 2775,1727 3465,1732 3671,1727 3667,1648 2883,1648"/>
      <TextLine id="r012-l008" index="0" custom="heights_v2:[56.9,21.7]">
        <Coords points="2775,1648 2775,1727 2879,1727 2896,1728 3465,1732 3671,1727 3667,1648 3557,1653 3465,1653 3365,1653 3270,1653 3170,1653 3075,1653 2975,1653 2883,1648 2775,1648"/>
        <Baseline points="2775,1705 2880,1705 2975,1710 3075,1710 3170,1710 3270,1710 3365,1710 3465,1710 3560,1710 3670,1705"/>
        <TextEquiv conf="0.944">
          <Unicode>V Praze dne 28. 12. 2018</Unicode>
        </TextEquiv>
      </TextLine>
    </TextRegion>
    <TextRegion id="r000">
      <Coords points="510,2030 440,2030 440,2113 840,2108 840,2025 510,2030"/>
      <TextLine id="r000-l009" index="0" custom="heights_v2:[59.8,22.8]">
        <Coords points="440,2030 440,2113 602,2111 640,2108 700,2108 765,2108 840,2108 840,2025 589,2029 570,2030 510,2030 440,2030"/>
        <Baseline points="440,2090 510,2090 575,2090 640,2085 700,2085 765,2085 840,2085"/>
        <TextEquiv conf="1.000">
          <Unicode>Dlužník:</Unicode>
        </TextEquiv>
      </TextLine>
    </TextRegion>
    <TextRegion id="r002">
      <Coords points="567,2402 465,2402 465,2481 664,2476 1345,2481 1345,2402 567,2402"/>
      <TextLine id="r002-l014" index="0" custom="heights_v2:[58.4,21.3]">
        <Coords points="465,2402 465,2481 664,2476 1345,2481 1345,2402 567,2402 465,2402"/>
        <Baseline points="465,2460 570,2460 665,2455 760,2460 855,2460 950,2460 1045,2460 1140,2460 1235,2460 1345,2460"/>
        <TextEquiv conf="1.000">
          <Unicode>Zastoupený jednatelem:</Unicode>
        </TextEquiv>
      </TextLine>
    </TextRegion>
    <TextRegion id="r008">
      <Coords points="1480,2396 1470,2579 1680,2579 1865,2481 2070,2476 2070,2391 2281,2206 3285,2201 3285,2123 2675,2123 2470,2025 1475,2030 1480,2396"/>
      <TextLine id="r008-l010" index="0" custom="heights_v2:[59.8,21.2]">
        <Coords points="1603,2030 1587,2030 1475,2030 1476,2111 1591,2111 1700,2106 1810,2106 1915,2106 2025,2106 2135,2106 2240,2106 2350,2106 2470,2106 2470,2025 1603,2030"/>
        <Baseline points="1476,2090 1590,2090 1700,2085 1810,2085 1915,2085 2025,2085 2135,2085 2240,2085 2350,2085 2470,2085"/>
        <TextEquiv conf="0.928">
          <Unicode>Dental &amp; Esthetic Clinic s.r.0.</Unicode>
        </TextEquiv>
      </TextLine>
      <TextLine id="r008-l011" index="1" custom="heights_v2:[56.6,21.3]">
        <Coords points="3285,2123 3075,2123 2875,2123 2675,2123 2475,2123 2279,2128 2081,2123 1881,2118 1679,2123 1476,2123 1477,2201 1681,2201 1879,2196 2079,2201 2281,2206 2475,2201 2675,2201 2875,2201 3075,2201 3285,2201 3285,2123"/>
        <Baseline points="1477,2180 1680,2180 1880,2175 2080,2180 2280,2185 2475,2180 2675,2180 2875,2180 3075,2180 3285,2180"/>
        <TextEquiv conf="0.981">
          <Unicode>se sídlem: Těšnov 1163/5, Nové město, 110 00 Praha 1</Unicode>
        </TextEquiv>
      </TextLine>
      <TextLine id="r008-l012" index="2" custom="heights_v2:[64.2,24.6]">
        <Coords points="1480,2295 1545,2295 1600,2295 1653,2294 1710,2300 1765,2300 1820,2300 1875,2300 1930,2300 1995,2300 1995,2211 1930,2211 1875,2211 1820,2211 1765,2211 1710,2211 1661,2206 1600,2206 1545,2206 1480,2206 1480,2295"/>
        <Baseline points="1480,2270 1545,2270 1600,2270 1655,2270 1710,2275 1765,2275 1820,2275 1875,2275 1930,2275 1995,2275"/>
        <TextEquiv conf="0.538">
          <Unicode>IČ: 017 35 284,</Unicode>
        </TextEquiv>
      </TextLine>
      <TextLine id="r008-l013" index="3" custom="heights_v2:[63.7,21.1]">
        <Coords points="1475,2481 1547,2486 1610,2481 1675,2481 1740,2481 1800,2481 1865,2481 1961,2479 1995,2476 2070,2476 2070,2391 1995,2391 1925,2396 1865,2396 1800,2396 1740,2396 1675,2396 1610,2396 1540,2401 1480,2396 1475,2481"/>
        <Baseline points="1476,2460 1545,2465 1610,2460 1675,2460 1740,2460 1800,2460 1865,2460 1930,2460 1995,2455 2070,2455"/>
        <TextEquiv conf="0.996">
          <Unicode>Zdeněk Štěpánek,</Unicode>
        </TextEquiv>
      </TextLine>
      <TextLine id="r008-l015" index="4" custom="heights_v2:[65.2,23.6]">
        <Coords points="1470,2579 1575,2579 1680,2579 1680,2490 1575,2490 1475,2490 1470,2579"/>
        <Baseline points="1471,2555 1575,2555 1680,2555"/>
        <TextEquiv conf="0.997">
          <Unicode>Nar.:</Unicode>
        </TextEquiv>
      </TextLine>
    </TextRegion>
    <TextRegion id="r009">
      <Coords points="1549,2588 1475,2587 1475,2666 1745,2671 1745,2592 1549,2588"/>
      <TextLine id="r009-l016" index="0" custom="heights_v2:[57.6,21.2]">
        <Coords points="1475,2587 1475,2666 1543,2666 1566,2668 1745,2671 1745,2592 1670,2592 1610,2592 1549,2588 1475,2587"/>
        <Baseline points="1475,2645 1545,2645 1610,2650 1670,2650 1745,2650"/>
        <TextEquiv conf="0.999">
          <Unicode>Bytem:</Unicode>
        </TextEquiv>
      </TextLine>
    </TextRegion>
    <TextRegion id="r001">
      <Coords points="525,2790 451,2795 456,2866 650,2856 850,2856 850,2785 525,2790"/>
      <TextLine id="r001-l018" index="0" custom="heights_v2:[50.4,20.7]">
        <Coords points="451,2795 456,2866 525,2861 553,2861 650,2856 715,2856 775,2856 850,2856 850,2785 603,2788 586,2790 525,2790 451,2795"/>
        <Baseline points="455,2845 525,2840 590,2840 650,2835 715,2835 775,2835 850,2835"/>
        <TextEquiv conf="0.918">
          <Unicode>práv. zast.:</Unicode>
        </TextEquiv>
      </TextLine>
    </TextRegion>
    <TextRegion id="r007">
      <Coords points="1630,2775 1470,2775 1470,2951 2925,2946 2925,2869 2852,2775 1630,2775"/>
      <TextLine id="r007-l017" index="0" custom="heights_v2:[59.7,21.6]">
        <Coords points="1470,2775 1470,2857 1630,2857 1780,2857 1930,2857 2080,2857 2235,2857 2385,2857 2536,2857 2684,2852 2849,2857 2852,2775 2533,2775 2533,2775 2469,2775 1630,2775 1470,2775"/>
        <Baseline points="1470,2835 1630,2835 1780,2835 1930,2835 2080,2835 2235,2835 2385,2835 2535,2835 2685,2830 2850,2835"/>
        <TextEquiv conf="0.760">
          <Unicode>Mgr. Lukáš Kock, advokát, čak č. 163382,</Unicode>
        </TextEquiv>
      </TextLine>
      <TextLine id="r007-l019" index="1" custom="heights_v2:[55.8,21.5]">
        <Coords points="1470,2951 2375,2948 2435,2946 2595,2946 2755,2946 2925,2946 2925,2869 2755,2869 2595,2869 2435,2869 2273,2874 2115,2874 1955,2874 1795,2874 1635,2874 1470,2874 1470,2951"/>
        <Baseline points="1470,2930 1635,2930 1795,2930 1955,2930 2115,2930 2275,2930 2435,2925 2595,2925 2755,2925 2925,2925"/>
        <TextEquiv conf="0.970">
          <Unicode>se sídlem Na střelnici 522/6, 186 00 Praha 8</Unicode>
        </TextEquiv>
      </TextLine>
    </TextRegion>
    <TextRegion id="r003">
      <Coords points="480,4264 480,4359 2075,4354 2540,4364 2915,4269 3620,4269 3620,4191 480,4186 480,4264"/>
      <TextLine id="r003-l020" index="0" custom="heights_v2:[59.4,19.4]">
        <Coords points="3260,4269 3620,4269 3620,4191 3260,4191 2915,4191 2828,4189 480,4186 480,4264 835,4264 1180,4264 1530,4264 1875,4264 2220,4264 2570,4264 2915,4269 3260,4269"/>
        <Baseline points="480,4245 835,4245 1180,4245 1530,4245 1875,4245 2220,4245 2570,4245 2915,4250 3260,4250 3620,4250"/>
        <TextEquiv conf="0.661">
          <Unicode>Věc: Návrh dlužníka na zahájení insolvenčního řízení v souladu s §103 a násl. IZ a návrh</Unicode>
        </TextEquiv>
      </TextLine>
      <TextLine id="r003-l021" index="1" custom="heights_v2:[58.0,19.2]">
        <Coords points="480,4359 715,4354 940,4354 1083,4357 2075,4354 2540,4364 2541,4287 2301,4282 2076,4277 1849,4282 1620,4282 1395,4282 1170,4282 941,4277 715,4277 480,4282 480,4359"/>
        <Baseline points="480,4340 715,4335 940,4335 1170,4340 1395,4340 1620,4340 1850,4340 2075,4335 2300,4340 2540,4345"/>
        <TextEquiv conf="0.797">
          <Unicode>na stanovení řešení úpadku konkursem dle §148 a násl. IZ</Unicode>
        </TextEquiv>
      </TextLine>
    </TextRegion>
    <TextRegion id="r010">
      <Coords points="2673,5131 2545,5131 2545,5206 3645,5201 3645,5126 2673,5131"/>
      <TextLine id="r010-l022" index="0" custom="heights_v2:[53.8,21.3]">
        <Coords points="2545,5131 2545,5206 2691,5206 2795,5201 2915,5201 3035,5201 3155,5201 3275,5201 3395,5201 3515,5201 3645,5201 3645,5126 2673,5131 2545,5131"/>
        <Baseline points="2545,5185 2675,5185 2795,5180 2915,5180 3035,5180 3155,5180 3275,5180 3395,5180 3515,5180 3645,5180"/>
        <TextEquiv conf="1.000">
          <Unicode>Prostřednictvím datové schránky</Unicode>
        </TextEquiv>
      </TextLine>
    </TextRegion>
    <TextRegion id="r004">
      <Coords points="585,5452 525,5452 525,5533 585,5533 585,5452"/>
      <TextLine id="r004-l023" index="0" custom="heights_v2:[57.6,22.7]">
        <Coords points="525,5452 525,5533 585,5533 585,5452 525,5452"/>
        <Baseline points="525,5510 585,5510"/>
        <TextEquiv conf="0.990">
          <Unicode>o</Unicode>
        </TextEquiv>
      </TextLine>
    </TextRegion>
    <TextRegion id="r006">
      <Coords points="690,5456 615,5456 615,5637 625,5733 1830,5733 1956,5643 2279,5638 2510,5643 2591,5538 2588,5455 1973,5465 1487,5455 1250,5550 1096,5555 965,5456 690,5456"/>
      <TextLine id="r006-l025" index="0" custom="heights_v2:[59.2,22.2]">
        <Coords points="615,5456 615,5537 690,5537 755,5537 820,5537 885,5537 965,5537 965,5456 885,5456 820,5456 755,5456 690,5456 615,5456"/>
        <Baseline points="615,5515 690,5515 755,5515 820,5515 885,5515 965,5515"/>
        <TextEquiv conf="0.999">
          <Unicode>se sídlem</Unicode>
        </TextEquiv>
      </TextLine>
      <TextLine id="r006-l026" index="1" custom="heights_v2:[59.9,23.2]">
        <Coords points="2588,5455 2453,5460 2335,5460 2283,5460 1973,5465 1728,5460 1615,5460 1487,5455 1484,5538 1615,5543 1735,5543 1854,5543 1976,5548 2095,5543 2215,5543 2335,5543 2456,5543 2591,5538 2588,5455"/>
        <Baseline points="1485,5515 1615,5520 1735,5520 1855,5520 1975,5525 2095,5520 2215,5520 2335,5520 2455,5520 2590,5515"/>
        <TextEquiv conf="0.986">
          <Unicode>o zapsaný v seznamu advokátů</Unicode>
        </TextEquiv>
      </TextLine>
      <TextLine id="r006-l027" index="2" custom="heights_v2:[60.5,23.2]">
        <Coords points="2510,5643 2510,5560 2390,5560 2283,5555 2170,5555 2060,5555 1952,5560 1845,5560 1738,5555 1625,5555 1513,5550 1509,5633 1625,5638 1734,5638 1845,5643 1956,5643 2060,5638 2170,5638 2279,5638 2510,5643"/>
        <Baseline points="1510,5610 1625,5615 1735,5615 1845,5620 1955,5620 2060,5615 2170,5615 2280,5615 2390,5620 2510,5620"/>
        <TextEquiv conf="0.717">
          <Unicode>vedeném ČAK pod číslem</Unicode>
        </TextEquiv>
      </TextLine>
      <TextLine id="r006-l028" index="3" custom="heights_v2:[60.1,22.0]">
        <Coords points="615,5637 690,5637 760,5637 830,5637 895,5637 965,5637 1035,5637 1102,5637 1170,5632 1250,5632 1250,5550 1096,5555 1035,5555 965,5555 895,5555 830,5555 760,5555 690,5555 615,5555 615,5637"/>
        <Baseline points="615,5615 690,5615 760,5615 830,5615 895,5615 965,5615 1035,5615 1100,5615 1170,5610 1250,5610"/>
        <TextEquiv conf="0.962">
          <Unicode>Na střelnici 522/6</Unicode>
        </TextEquiv>
      </TextLine>
      <TextLine id="r006-l030" index="4" custom="heights_v2:[59.8,23.4]">
        <Coords points="765,5733 895,5733 1030,5733 1160,5733 1290,5733 1425,5733 1555,5733 1685,5733 1830,5733 1830,5650 1685,5650 1555,5650 1425,5650 1290,5650 1160,5650 1030,5650 895,5650 765,5650 625,5650 625,5733 765,5733"/>
        <Baseline points="625,5710 765,5710 895,5710 1030,5710 1160,5710 1290,5710 1425,5710 1555,5710 1685,5710 1830,5710"/>
        <TextEquiv conf="0.989">
          <Unicode>186 00 Praha 8, Karlín 16382</Unicode>
        </TextEquiv>
      </TextLine>
    </TextRegion>
    <TextRegion id="r013">
      <Coords points="2848,5533 2845,5639 3275,5649 3500,5644 3500,5558 3421,5461 3290,5466 2854,5451 2848,5533"/>
      <TextLine id="r013-l024" index="0" custom="heights_v2:[59.3,22.6]">
        <Coords points="3143,5461 3105,5461 3080,5459 2998,5456 2980,5456 2920,5456 2854,5451 2848,5533 2920,5538 2980,5538 3043,5538 3105,5543 3165,5543 3228,5543 3290,5548 3352,5548 3427,5543 3421,5461 3346,5466 3290,5466 3143,5461"/>
        <Baseline points="2850,5510 2920,5515 2980,5515 3045,5515 3105,5520 3165,5520 3230,5520 3290,5525 3350,5525 3425,5520"/>
        <TextEquiv conf="0.434">
          <Unicode>o DS: ecuound</Unicode>
        </TextEquiv>
      </TextLine>
      <TextLine id="r013-l029" index="1" custom="heights_v2:[61.8,24.4]">
        <Coords points="2845,5639 2925,5639 2993,5639 3065,5644 3135,5644 3203,5644 3275,5649 3377,5647 3415,5644 3500,5644 3500,5558 3415,5558 3341,5563 3275,5563 3209,5558 3135,5558 3065,5558 2999,5553 2925,5553 2848,5553 2845,5639"/>
        <Baseline points="2846,5615 2925,5615 2995,5615 3065,5620 3135,5620 3205,5620 3275,5625 3345,5625 3415,5620 3500,5620"/>
        <TextEquiv conf="0.539">
          <Unicode> IC: 691 82 604</Unicode>
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
