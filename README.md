# Sites Monitoring Utility

This utility is monitoring site "health" (HTTP Status and expiration date). You need text file with correct URLs one per row. 

Example of URLs list to check.

File name url.txt
```
http://ya.ru
http://vk.com
http://google.com
http://mail.ru
```

# Quickstart

Example

```
check_sites_health.py c:\1\url.txt
URL:http://ya.ru | Status:200 | Expired in:354 days, 3:11:55.343863
URL:http://vk.com | Status:200 | Expired in:315 days, 10:11:51.921521
URL:http://google.com | Status:200 | Expired in:1129 days, 10:11:50.085337
URL:http://foo.bar | Status:Error | Expired in:N/A
URL:http://mail.ru | Status:200 | Expired in:50 days, 3:11:44.264755
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
