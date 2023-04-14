# GPT 3.5 Discord chat bot

Welcome to my Discord chat bot project, which uses the GPT 3.5 Turbo Model from OpenAI to generate human-like responses. This bot is written in Python and is designed to be both simple and versatile.
## Features

This Discord chat bot has the following features:
- Uses the GPT 3.5 Turbo Model from OpenAI to generate human-like responses
- Responds to user input in Discord channels 
- Can be easily configured and customized with a `credentials.json` file 
- Easy to install and set up using the `requirements.txt` file
## Getting Started

To use the Discord chat bot, follow these steps:
1. Clone this repository to your local machine. 
2. Install the required dependencies by running the command `pip install -r requirements.txt` in your terminal or command prompt. 
3. Configure the bot by filling in the values in the `credentials.json` file. 
4. Run the bot by executing the `main.py` file using `python main.py` command in your terminal or command prompt.
## Configuration

To configure the bot, update the values in the `credentials.json` file with your own information:

```json

{
    "discord_bot_token": "<insert your bot token here>",
    "openai_api_key": "<insert your OpenAI API key here>",
    "owner_ids": [<insert your Discord user ID here>]
}
```



Make sure to keep your `credentials.json` file safe and secure, as it contains sensitive information.
## Video Tutorial

If you prefer a video tutorial, I've created one that will guide you through the process of setting up and using the Discord chat bot. You can watch it on [YouTube](https://www.youtube.com/watch?v=KmEvamVc750) .

## Contributing

We welcome contributions to this project. If you find a bug or have a feature request, please open an issue on GitHub. If you would like to contribute code, please fork the repository and create a pull request.
## License

This project is licensed under the MIT License.
