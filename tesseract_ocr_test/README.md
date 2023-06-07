Introduction
Tesseract is an open source text recognition (OCR) Engine, available under the Apache 2.0 license. It can be used directly, or (for programmers) using an API to extract printed text from images. It supports a wide variety of languages.

Tesseract doesn't have a built-in GUI, but there are several available from the 3rdParty page.

Installation
There are two parts to install, the engine itself, and the traineddata for the languages.

Tesseract is available directly from many Linux distributions. The package is generally called 'tesseract' or 'tesseract-ocr' - search your distribution's repositories to find it.

Packages for over 130 languages and over 35 scripts are also available directly from the Linux distributions. The language traineddata packages are called 'tesseract-ocr-langcode' and 'tesseract-ocr-script-scriptcode', where langcode is three letter language code and scriptcode is four letter script code.

Examples: tesseract-ocr-eng (English), tesseract-ocr-ara (Arabic), tesseract-ocr-chi-sim (Simplified Chinese), tesseract-ocr-script-latn (Latin Script), tesseract-ocr-script-deva (Devanagari script), etc.

Ubuntu
You can install Tesseract and its developer tools on Ubuntu by simply running:

sudo apt install tesseract-ocr
sudo apt install libtesseract-dev