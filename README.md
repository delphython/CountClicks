# Bitly shortener and clicks counter

Bitly shortener and clicks counter is a console utility that shortens links using Bitly URL shortener and counts clicks by Bitlink short URL.

## Requirements

Operating system: Microsoft Windows 7 or higher. Python3 should be installed. Use command line utility `cmd.exe` to run Python3 scripts.

## Prerequisites

Use `pip` to install dependences:
```bash
python -m pip install -r requirements.txt
```

## Installation
You have to set BITLY_API_KEY enviroment variable before use script. This is necessary to get access to Bitly API.

1. You have to get API Bitly token. Visit https://bitly.com/ and create a Bitly account. Then generate an [access token](https://bitly.is/accesstoken). It looks like "9b7934f7d7f422a6sddf92df0663197ff0409ed82". See [documentation](https://dev.bitly.com/) for instructions.
2. Copy your API Bitly token to .env file:
```
export BITLY_API_KEY="9b7934f7d7f422a6sddf92df0663197ff0409ed82"
```

## Usage example

How to shorten URL:
```sh
C:\PythonProjects\CountClicks>python main.py https://www.google.com
Bitlink https://bit.ly/3s50Az0
```

How to count clicks:
```sh
C:\PythonProjects\CountClicks>python main.py https://bit.ly/3s50Az0
Your URL clicks count: 2 time(s)
```
If URL to short is broken there will be error message:

```sh
C:\PythonProjects\CountClicks>python main.py www.gooble.com
Bitlink can't give short URL because URL www.gooble.com is broken!
```
if Bitlink URL is broken there will be error message:

```sh
C:\PythonProjects\CountClicks>python main.py https://bit.ly/3s50Az9
Bitlink can't give data about clicks because URL https://bit.ly/3s50Az9 is broken!
```

## Meta

Vitaly Klyukin – [@delphython](https://t.me/delphython) – [delphython@gmail.com](mailto:delphython@gmail.com)

[https://github.com/delphython](https://github.com/delphython/)
