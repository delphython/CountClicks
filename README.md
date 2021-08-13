# Bitly shortener and clicks counter

Bitly shortener and clicks counter is a console utility that shortens links using Bitly URL shortener and counts clicks by Bitlink short URL.

## Requirements

Operating system: Microsoft Windows 7 or higher. Python3 should be installed. Use command line utility `cmd.exe` to run Python3 scripts.

## Prerequisites

Use `pip` to install dependences:
```bash
python -m pip install -r requirements.txt
```

## Usage example

How to shorten URL:
```sh
C:\PythonProjects\CountClicks>python main.py https://www.google.com
Битлинк https://bit.ly/3s50Az0
```

How to count clicks:
```sh
C:\PythonProjects\CountClicks>python main.py https://bit.ly/3s50Az0
По вашей ссылке прошли 2 раз(а)
```
If URL to short is broken there will be error message:

```sh
C:\PythonProjects\CountClicks>python main.py www.gooble.com
Bitlink can't give short URL because URL www.gooble.com is broken!
```
if Bitlink URL is broken there will be error message:

```sh
C:\PythonProjects\CountClicks>python main.py https://bit.ly/3s50Az9
Bitlink can't give short URL because URL https://bit.ly/3s50Az9 is broken!
```

## Meta

Vitaly Klyukin – [@delphython](https://t.me/delphython) – [delphython@gmail.com](mailto:delphython@gmail.com)

[https://github.com/delphython](https://github.com/delphython/)
