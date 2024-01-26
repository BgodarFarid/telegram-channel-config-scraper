# telegram-channel-config-scraper
A Python script for automated collection and categorization of VPN settings from Telegram channels.
# telegram-channel-config-scraper
بله، حتما. اینجا یک README با جزئیات بیشتر برای کد شما است:

```markdown
# Telegram Channel Configurations Scraper

This Python script allows you to scrape Telegram channels for VPN configurations. It supports various protocols such as V2Ray, Shadowsocks, and more. The script categorizes the obtained configurations based on their protocols and saves them in separate text files for easy access.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Configuration Files](#configuration-files)
- [Channels](#channels)
- [Customization](#customization)
- [Notes](#notes)
- [Disclaimer](#disclaimer)

## Overview

Telegram channels are a popular platform for sharing VPN configurations. This script simplifies the process of collecting and categorizing these configurations, making it easier for users to find and use them.

## Features

- **Multi-Protocol Support**: The script supports various VPN protocols, including V2Ray, Shadowsocks, Trojan, and VLESS.

- **Channel Scraping**: It fetches the latest messages from specified Telegram channels, even considering channels with more than 100 messages.

- **Configuration Categorization**: Configurations are organized into separate files based on the protocol type.

- **Easy Customization**: Users can easily customize the list of channels and protocols based on their preferences.

## Getting Started

1. **Install Dependencies**:

   ```bash
   pip install requests beautifulsoup4
   ```

2. **Run the Script**:

   ```bash
   python main.py
   ```

## Usage

1. Run the script using the instructions provided in the "Getting Started" section.

2. The script will fetch the latest configuration messages from the specified Telegram channels.

3. Configurations will be saved in separate text files based on the protocol type.

## Configuration Files

The script generates the following configuration files:

- `ss_iran.txt`: Shadowsocks configurations for Iran.
- `vmess_iran.txt`: V2Ray VMess configurations for Iran.
- `trojan_iran.txt`: Trojan configurations for Iran.
- `vless_iran.txt`: VLESS configurations for Iran.
- `mixed_iran.txt`: Mixed configurations containing all protocols for Iran.

## Channels

The script currently scrapes configurations from the following Telegram channels:

- [Channel 1](https://t.me/s/channel1)
- [Channel 2](https://t.me/s/channel2)
- ...

## Customization

Feel free to customize the `channels` list in the script to add or remove channels based on your preferences.

## Notes

- The script fetches the latest messages from each channel, ensuring that even channels with more than 100 messages are considered.

- Configuration messages are saved in separate text files, making it convenient to access and use them.

## Disclaimer

This script is intended for educational purposes only. Use it responsibly and comply with the terms of service of the Telegram platform.

```
