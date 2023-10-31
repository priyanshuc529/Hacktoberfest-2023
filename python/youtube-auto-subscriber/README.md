# YouTube Auto Subscriber
This is a Python program that automatically subscribes to YouTube channels. It utilizes Selenium library to automate the subscription process.

## Installation
1. Install the required packages by running the following command in the terminal:
```bash
pip install -r requirements.txt
```
2. Provide your Google account credentials in the `user_info.txt` file. The format should be as follows:
```txt
username = your_id
password = your_password
```
Note: Please ensure that you keep your credentials secure and do not share them with anyone.

3. Add the YouTube channel IDs of the channels you want to subscribe to in the `channel_ids.txt` file. The format should be as follows:
```txt
Channel_ID_1
Channel_ID_2
Channel_ID_3
...
Channel_ID_N
```
You can copy the YouTube channel ID by going to the channel's "About" tab and clicking on the arrow icon next to the "Share" button, then selecting "Copy channel ID".
![](image.png)

## Usage
To run the program, execute the `main.py` file. The program will automatically open a web browser, log in to your Google account, and start subscribing to the specified YouTube channels.

Please note that this program interacts with the YouTube website using automation techniques, which may violate Google or YouTube's terms of service. Use it responsibly and at your own risk.

## Disclaimer
This program is for educational purposes only. The developer does not take responsibility for any misuse or damage caused by the program. Use it responsibly and adhere to the terms of service of the websites you interact with.