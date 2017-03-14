# About LOFTER
## 轻巧
LOFTER是一个用图片记录生活的网站。

主要用Flask开发，数据库使用MongoDB，具有简洁的界面和强大的后台管理。
## 随性
方便地记录照片、文字、音乐、视频，适用于iPhone、iPad和Android移动客户端及PC端。

方便同步你的内容到新浪微博、QQ空间等社交网络，还可以分享到微信、易信聊天和朋友圈。

让你随时随地的记录与分享。
</br>
## Demo
[LOFTER](deepdark.cc) is powered by LOFTER
## Dependency
### Backend
* Flask  
    * Flask-cript
    * Flask-login
    * Flask-admin
    * Flask-WTF
    * Flask-principal
    * Flask_mongoengine
* Mongoengine
* WTForms
* Markdown2
* Bleach
</br>

## How to run it ?
### Run by docker
#### First Run 
1.Get your LOFTER image
Pull LOFTER image from DockerHub:
```
(sudo) docker pull 0x0004/lofter:latest
```
2.Run LOFTER
```
(sudo) docker-compose up -d
```
Then you can visit LOFTER in your brower at `http://localhost`

#### After first run
Stop LOFTER
```
(sudo) docker-compose stop
```
Start LOFTER
```
(sudo) docker-compose start
```
### Get started with LOFTER
#### 1.Create a superuser to administrate LOFTER
Visit the following url and create a superuser.
```
http://localhost/accounts/registration/su
```
If the url is forbidden, you need to modify your configurations to allow the creation.
#### 2.Administrate LOFTER
The admin home is: `http://localhost/admin`
You will be redirected to login page if you haven't logged in.
#### 3.Modify the default configurations
You either change settings in `app/LOFTER/config.py` file, or set environment variables defined in that file.
#### Setting environment variables is recommended, and once the configuration is changed, you need to restart the service.
</br>

### 技术支持
如果你在部署和使用过程中有疑问，请给作者留言：

作者个人博客网站：http://deepdark.cc

微博：http://weibo.com/geeksunc 

知乎：https://www.zhihu.com/people/0x0004

### Enjoy it.:coffee::lollipop:
