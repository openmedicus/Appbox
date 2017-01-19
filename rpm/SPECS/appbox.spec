%define MINGW_FILESYSTEM_VERSION 101
%define BINUTILS_VERSION 2.26
%define HEADER_CRT_THREAD_VERSION 5.0.0
%define COMPILER_VERSION 6.3.0
%define PKG_CONFIG_VERSION 0.28
%define TERMCAP_VERSION 1.3.1
%define ZLIB_VERSION 1.2.8
%define ICONV_VERSION 0.0.6
%define GETTEXT_VERSION 0.19.7
%define LIBFFI_VERSION 3.0.13
%define GLIB2_VERSION 2.50.1
%define PIXMAN_VERSION 0.34.0
%define BZIP2_VERSION 1.0.6
%define FREETYPE_VERSION 2.6
%define EXPAT_VERSION 2.2.0
%define FONTCONFIG_VERSION 2.12.1
%define LIBPNG_VERSION 1.6.27
%define LIBJPEG_TURBO_VERSION 1.5.1
%define LIBTIFF_VERSION 4.0.3
%define CAIRO_VERSION 1.14.6
%define ICU_VERSION 57.1
%define HARFBUZZ_VERSION 1.3.2
%define PANGO_VERSION 1.40.3
%define ATK_VERSION 2.22.0
%define JASPER_VERSION 1.900.1
%define LIBXML2_VERSION 2.9.3
%define LIBCROCO_VERSION 0.6.11
%define LIBRSVG2_VERSION 2.40.16
%define GDK_PIXBUF_VERSION 2.36.0
%define GTK3_VERSION 3.22.2
%define GTK3_ADWAITA_VERSION 3.14.1
%define GDL_VERSION 3.22.0

%define NSIS_VERSION 2.46

%define GTK_MAC_BUNDLER_VERSION 0.5
%define GTK_MAC_INTEGRATION_VERSION 0.9

%define LIBGPG_ERROR_VERSION 1.22
%define LIBGCRYPT_VERSION 1.6.3
%define GMP_VERSION 6.1.1
%define NETTLE_VERSION 3.3
%define P11_KIT_VERSION 0.23.2
%define LIBTASN1_VERSION 4.9
%define READLINE_VERSION 6.2
%define GNUTLS_VERSION 3.5.5
%define GLIB_NETWORKING_VERSION 2.50.0

%define LIBXSLT_VERSION 1.1.28
%define SQLITE_VERSION 3.12.2
%define LIBSOUP_VERSION 2.56.0

%define HUNSPELL_VERSION 1.3.2
%define ENCHANT_VERSION 1.6.0

%define LIBOGG_VERSION 1.3.2
%define LIBVORBIS_VERSION 1.3.4
%define LIBWEBP_VERSION 0.5.2
%define GSTREAMER1_VERSION 1.10.0
%define GSTREAMER1_PLUGINS_BASE_VERSION 1.10.0
%define GSTREAMER1_PLUGINS_GOOD_VERSION 1.10.0
%define GSTREAMER1_PLUGINS_BAD_VERSION 1.10.0
%define WEBKITGTK3_VERSION 2.4.11
%define LIBEXIF_VERSION 0.6.20

%define DBUS_VERSION 1.8.16
%define DBUS_GLIB_VERSION 0.108

%define MONO_VERSION 4.8.0
%define NPGSQL_VERSION 3.1.9
%define GTK3_SHARP_VERSION 3.22.2
%define GDL_SHARP_VERSION 3.22.0
%define MONO_ZEROCONF_VERSION 0.9.0
%define MONO_ADDINS_VERSION 1.3
%define WEBKITGTK3_SHARP_VERSION 2.4.11
%define DBUS_SHARP_VERSION 0.9.0
%define DBUS_SHARP_GLIB_VERSION 0.6.0
%define GSTREAMER1_SHARP_VERSION 1.39.91
%define NEWTONSOFT_JSON_VERSION 9.0.1
%define PUSH_SHARP_VERSION 4.0.10
%define NHAPI_VERSION 2.3.1
%define OSMSHARP_VERSION 4.2.0
%define GTK_MAC_INTEGRATION_SHARP_VERSION 0.9

Summary: 		Easy management of applications
Name: 			appbox
Version:		2.2
Release:		3%{?dist}
License:		GPL
Group: 			Applications/Desktop
Source0: 		%{name}-0.1.tar.bz2
Source1:		yum_ignoreos.conf
Source2:		yum_ignoreos.py
Source3:		appbox.repo
Source4:		RPM-GPG-KEY-appbox
Source5:		macros.darwinx
Source6:		darwinx-cmake
Source7:		darwinx-configure 
Source8:		darwinx-make
Source9:		darwinx-pkg-config
URL:			http://www.appbox.info
Vendor:			Appbox
Packager:		Mikkel Kruse Johnsen <mikkel@appbox.info>
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:		noarch

Requires:		appbox-runtime = %{version}

#BuildRequires:		mono-devel >= %{MONO_VERSION}
#BuildRequires:		gtk-sharp3-devel >= %{GTK3_SHARP_VERSION}
#BuildRequires:		webkitgtk3-sharp >= %{WEBKITGTK3_SHARP_VERSION}

%description
Easy management of applications


%package release
Summary:                Runtime environment for AppBox
License:                GPL
Group:                  Applications/Desktop
BuildArch:              noarch

%description release
Easy management of applications


%package runtime
Summary: 		Runtime environment for AppBox
License:		GPL
Group: 			Applications/Desktop
BuildArch:		noarch

Requires:		mono-core >= %{MONO_VERSION}
Requires:		mono-extras >= %{MONO_VERSION}
Requires:		mono-locale-extras >= %{MONO_VERSION}
Requires:		mono-data >= %{MONO_VERSION}
Requires:		mono-data-sqlite >= %{MONO_VERSION}
Requires:		mono-data-npgsql >= %{NPGSQL_VERSION}
Requires:		mono-web >= %{MONO_VERSION}
Requires:		mono-wcf >= %{MONO_VERSION}
Requires:		mono-winfxcore >= %{MONO_VERSION}

Requires:		mono-addins >= %{MONO_ADDINS_VERSION}
Requires:		mono-zeroconf >= %{MONO_ZEROCONF_VERSION}
Requires:		dbus-sharp >= %{DBUS_SHARP_VERSION}
Requires:		dbus-sharp-glib >= %{DBUS_SHARP_GLIB_VERSION}

Requires:		libcroco >= %{LIBCROCO_VERSION}
Requires:		librsvg2 >= %{LIBRSVG2_VERSION}
Requires:		gtk3 >= %{GTK3_VERSION}
Requires:		adwaita-icon-theme >= %{GTK3_ADWAITA_VERSION}
Requires:		gtk-sharp3 >= %{GTK3_SHARP_VERSION}

Requires:		libgdl >= %{GDL_VERSION}
Requires:		gdl-sharp >= %{GDL_SHARP_VERSION}

Requires:		libsoup >= %{LIBSOUP_VERSION}
Requires:		hunspell >= %{HUNSPELL_VERSION}
Requires:		enchant >= %{ENCHANT_VERSION}
Requires:		webkitgtk3 >= %{WEBKITGTK3_VERSION}
Requires:		webkitgtk3-sharp >= %{WEBKITGTK3_SHARP_VERSION}

Requires:		libogg => %{LIBOGG_VERSION}
Requires:		libvorbis => %{LIBVORBIS_VERSION}
Requires:		libwebp => %{LIBWEBP_VERSION}
Requires:		gstreamer1 => %{GSTREAMER1_VERSION}
Requires:		gstreamer1-plugins-base >= %{GSTREAMER1_PLUGINS_BASE_VERSION}
Requires:		gstreamer1-plugins-good >= %{GSTREAMER1_PLUGINS_GOOD_VERSION}
Requires:		gstreamer1-plugins-bad-free >= %{GSTREAMER1_PLUGINS_BAD_VERSION}
Requires:		gstreamer1-sharp >= %{GSTREAMER1_SHARP_VERSION}

Requires:		libexif >= %{LIBEXIF_VERSION}
#Requires:		libgphoto2 >= %{LIBGPHOTO2_VERSION}
#Requires:		libgphoto2-sharp >= %{LIBGPHOTO2_SHARP_VERSION}

Requires:		NHapi => %{NHAPI_VERSION}
Requires:		PushSharp >= %{PUSH_SHARP_VERSION}
Requires:		Newtonsoft.Json >= %{NEWTONSOFT_JSON_VERSION}
Requires:		OsmSharp >= %{OSMSHARP_VERSION}

%description runtime
Easy management of applications




%package sdk
Summary: 		SDK for AppBox
License:		GPL
Group: 			Applications/Desktop
BuildArch:		noarch

Requires:		appbox-runtime = %{version}

Requires:		gnome-common intltool glib2-devel redhat-rpm-config

Requires:		mono-zeroconf-devel
Requires:		gtk-sharp3-devel gtk-sharp3-gapi
Requires:		gstreamer1-sharp-devel

#Requires:		libgphoto2-sharp-devel

Requires:		gnome-sharp
Requires:		monodevelop
Requires:		xsp


%description sdk
Easy management of applications




%package sdk-mingw32
Summary:                SDK for AppBox Mingw 32 bit
License:                GPL
Group:                  Applications/Desktop
BuildArch:              noarch


Requires:               mingw32-winpthreads >= %{HEADER_CRT_THREAD_VERSION}
Requires:               mingw32-termcap >= %{TERMCAP_VERSION}
Requires:               mingw32-zlib >=	%{ZLIB_VERSION}
Requires:               mingw32-win-iconv >= %{ICONV_VERSION}
Requires:               mingw32-gettext >= %{GETTEXT_VERSION}
Requires:               mingw32-libffi >= %{LIBFFI_VERSION}
Requires:               mingw32-glib2 >= %{GLIB2_VERSION}
Requires:               mingw32-pixman >= %{PIXMAN_VERSION}
Requires:               mingw32-bzip2 >= %{BZIP2_VERSION}
Requires:               mingw32-freetype >= %{FREETYPE_VERSION}
Requires:               mingw32-expat >= %{EXPAT_VERSION}
Requires:               mingw32-fontconfig >= %{FONTCONFIG_VERSION}
Requires:               mingw32-libpng >= %{LIBPNG_VERSION}
Requires:               mingw32-libjpeg-turbo >= %{LIBJPEG_TURBO_VERSION}
Requires:               mingw32-libtiff >= %{LIBTIFF_VERSION}
Requires:               mingw32-cairo >= %{CAIRO_VERSION}
Requires:               mingw32-icu >= %{ICU_VERSION}
Requires:               mingw32-harfbuzz >= %{HARFBUZZ_VERSION}
Requires:               mingw32-pango >= %{PANGO_VERSION}
Requires:               mingw32-atk >= %{ATK_VERSION}
Requires:               mingw32-jasper >= %{JASPER_VERSION}
Requires:               mingw32-libxml2 >= %{LIBXML2_VERSION}
Requires:               mingw32-gdk-pixbuf >= %{GDK_PIXBUF_VERSION}
Requires:               mingw32-libcroco >= %{LIBCROCO_VERSION}
Requires:               mingw32-librsvg2 >= %{LIBRSVG2_VERSION}
Requires:               mingw32-gtk3 >= %{GTK3_VERSION}
Requires:               mingw32-adwaita-icon-theme >= %{GTK3_ADWAITA_VERSION}
Requires:               mingw32-gdl >= %{GDL_VERSION}

Requires:               mingw32-libgpg-error >= %{LIBGPG_ERROR_VERSION}
Requires:               mingw32-libgcrypt >= %{LIBGCRYPT_VERSION}
Requires:               mingw32-gmp >= %{GMP_VERSION}
Requires:               mingw32-nettle >= %{NETTLE_VERSION}
Requires:               mingw32-p11-kit >= %{P11_KIT_VERSION}
Requires:               mingw32-libtasn1 >= %{LIBTASN1_VERSION}
Requires:               mingw32-readline >= %{READLINE_VERSION}
Requires:               mingw32-gnutls 	>= %{GNUTLS_VERSION}
Requires:               mingw32-glib-networking >= %{GLIB_NETWORKING_VERSION}

Requires:               mingw32-libxslt >= %{LIBXSLT_VERSION}
Requires:               mingw32-sqlite >= %{SQLITE_VERSION}
Requires:               mingw32-libsoup >= %{LIBSOUP_VERSION}

Requires:               mingw32-hunspell >= %{HUNSPELL_VERSION}
Requires:               mingw32-enchant >= %{ENCHANT_VERSION}

Requires:               mingw32-libogg >= %{LIBOGG_VERSION}
Requires:               mingw32-libvorbis >= %{LIBVORBIS_VERSION}
Requires:               mingw32-libwebp >= %{LIBWEBP_VERSION}
Requires:               mingw32-gstreamer1 >= %{GSTREAMER1_VERSION}
Requires:               mingw32-gstreamer1-plugins-base >= %{GSTREAMER1_PLUGINS_BASE_VERSION}
Requires:               mingw32-gstreamer1-plugins-good >= %{GSTREAMER1_PLUGINS_GOOD_VERSION}
Requires:               mingw32-gstreamer1-plugins-bad-free >= %{GSTREAMER1_PLUGINS_BAD_VERSION}
Requires:               mingw32-webkitgtk3 >= %{WEBKITGTK3_VERSION}

Requires:               mingw32-dbus >= %{DBUS_VERSION}
Requires:               mingw32-dbus-glib >= %{DBUS_GLIB_VERSION}

Requires:               mingw32-mono >= %{MONO_VERSION}
Requires:               mingw32-mono-data-npgsql >= %{NPGSQL_VERSION}
Requires:               mingw32-gtk-sharp3 >= %{GTK3_SHARP_VERSION}
Requires:               mingw32-gdl-sharp >= %{GDL_SHARP_VERSION}
Requires:               mingw32-mono-zeroconf >= %{MONO_ZEROCONF_VERSION}
Requires:               mingw32-mono-addins >= %{MONO_ADDINS_VERSION}
Requires:               mingw32-webkitgtk3-sharp >= %{WEBKITGTK3_SHARP_VERSION}
Requires:               mingw32-dbus-sharp >= %{DBUS_SHARP_VERSION}
Requires:               mingw32-dbus-sharp-glib >= %{DBUS_GLIB_SHARP_VERSION}
Requires:		mingw32-gstreamer1-sharp >= %{GSTREAMER1_SHARP_VERSION}
Requires:		mingw32-newtonsoft-json >= %{NEWTONSOFT_JSON_VERSION}
#Requires:		mingw32-SharpSSH >= %{SHARP_SSH_VERSION}

%description sdk-mingw32
Easy management of applications for Windows 32 bit



%package sdk-mingw64
Summary:                SDK for AppBox Mingw 64 bit
License:                GPL
Group:                  Applications/Desktop
BuildArch:              noarch

Requires:               mingw64-winpthreads >= %{HEADER_CRT_THREAD_VERSION}
Requires:               mingw64-termcap >= %{TERMCAP_VERSION}
Requires:               mingw64-zlib >= %{ZLIB_VERSION}
Requires:               mingw64-win-iconv >= %{ICONV_VERSION}
Requires:               mingw64-gettext >= %{GETTEXT_VERSION}
Requires:               mingw64-libffi >= %{LIBFFI_VERSION}
Requires:               mingw64-glib2 >= %{GLIB2_VERSION}
Requires:               mingw64-pixman >= %{PIXMAN_VERSION}
Requires:               mingw64-bzip2 >= %{BZIP2_VERSION}
Requires:               mingw64-freetype >= %{FREETYPE_VERSION}
Requires:               mingw64-expat >= %{EXPAT_VERSION}
Requires:               mingw64-fontconfig >= %{FONTCONFIG_VERSION}
Requires:               mingw64-libpng >= %{LIBPNG_VERSION}
Requires:               mingw64-libjpeg-turbo >= %{LIBJPEG_TURBO_VERSION}
Requires:               mingw64-libtiff >= %{LIBTIFF_VERSION}
Requires:               mingw64-cairo >= %{CAIRO_VERSION}
Requires:               mingw64-icu >= %{ICU_VERSION}
Requires:               mingw64-harfbuzz >= %{HARFBUZZ_VERSION}
Requires:               mingw64-pango >= %{PANGO_VERSION}
Requires:               mingw64-atk >= %{ATK_VERSION}
Requires:               mingw64-jasper >= %{JASPER_VERSION}
Requires:               mingw64-libxml2 >= %{LIBXML2_VERSION}
Requires:               mingw64-gdk-pixbuf >= %{GDK_PIXBUF_VERSION}
Requires:               mingw64-libcroco >= %{LIBCROCO_VERSION}
Requires:               mingw64-librsvg2 >= %{LIBRSVG2_VERSION}
Requires:               mingw64-gtk3 >= %{GTK3_VERSION}
Requires:               mingw64-adwaita-icon-theme >= %{GTK3_ADWAITA_VERSION}
Requires:               mingw64-gdl >= %{GDL_VERSION}

Requires:               mingw64-libgpg-error >= %{LIBGPG_ERROR_VERSION}
Requires:               mingw64-libgcrypt >= %{LIBGCRYPT_VERSION}
Requires:               mingw64-gmp >= %{GMP_VERSION}
Requires:               mingw64-nettle >= %{NETTLE_VERSION}
Requires:               mingw64-p11-kit >= %{P11_KIT_VERSION}
Requires:               mingw64-libtasn1 >= %{LIBTASN1_VERSION}
Requires:               mingw64-readline >= %{READLINE_VERSION}
Requires:               mingw64-gnutls  >= %{GNUTLS_VERSION}
Requires:               mingw64-glib-networking >= %{GLIB_NETWORKING_VERSION}

Requires:               mingw64-libxslt >= %{LIBXSLT_VERSION}
Requires:               mingw64-sqlite >= %{SQLITE_VERSION}
Requires:               mingw64-libsoup >= %{LIBSOUP_VERSION}

Requires:               mingw64-hunspell >= %{HUNSPELL_VERSION}
Requires:               mingw64-enchant >= %{ENCHANT_VERSION}

Requires:               mingw64-libogg >= %{LIBOGG_VERSION}
Requires:               mingw64-libvorbis >= %{LIBVORBIS_VERSION}
Requires:               mingw64-libwebp >= %{LIBWEBP_VERSION}
Requires:               mingw64-gstreamer1 >= %{GSTREAMER1_VERSION}
Requires:               mingw64-gstreamer1-plugins-base >= %{GSTREAMER1_PLUGINS_BASE_VERSION}
Requires:               mingw64-gstreamer1-plugins-good >= %{GSTREAMER1_PLUGINS_GOOD_VERSION}
Requires:               mingw64-gstreamer1-plugins-bad-free >= %{GSTREAMER1_PLUGINS_BAD_VERSION}
Requires:               mingw64-webkitgtk3 >= %{WEBKITGTK3_VERSION}

Requires:               mingw64-dbus >= %{DBUS_VERSION}
Requires:               mingw64-dbus-glib >= %{DBUS_GLIB_VERSION}

Requires:               mingw64-mono >= %{MONO_VERSION}
Requires:               mingw64-mono-data-npgsql >= %{NPGSQL_VERSION}
Requires:               mingw64-gtk-sharp3 >= %{GTK3_SHARP_VERSION}
Requires:               mingw64-gdl-sharp >= %{GDL_SHARP_VERSION}
Requires:               mingw64-mono-zeroconf >= %{MONO_ZEROCONF_VERSION}
Requires:               mingw64-mono-addins >= %{MONO_ADDINS_VERSION}
Requires:               mingw64-webkitgtk3-sharp >= %{WEBKITGTK3_SHARP_VERSION}
Requires:               mingw64-dbus-sharp >= %{DBUS_SHARP_VERSION}
Requires:               mingw64-dbus-sharp-glib >= %{DBUS_GLIB_SHARP_VERSION}
#Requires:              mingw64-gstreamer1-sharp >= %{GSTREAMER1_SHARP_VERSION}
Requires:               mingw64-newtonsoft-json >= %{NEWTONSOFT_JSON_VERSION}
#Requires:              mingw64-SharpSSH >= %{SHARP_SSH_VERSION}

%description sdk-mingw64
Easy management of applications for Windows 64 bit


%package sdk-mingw
Summary:                SDK for AppBox Mingw 32/64 bit
License:                GPL
Group:                  Applications/Desktop
BuildArch:              noarch

Requires:		appbox-sdk-mingw32
Requires:		appbox-sdk-mingw64

%description sdk-mingw
Easy management of applications for Windows



%package sdk-mingw-devel
Summary:                SDK for AppBox Mingw 32/64 bit
License:                GPL
Group:                  Applications/Desktop
BuildArch:              noarch

Requires:               appbox-sdk-mingw32-devel
Requires:               appbox-sdk-mingw64-devel

%description sdk-mingw-devel
Easy management of applications for Windows


%package sdk-mingw32-devel
Summary:                SDK for AppBox Mingw 32 bit
License:                GPL
Group:                  Applications/Desktop
BuildArch:              noarch

Requires:               appbox-sdk-mingw32

Requires:		redhat-rpm-config rpm-build
Requires:		osslsigncode
Requires:		hunspell-da
Requires:               mingw32-filesystem >= %{MINGW_FILESYSTEM_VERSION}
Requires:               mingw32-binutils >= %{BINUTILS_VERSION}
Requires:               mingw32-crt >= %{HEADER_CRT_THREAD_VERSION}
Requires:               mingw32-headers >= %{HEADER_CRT_THREAD_VERSION}
Requires:               mingw32-cpp >= %{COMPILER_VERSION}
Requires:               mingw32-gcc >= %{COMPILER_VERSION}
Requires:               mingw32-gcc-c++ >= %{COMPILER_VERSION}
Requires:               mingw32-gcc-objc >= %{COMPILER_VERSION}
Requires:               mingw32-pkg-config >= %{PKG_CONFIG_VERSION}
Requires:		mingw32-nsis >= %{NSIS_VERSION}
Requires:		mingw32-libidn

%description sdk-mingw32-devel
Easy management of applications for Windows


%package sdk-mingw64-devel
Summary:                SDK for AppBox Mingw 64 bit
License:                GPL
Group:                  Applications/Desktop
BuildArch:              noarch

Requires:		appbox-sdk-mingw64

Requires:               redhat-rpm-config rpm-build
Requires:		osslsigncode
Requires:		hunspell-da
Requires:               mingw64-filesystem >= %{MINGW_FILESYSTEM_VERSION}
Requires:               mingw64-binutils >= %{BINUTILS_VERSION}
Requires:               mingw64-crt >= %{HEADER_CRT_THREAD_VERSION}
Requires:               mingw64-headers >= %{HEADER_CRT_THREAD_VERSION}
Requires:               mingw64-cpp >= %{COMPILER_VERSION}
Requires:               mingw64-gcc >= %{COMPILER_VERSION}
Requires:               mingw64-gcc-c++ >= %{COMPILER_VERSION}
Requires:               mingw64-gcc-objc >= %{COMPILER_VERSION}
Requires:               mingw64-pkg-config >= %{PKG_CONFIG_VERSION}
Requires:		mingw64-libidn

%description sdk-mingw64-devel
Easy management of applications for Windows



%package sdk-darwinx
Summary:                SDK for AppBox Mac OS X
License:                GPL
Group:                  Applications/Desktop
BuildArch:              noarch

Requires:		ige-mac-bundler >= %{GTK_MAC_BUNDLER_VERSION}
Requires:		hunspell-da
Requires:               darwinx-gettext >= %{GETTEXT_VERSION}
Requires:               darwinx-libffi >= %{LIBFFI_VERSION}
Requires:               darwinx-glib2 >= %{GLIB2_VERSION}
Requires:               darwinx-pixman >= %{PIXMAN_VERSION}
Requires:               darwinx-freetype >= %{FREETYPE_VERSION}
Requires:               darwinx-fontconfig >= %{FONTCONFIG_VERSION}
Requires:               darwinx-libpng >= %{LIBPNG_VERSION}
Requires:               darwinx-libjpeg-turbo >= %{LIBJPEG_TURBO_VERSION}
Requires:               darwinx-libtiff >= %{LIBTIFF_VERSION}
Requires:               darwinx-cairo >= %{CAIRO_VERSION}
Requires:               darwinx-icu >= %{ICU_VERSION}
Requires:               darwinx-harfbuzz >= %{HARFBUZZ_VERSION}
Requires:               darwinx-pango >= %{PANGO_VERSION}
Requires:               darwinx-atk >= %{ATK_VERSION}
Requires:               darwinx-jasper >= %{JASPER_VERSION}
Requires:               darwinx-libxml2 >= %{LIBXML2_VERSION}
Requires:               darwinx-gdk-pixbuf >= %{GDK_PIXBUF_VERSION}
Requires:               darwinx-libcroco >= %{LIBCROCO_VERSION}
Requires:               darwinx-librsvg2 >= %{LIBRSVG2_VERSION}
Requires:               darwinx-gtk3 >= %{GTK3_VERSION}
Requires:               darwinx-adwaita-icon-theme >= %{GTK3_ADWAITA_VERSION}
Requires:               darwinx-gdl >= %{GDL_VERSION}
Requires:		darwinx-gtk-mac-integration >= %{GTK_MAC_INTEGRATION_VERSION}

Requires:               darwinx-libgpg-error >= %{LIBGPG_ERROR_VERSION}
Requires:               darwinx-libgcrypt >= %{LIBGCRYPT_VERSION}
Requires:               darwinx-gmp >= %{GMP_VERSION}
Requires:               darwinx-nettle >= %{NETTLE_VERSION}
Requires:               darwinx-p11-kit >= %{P11_KIT_VERSION}
Requires:               darwinx-libtasn1 >= %{LIBTASN1_VERSION}
Requires:               darwinx-gnutls  >= %{GNUTLS_VERSION}
Requires:               darwinx-glib-networking >= %{GLIB_NETWORKING_VERSION}

Requires:               darwinx-libxslt >= %{LIBXSLT_VERSION}
Requires:               darwinx-libsoup >= %{LIBSOUP_VERSION}

Requires:               darwinx-enchant >= %{ENCHANT_VERSION}

Requires:               darwinx-libogg >= %{LIBOGG_VERSION}
Requires:               darwinx-libvorbis >= %{LIBVORBIS_VERSION}
Requires:               darwinx-libwebp >= %{LIBWEBP_VERSION}
Requires:               darwinx-gstreamer1 >= %{GSTREAMER1_VERSION}
Requires:               darwinx-gstreamer1-plugins-base >= %{GSTREAMER1_PLUGINS_BASE_VERSION}
Requires:               darwinx-gstreamer1-plugins-good >= %{GSTREAMER1_PLUGINS_GOOD_VERSION}
Requires:               darwinx-gstreamer1-plugins-bad >= %{GSTREAMER1_PLUGINS_BAD_VERSION}
Requires:               darwinx-webkitgtk3 >= %{WEBKITGTK3_VERSION}

Requires:               darwinx-dbus >= %{DBUS_VERSION}
Requires:               darwinx-dbus-glib >= %{DBUS_GLIB_VERSION}

Requires:               darwinx-mono >= %{MONO_VERSION}
Requires:               darwinx-mono-data-npgsql >= %{NPGSQL_VERSION}
Requires:               darwinx-gtk-sharp3 >= %{GTK3_SHARP_VERSION}
Requires:               darwinx-gdl-sharp >= %{GDL_SHARP_VERSION}
Requires:		darwinx-gtk-mac-integration-sharp >= %{GTK_MAC_INTEGRATION_SHARP_VERSION}
Requires:               darwinx-mono-zeroconf >= %{MONO_ZEROCONF_VERSION}
Requires:               darwinx-mono-addins >= %{MONO_ADDINS_VERSION}
Requires:               darwinx-webkitgtk3-sharp >= %{WEBKITGTK3_SHARP_VERSION}
Requires:               darwinx-dbus-sharp >= %{DBUS_SHARP_VERSION}
Requires:               darwinx-dbus-sharp-glib >= %{DBUS_GLIB_SHARP_VERSION}
Requires:               darwinx-gstreamer1-sharp >= %{GSTREAMER1_SHARP_VERSION}
Requires:		darwinx-newtonsoft-json >= %{GSTREAMER1_SHARP_VERSION}
#Requires:               darwinx-SharpSSH >= %{SHARP_SSH_VERSION}

%description sdk-darwinx
Easy management of applications for Mac OS X




%prep

%setup -q -n appbox-0.1

#sed -i -e 's!gmcs!mcs!' configure.in
#./autogen.sh --prefix=%{_prefix} --sysconfdir=/etc

%build
#make all

%install
#if [ -d $RPM_BUILD_ROOT ]; then rm -rf $RPM_BUILD_ROOT; fi
#DESTDIR=$RPM_BUILD_ROOT make install

mkdir -p $RPM_BUILD_ROOT%{_datadir}/yum-plugins
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/yum/pluginconf.d

cp %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/yum/pluginconf.d/
cp %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/yum-plugins

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d
cp %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg
cp %{SOURCE4} $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg/

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/rpm
cp %{SOURCE5} $RPM_BUILD_ROOT%{_sysconfdir}/rpm/

mkdir -p $RPM_BUILD_ROOT%{_bindir}
cp %{SOURCE6} $RPM_BUILD_ROOT%{_bindir}/
cp %{SOURCE7} $RPM_BUILD_ROOT%{_bindir}/
cp %{SOURCE8} $RPM_BUILD_ROOT%{_bindir}/
cp %{SOURCE9} $RPM_BUILD_ROOT%{_bindir}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README TODO LICENSE
#%attr(0775,root,root) %{_prefix}/bin/appbox
#%{_libdir}/mono/appbox/AppBox.Config.dll
#%{_libdir}/mono/appbox/AppBox.Utils.dll
#%{_libdir}/mono/appbox/appbox.exe
#%{_libdir}/mono/gac
#%{_datadir}/appbox/ui/appbox.xml
#%{_datadir}/applications/appbox.desktop
#%{_datadir}/locale


%files release
%defattr(-, root, root)
%{_sysconfdir}/yum.repos.d/appbox.repo
%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-appbox
%{_sysconfdir}/yum/pluginconf.d/yum_ignoreos.conf
%{_datadir}/yum-plugins/yum_ignoreos.py
%{_datadir}/yum-plugins/yum_ignoreos.pyc
%{_datadir}/yum-plugins/yum_ignoreos.pyo


%files runtime
%defattr(-, root, root)


%files sdk
%defattr(-, root, root)


%files sdk-mingw32
%defattr(-, root, root)


%files sdk-mingw64
%defattr(-, root, root)


%files sdk-mingw
%defattr(-, root, root)


%files sdk-mingw32-devel
%defattr(-, root, root)


%files sdk-mingw64-devel
%defattr(-, root, root)


%files sdk-mingw-devel
%defattr(-, root, root)


%files sdk-darwinx
%defattr(-, root, root)
%{_sysconfdir}/rpm/macros.darwinx
%{_bindir}/darwinx-cmake
%{_bindir}/darwinx-configure
%{_bindir}/darwinx-make
%{_bindir}/darwinx-pkg-config



###########################################################################
%changelog
* Thu Jun 08 2010 Mikkel Kruse Johnsen, Appbox <mikkel@appbox.info>
- First rpm build.
