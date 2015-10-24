%define		majorminor	1.0

Name:		darwinx-gstreamer1-plugins-bad
Version: 	1.4.5
Release: 	1%{?dist}
Summary: 	GStreamer streaming media framework base plug-ins
Group: 		Applications/Multimedia
License: 	LGPLv2+
URL:		http://gstreamer.freedesktop.org/
Source: 	http://gstreamer.freedesktop.org/src/gst-plugins-bad/gst-plugins-bad-%{version}.tar.xz
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch: 	noarch

Requires:	darwinx-filesystem >= 16
Requires:	darwinx-gstreamer1 >= %{version}
Requires:	darwinx-gstreamer1-plugins-base >= %{version}

BuildRequires:	darwinx-filesystem >= 16
BuildRequires:	darwinx-gcc
BuildRequires:	darwinx-glib2
BuildRequires:	darwinx-gstreamer1 >= %{version}
BuildRequires:	darwinx-gstreamer1-plugins-base >= %{version}
BuildRequires:  darwinx-libwebp
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	m4
BuildRequires:	pkgconfig
BuildRequires:	libtool

Obsoletes:	darwinx-gstreamer-plugins-bad

%description
GStreamer is a streaming media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new
plug-ins.

This package contains a set of well-maintained base plug-ins.

%prep
%setup -q -n gst-plugins-bad-%{version}

#%patch1 -p1 -b .rpm-provides

%build
%{_darwinx_configure} \
  --with-package-name='Fedora gstreamer package' \
  --with-package-origin='http://download.fedora.redhat.com/fedora' \
  --disable-x \
  --disable-xvideo \
  --disable-gtk-doc \
  --enable-debug \
  --disable-tests \
  --disable-examples \
  --disable-shout2 \
  --disable-shout2test \
  --disable-jpeg \
  --disable-goom

%{_darwinx_make} OBJC=darwinx-gcc %{?_smp_mflags}

%install  
rm -rf $RPM_BUILD_ROOT

# Install doc temporarily later will be removed
%{_darwinx_makeinstall}

# Remove manpages.
rm -rf $RPM_BUILD_ROOT%{_darwinx_mandir}

# Remove gtk documentation.
rm -rf $RPM_BUILD_ROOT%{_darwinx_datadir}/gtk-doc

# Remove GConf schemas
rm -rf $RPM_BUILD_ROOT%{_darwinx_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root, -)
%{_darwinx_libdir}
%{_darwinx_datadir}
%{_darwinx_includedir}

%changelog
* Thu Apr 06 2010 Mikkel Kruse Johnsen <mikkel@linet.dk>
- first draft of spec file
