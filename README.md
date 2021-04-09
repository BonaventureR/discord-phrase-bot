<h3> Discord Random Phrase Bot </h3>


This script allows you to run a discord bot that says phrases at random intervals based on the count of messages. 


Create a .env file and configure the settings to have these variables.
```
DISCORD_TOKEN={Insert Discord Token}
DISCORD_GUILD={Insert Discord Channel}
```

In the PogClient class, you'll see messages which is where you can populate the random messages that you wish to show.

"Spammer Alert" is created for people who are cringe and like to spam messages to force the bot to say something.

Currently the RNG is set to between 750 and 1500, change this to whatever your heart so desires by editing the rng_lowerbound and rng_upperbound variables.
