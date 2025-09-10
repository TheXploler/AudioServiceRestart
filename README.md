# AudioServiceRestart
A simple python script to kill and restart the windows audio service (Audiosrv)

## Why?
<details>
<summary><b>TL;DR : I got tired of typing the same command over and over again</b></summary>
<br>
For some reason my laptop windows audio service keeps stopping randomly (probably it's because I mess around with audio a lot), That wasn't a big deal since I usually ran the troubleshooter, but then the old troubleshooter got replaced and integrated with the "Get Help" application in windows, which is such an absolute garbage of an application but I went though with it for a couple of months, and then it suddenly stopped working for some reason so I just said "fuck it" and I found out that the windows audio service (Audiosrv) stopped responding meaning it can't be stopped using the "services" application or task manager but it can be killed and restarted with a simple command, but then I got tired of typing the same command over and over again so here we are
<br><br>
I swear to god if it's not for Games, Ableton, and Adobe Premiere I would've moved back to my beloved Arch Linux
</details>



## Run
```bash
python "AudiosrvRestart.py"
```

## Contributing

All contributions are welcome!

If you face any issues or have a recommendation for a feature, don't hesitate to open a new issue, Thanks 😊

- Fandrest (TheXploler)

## License

[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)