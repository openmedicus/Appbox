#!/bin/bash

#shopt -s extglob

FROM=$1
TO=$2
ARCH=$3

echo "Install Framework $FROM"

# BIN directory
mkdir $TO/bin
cp $FROM/bin/dbus-daemon.exe $TO/bin/
cp $FROM/bin/dbus-launch.exe $TO/bin/
cp $FROM/bin/dbus-send.exe $TO/bin/
cp $FROM/bin/gdk-pixbuf-query-loaders.exe $TO/bin/
cp $FROM/bin/gtk-query-immodules-3.0.exe $TO/bin/

cp $FROM/bin/*.dll $TO/bin/
cp $TO/bin/libintl-8.dll $TO/bin/intl.dll
cp $TO/bin/libsqlite3-0.dll $TO/bin/libsqlite3.dll
cp $TO/bin/libsqlite3-0.dll $TO/bin/sqlite3.dll
#cp $TO/bin/libgphoto2-sharp.dll $TO/bin/libgphoto2.dll

#cp $FROM/bin/sane-find-scanner.exe $TO/bin/

# ETC directory
mkdir $TO/etc
cp -r $FROM/etc/dbus-1 $TO/etc/
cp -r $FROM/etc/fonts $TO/etc/
cp -r $FROM/etc/gtk-3.0 $TO/etc/
cp -r $FROM/etc/pki $TO/etc/
#cp -r $FROM/etc/sane.d $TO/etc/

# LIB directory
mkdir $TO/lib
cp -r $FROM/lib/enchant $TO/lib/
cp -r $FROM/lib/engines-1_1 $TO/lib/
cp -r $FROM/lib/gdk-pixbuf-2.0 $TO/lib/
cp -r $FROM/lib/gio $TO/lib/
cp -r $FROM/lib/gstreamer-1.0 $TO/lib/
cp -r $FROM/lib/gtk-3.0 $TO/lib/
#cp -r $FROM/lib/libgphoto2 $TO/lib/
#mv $TO/lib/libgphoto2/print-camera-list.exe $TO/bin/
#cp -r $FROM/lib/libgphoto2_port $TO/lib/

# SHARE directory
mkdir $TO/share
cp -r $FROM/share/dbus-1 $TO/share/
touch $TO/share/dbus-1/session.d/empty
mkdir $TO/share/glib-2.0
cp -r $FROM/share/glib-2.0/schemas $TO/share/glib-2.0/

mkdir -p $TO/share/icons/Adwaita
cp -r $FROM/share/icons/Adwaita/16x16 $TO/share/icons/Adwaita/
cp -r $FROM/share/icons/Adwaita/24x24 $TO/share/icons/Adwaita/
cp -r $FROM/share/icons/Adwaita/32x32 $TO/share/icons/Adwaita/
cp -r $FROM/share/icons/Adwaita/48x48 $TO/share/icons/Adwaita/
cp $FROM/share/icons/Adwaita/index.theme $TO/share/icons/Adwaita/

mkdir -p $TO/share/locale
cp -r $FROM/share/locale/da $TO/share/locale/
cp -r $FROM/share/locale/sv $TO/share/locale/

cp -r $FROM/share/myspell $TO/share/

# REMOVE FOR BUILDIN
rm -f $TO/bin/System.DirectoryServices.AccountManagement.dll
rm -f $TO/bin/System.DirectoryServices.dll
rm -f $TO/bin/System.Security.Principal.Windows.dll

# HACK: Override System.Drawing.Common.dll
cp -f dll/System.Drawing.Common.dll $TO/bin/
 
