alpha-png
=========

Create transparent PNGs quickly for repeating backgrounds in web design. `rgba()` is awesome, but it sadly does not work in the old browsers... specifically IE8. I'll leave it up to you to decide if you want to support IE8, but sometimes you don't have a choice. There are a ton of fallbacks, but the repeating, transparent PNG is pretty solid through and through.

This app allows you to specify a HEX value and an alpha value (in percentage), which then converts your hexidecimal values to RGB values and builds a 1x1 pixel png and downloads as an attachment in your browser. The app is built on [Flask](http://flask.pocoo.org/), a python microframework, and [pypng](https://github.com/drj11/pypng), a pure python library for PNG image encoding and decoding.

```CSS
div {
  background:url(img/transparent-image.png) repeat; /* fallback */
  background:rgba(x, x, x, x); /* main style */
}
```

## Setup

*This will eventually be an available web-app, but for now you must install locally. Sorry!*

1. Start your virtualenv with `. venv/bin/activate`
2. In command line run `python app.py`
3. Head to `localhost:5000`
