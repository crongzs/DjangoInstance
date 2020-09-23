# DjangoInstance
My Apps about some applications and configurations

* django_admin：django admin后台使用（配置、汉化）
* django_cross_origin：django跨域处理

## 在Ubuntu 16.04 安装python3.6 环境并设置为默认

* 安装3.6

~~~bash
sudo apt-get install software-properties-common
sudo add-apt-repository ppa:jonathonf/python-3.6
sudo apt-get update
sudo apt-get install python3.6
~~~

* 修改默认版本为python3.6

~~~bash
cd /user/bin
rm python
ln -s python3.6m python
~~~

* 升级pip版本

~~~bash
python pip install --upgrade pip
~~~

