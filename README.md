# LibreOffice Calc - Binance API Extension

This is a simple LibreOffice Calc extension that provides `YAHOOPRICE`, `YAHOOHIGHPRICE`, `YAHOOLOWPRICE`,
`YAHOOVOLUME` functions from Yahoo Finance.

## Install

Download the latest plugin from the [Releases page][releases]. Make sure you
grab the `YahooApi.oxt` and not the source code downloads.

In LibreOffice, go to `Tools -> Extension Manager -> Add` and select the
`YahooApi.oxt` file you downloaded. Restart LibreOffice when prompted.

## Usage

Simply pass your trading symbol to the functions:

    =YAHOOPRICE("KRDMD.IS")      // Current price of KRDMD.IS
    =YAHOOHIGHPRICE("KRDMD.IS")  // Highest price of KRDMD.IS in last 24 hr
    =YAHOOLOWPRICE("KRDMD.IS")   // Lowest price of KRDMD.IS in last 24 hr
    =YAHOOVOLUME("KRDMD.IS")     // Volume in last 24 hr

## Build

If you want to build the plugin yourself, you need to install `7zip`, `make`,
`python`, & the libreoffice-sdk.

Then you can just run `make` to generate `YahooApi.oxt`.


## LICENSE

GPL-3.0
