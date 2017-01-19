%define		debug_package %{nil}

Name:		webkitgtk3-sharp
Version:	2.4.11
Release:	1%{?dist}
Summary:	.NET bindings for WebKit
Group:		Development/Languages
License:	MIT
URL:		http://ftp.novell.com/pub/mono/sources/webkit-sharp/
Source0:        webkitgtk3-sharp-%{version}.tar.gz
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:	webkitgtk3-devel >= %{version}
BuildRequires:	mono-devel
BuildRequires:	gtk-sharp3-devel
BuildRequires:	gtk-sharp3-gapi >= 3.12.0
BuildRequires:	monodoc-devel

Obsoletes:	webkit-sharp
Provides:	webkit-sharp = %{version}-%{release}

Requires:	webkitgtk3 >= %{version}
Requires:	gtk-sharp3 >= 3.12.0

Provides:	webkitgtk3-sharp-devel

%description
webkitgtk-sharp is .NET bindings for the WebKit rendering engine.

%prep
%setup -q

%build
sh autogen.sh --prefix=/usr
# parallel build fails in mock
make

%install
%{__rm} -rf %{buildroot}
make DESTDIR=%{buildroot} install

%clean
#%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc COPYING README
%{_prefix}/lib/mono/
%{_datadir}/pkgconfig/webkitgtk3-sharp-3.0.pc
%{_prefix}/lib/monodoc/sources/webkitgtk3-sharp*

%changelog
* Sat May 5 2013 Mikkel Kruse Johnsen <mikkel@structura-it.dk> - 2.0.1-1
- Updated to 2.0.1 and moved to own git

* Sat Jan 5 2013 Mikkel Kruse Johnsen <mikkel@structura-it.dk> - 1.4.0-1
- Initial package
