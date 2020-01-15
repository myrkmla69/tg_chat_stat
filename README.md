# Statistic of Personal Chats Telegram &middot; [![GitHub license](https://img.shields.io/badge/license-ISC-blue.svg?style=flat-square)](https://github.com/andrey18106/tg_chat_stat/blob/master/LICENSE)
> For now only Windows is currently supported.

To analyze chats, you need to [export your data](https://telegram.org/blog/export-and-more) (only personal chats without files) from Telegram Desktop (JSON) and select export from the list in program.

## Getting started

A quick introduction of the minimal setup you need to get running.

If you already installed [python](https://www.python.org/downloads/) you need to install `pyinstaller` to compile (*.exe) the current verison of the console application.

In command line (`Win + R -> cmd`):

```shell
pip install pyinstaller
```

Next we clone the repository and compiling the console application using `pyinstaller`.

```shell
git clone https://github.com/andrey18106/tg_chat_stat.git
cd tg_chat_stat/
pyinstaller -F tg_chat_stat.py
```

Key `-F` creates a one-file bundled executable.

## Tasks

There is some list of tasks is needed to do:

- [x] Search and select export files
- [x] The number of messages from each of the participants and in total;
- [x] Number of characters in messages from each of the partocopants and in total;
- [x] Number of individual words from each of the participants and in total;
- [x] Number of voice messages from each of the participants and in total;
- [x] Number of round videos from each of the participants and in total;
- [ ] Number of periods / commas / slashes / hyphens / colons / question marks / exclamation marks;
- [ ] Number of replies (messages that are sent to another);
- [ ] Number of popular words: “ok”, “dad”, “nit”, “good”, “sho”;
- [ ] The average number of characters in the message;
- [ ] The average number of words in a message;
- [ ] The average number of messages per day.