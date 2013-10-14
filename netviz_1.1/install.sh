#!/bin/sh

cd ..

mv netviz_1.1 /opt/

cd /opt

mv netviz_1.1 netviz

ln -s netviz/netviz.py /usr/bin/netviz

exit
