# ---------------------- 可配置信息 ----------------------------#
# 配置信息
APPHOME=`pwd`/feedback
SERVERPORT=8080
NGINXDIR="/etc/nginx/conf.d/"
UWSGIPATH="/home/abelit/.local/bin"
USER="abelit"
GROUP="root"
# ---------------------- 可配置信息 ----------------------------#


# ---------------------- 无需改动信息 ----------------------------#
# Nginx配置
cp $APPHOME/nginx_example.conf $APPHOME/eqapp_nginx.conf
sed -i "s:{SERVERPORT}:$SERVERPORT:g" $APPHOME/eqapp_nginx.conf
sudo cp $APPHOME/eqapp_nginx.conf $NGINXDIR
# UWSGI配置
cp $APPHOME/uwsgi_example.ini $APPHOME/eqapp_uwsgi.ini
sed -i "s:{APPHOME}:$APPHOME:g" $APPHOME/eqapp_uwsgi.ini

# 系统服务配置
cp $APPHOME/eqapp_example.service $APPHOME/eqapp.service
sed -i "s:{APPHOME}:$APPHOME:g" $APPHOME/eqapp.service
sed -i "s:{UWSGIPATH}:$UWSGIPATH:g" $APPHOME/eqapp.service
sed -i "s:{USER}:$USER:g" $APPHOME/eqapp.service
sed -i "s:{GROUP}:$GROUP:g" $APPHOME/eqapp.service
sudo cp $APPHOME/eqapp.service /etc/systemd/system/eqapp.service
# ---------------------- 无需改动信息 ----------------------------#

