<p align="center">
  <img src="./LOCAL/Wavy_Lst-14_Single-06.jpg" alt="VideoConvertor poster">
</p>
<h1 align="center">
  <b>ᴠɪᴅᴇᴏ ᴄᴏɴᴠᴇʀᴛᴏʀ</b>
</h1>


<p align="left"><a href="https://github.com/vasusen-code/videoconvertor"><img src="https://github-readme-stats.vercel.app/api/pin?username=vasusen-code&show_icons=true&theme=dracula&hide_border=true&repo=VideoConvertor"></a></p>
  

Variables required are:
* `API_ID`

* `API_HASH`

* `BOT_TOKEN`

* `LOG_CHANNEL` - Log channel `username`
  
* `LOG_ID` - Log channel `id` `[Should be Public]`

* `ACCESS_CHANNEL` - Input access channel/group `id` [`SHOULD BE PRIVATE GROUP`]

* `FORCESUB` - Channel/group `id` to which u want user be forced to subscribe.

* `MONGODB_URI`

* `AUTH_USERS` - Bot owner `UserId`.

* `FORCESUB_UN` - Username of your forcesub channel.

* `BOT_UN` - Username of yout Bot.
  
* `HEROKU_API` - Your heroku api, you can get it from heroku account settings(optional, add only if you want to restart directly from tg.)

* `HEROKU_APP_NAME` - Your heroku app name(optional, add only if you want to restart directly from tg.)
               
AUTH_USERS COMMANDS:
  
  - `/disallow <id>` : to ban
  - `/allow <id>` : to unban
  - `/users` : count total users
  - `/msg <id>` : give this command replying to a message
  - `/bcast` : Reply to any kind of message to broadcast it
  - `menu` >> `settings` >>  `restart`
  
Deploy your own bot on heroku.

`Warning` - There are two different branches available, look(above) which one you want to deploy. Go to `main` branch if you need bot for your `personal` needs.
  
<p><a href="https://heroku.com/deploy"> <img src="https://img.shields.io/badge/Deploy%20To%20Heroku-black?style=for-the-badge&logo=heroku" width="250""/></a></p>

`Alternate way:`

If facing any problem while deploying through heroku button, just fork and deploy manually by creating a new app in heroku.
Add this buildpack if deploying manually: 
- `https://github.com/jonathanong/heroku-buildpack-ffmpeg-latest.git`
- `heroku/python`

LICENSE:

[![License](https://www.gnu.org/graphics/gplv3-127x51.png)](LICENSE)

