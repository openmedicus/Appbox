Name:           darwinx-pango
Version:        1.36.8
Release:        1%{?dist}
Summary:        Darwin Pango library

License:        LGPLv2+
Group:          Development/Libraries
URL:            http://www.pango.org
Source0:        http://download.gnome.org/sources/pango/1.36/pango-%{version}.tar.xz

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

# Native pango uses a %post script to generate this, but the
# pango-querymodules.exe binary is not something we can easily run on
# a Linux host. We could use wine but wine isn't happy in a mock
# environment. So we just include a pre-generated copy on basis that
# it won't ever change much.
#
Source1:        pango.modules

BuildArch:      noarch

BuildRequires:  darwinx-filesystem >= 6
BuildRequires:  darwinx-gcc
BuildRequires:  darwinx-sdk
BuildRequires:  darwinx-odcctools

BuildRequires:  darwinx-freetype
BuildRequires:  darwinx-fontconfig
BuildRequires:  darwinx-cairo >= 1.12
BuildRequires:  darwinx-harfbuzz
BuildRequires:  darwinx-gettext
BuildRequires:  darwinx-glib2
BuildRequires:  darwinx-libpng
BuildRequires:  darwinx-pixman
BuildRequires:  pkgconfig

Requires:  	darwinx-freetype
Requires:  	darwinx-fontconfig
Requires:  	darwinx-cairo >= 1.12
Requires:  	darwinx-harfbuzz
Requires:  	darwinx-gettext
Requires:  	darwinx-glib2
Requires:  	darwinx-libpng
Requires:  	darwinx-pixman



%description
Darwin Pango library.


%package static
Summary:        Static version of the Darwin Pango library
Requires:       %{name} = %{version}-%{release}
Group:          Development/Libraries

%description static
Static version of the Darwin Pango library.


%prep
%setup -q -n pango-%{version}

%build
# Pango can't build static and shared libraries in one go, so we
# build Pango twice here
mkdir build_static
pushd build_static
%{_darwinx_configure} \
        --enable-static \
        --disable-shared \
        CFLAGS="$CFLAGS -DGLIB_STATIC_COMPILATION -DGOBJECT_STATIC_COMPILATION"

    sed -i -e 's!SUBDIRS = pango modules pango-view examples docs tools tests build!SUBDIRS = pango modules pango-view examples docs tools build!g' Makefile
    make %{?_smp_mflags}
popd

mkdir build_shared
pushd build_shared
%{_darwinx_configure} \
        --disable-static
    sed -i -e 's!SUBDIRS = pango modules pango-view examples docs tools tests build!SUBDIRS = pango modules pango-view examples docs tools build!g' Makefile
    make %{?_smp_mflags}
popd

%install
rm -rf $RPM_BUILD_ROOT

# First install all the files belonging to the shared build
make -C build_shared DESTDIR=$RPM_BUILD_ROOT install

# Install all the files from the static build in a seperate folder
# and move the static libraries to the right location
make -C build_static DESTDIR=$RPM_BUILD_ROOT/build_static install
mv $RPM_BUILD_ROOT/build_static%{_darwinx_libdir}/*.a $RPM_BUILD_ROOT%{_darwinx_libdir}
mv $RPM_BUILD_ROOT/build_static%{_darwinx_libdir}/pango/1.8.0/modules/*.a $RPM_BUILD_ROOT%{_darwinx_libdir}/pango/1.8.0/modules/

# Manually merge the libtool files
sed -i '' s/"old_library=''"/"old_library='libpango-1.0.a'"/ $RPM_BUILD_ROOT%{_darwinx_libdir}/libpango-1.0.la
sed -i '' s/"old_library=''"/"old_library='libpangocairo-1.0.a'"/ $RPM_BUILD_ROOT%{_darwinx_libdir}/libpangocairo-1.0.la
sed -i '' s/"old_library=''"/"old_library='libpangoft2-1.0.a'"/ $RPM_BUILD_ROOT%{_darwinx_libdir}/libpangoft2-1.0.la
#sed -i '' s/"old_library=''"/"old_library='libpangowin32-1.0.a'"/ $RPM_BUILD_ROOT%{_darwinx_libdir}/libpangowin32-1.0.la
#sed -i '' s/"old_library=''"/"old_library='pango-basic-atsui.a'"/ $RPM_BUILD_ROOT%{_darwinx_libdir}/pango/1.8.0/modules/pango-basic-atsui.la
sed -i '' s/"old_library=''"/"old_library='pango-basic-coretext.a'"/ $RPM_BUILD_ROOT%{_darwinx_libdir}/pango/1.8.0/modules/pango-basic-coretext.la
sed -i '' s/"old_library=''"/"old_library='pango-arabic-lang.a'"/ $RPM_BUILD_ROOT%{_darwinx_libdir}/pango/1.8.0/modules/pango-arabic-lang.la
sed -i '' s/"old_library=''"/"old_library='pango-indic-lang.a'"/ $RPM_BUILD_ROOT%{_darwinx_libdir}/pango/1.8.0/modules/pango-indic-lang.la
#sed -i '' s/"old_library=''"/"old_library='pango-arabic-fc.a'"/ $RPM_BUILD_ROOT%{_darwinx_libdir}/pango/1.8.0/modules/pango-arabic-fc.la
sed -i '' s/"old_library=''"/"old_library='pango-basic-fc.a'"/ $RPM_BUILD_ROOT%{_darwinx_libdir}/pango/1.8.0/modules/pango-basic-fc.la
#sed -i '' s/"old_library=''"/"old_library='pango-hangul-fc.a'"/ $RPM_BUILD_ROOT%{_darwinx_libdir}/pango/1.8.0/modules/pango-hangul-fc.la
#sed -i '' s/"old_library=''"/"old_library='pango-hebrew-fc.a'"/ $RPM_BUILD_ROOT%{_darwinx_libdir}/pango/1.8.0/modules/pango-hebrew-fc.la
#sed -i '' s/"old_library=''"/"old_library='pango-indic-fc.a'"/ $RPM_BUILD_ROOT%{_darwinx_libdir}/pango/1.8.0/modules/pango-indic-fc.la
#sed -i '' s/"old_library=''"/"old_library='pango-khmer-fc.a'"/ $RPM_BUILD_ROOT%{_darwinx_libdir}/pango/1.8.0/modules/pango-khmer-fc.la
#sed -i '' s/"old_library=''"/"old_library='pango-syriac-fc.a'"/ $RPM_BUILD_ROOT%{_darwinx_libdir}/pango/1.8.0/modules/pango-syriac-fc.la
#sed -i '' s/"old_library=''"/"old_library='pango-thai-fc.a'"/ $RPM_BUILD_ROOT%{_darwinx_libdir}/pango/1.8.0/modules/pango-thai-fc.la
#sed -i '' s/"old_library=''"/"old_library='pango-tibetan-fc.a'"/ $RPM_BUILD_ROOT%{_darwinx_libdir}/pango/1.8.0/modules/pango-tibetan-fc.la

# Drop the folder which was temporary used for installing the static bits
rm -rf $RPM_BUILD_ROOT/build_static

mkdir -p $RPM_BUILD_ROOT%{_darwinx_sysconfdir}/pango/
cp %{SOURCE1} $RPM_BUILD_ROOT%{_darwinx_sysconfdir}/pango/

# Drop unnecessary and duplicate files
rm -f $RPM_BUILD_ROOT%{_darwinx_libdir}/charset.alias
rm -rf $RPM_BUILD_ROOT%{_darwinx_mandir}
rm -rf $RPM_BUILD_ROOT%{_darwinx_datadir}/gtk-doc


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc COPYING
%{_darwinx_bindir}/pango-querymodules
%{_darwinx_bindir}/pango-view
%{_darwinx_sysconfdir}/pango/
%{_darwinx_includedir}/pango-1.0/
%{_darwinx_libdir}/libpango-1.0.0.dylib
%{_darwinx_libdir}/libpango-1.0.dylib
%{_darwinx_libdir}/libpango-1.0.la
%{_darwinx_libdir}/libpangocairo-1.0.0.dylib
%{_darwinx_libdir}/libpangocairo-1.0.dylib
%{_darwinx_libdir}/libpangocairo-1.0.la
%{_darwinx_libdir}/libpangoft2-1.0.0.dylib
%{_darwinx_libdir}/libpangoft2-1.0.dylib
%{_darwinx_libdir}/libpangoft2-1.0.la
%dir %{_darwinx_libdir}/pango
%dir %{_darwinx_libdir}/pango/1.8.0
%dir %{_darwinx_libdir}/pango/1.8.0/modules
%{_darwinx_libdir}/pango/1.8.0/modules/pango-arabic-lang.la
%{_darwinx_libdir}/pango/1.8.0/modules/pango-arabic-lang.so
%{_darwinx_libdir}/pango/1.8.0/modules/pango-indic-lang.la
%{_darwinx_libdir}/pango/1.8.0/modules/pango-indic-lang.so
%{_darwinx_libdir}/pango/1.8.0/modules/pango-basic-coretext.la
%{_darwinx_libdir}/pango/1.8.0/modules/pango-basic-coretext.so
%{_darwinx_libdir}/pango/1.8.0/modules/pango-basic-fc.la
%{_darwinx_libdir}/pango/1.8.0/modules/pango-basic-fc.so
%{_darwinx_libdir}/pkgconfig/pango.pc
%{_darwinx_libdir}/pkgconfig/pangocairo.pc
%{_darwinx_libdir}/pkgconfig/pangoft2.pc

%files static
%defattr(-,root,root,-)
%{_darwinx_libdir}/libpango-1.0.a
%{_darwinx_libdir}/libpangocairo-1.0.a
%{_darwinx_libdir}/libpangoft2-1.0.a
%{_darwinx_libdir}/pango/1.8.0/modules/pango-basic-coretext.a
%{_darwinx_libdir}/pango/1.8.0/modules/pango-arabic-lang.a
%{_darwinx_libdir}/pango/1.8.0/modules/pango-indic-lang.a
%{_darwinx_libdir}/pango/1.8.0/modules/pango-basic-fc.a
 

%changelog
* Sat May  8 2010 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.26.0-5
- Rebuild for PPC fix in GLib

* Sat Mar 20 2010 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.26.0-4
- Rebuild for GLib changes
- Don't build with x86_64 support because some API isn't available on OSX x86_64

* Sat Feb  6 2010 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.26.0-3
- Rebuild for x86_64 support
- Rebuild for stabs debug symbols

* Fri Sep 25 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.26.0-2
- Revert GIT commit 01783de926a as it introduced unwanted side-effects

* Fri Sep 25 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.26.0-1
- Update to 1.26.0

* Sun Sep  6 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.25.5-1
- Update to 1.25.5

* Fri Jul 10 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.24.2-2
- Rebuild for universal binary support

* Sun Jun 14 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.24.2-1
- Update to 1.24.2

* Sat Jun 13 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.23.0-4
- Use macros instead of static paths

* Sun Jun  7 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.23.0-3
- Ported the mingw package to darwin

* Thu Apr  2 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.23.0-2
- This package cannot be compiled both static and shared in one go, so
  perform the build twice

* Mon Mar  9 2009 Richard W.M. Jones <rjones@redhat.com> - 1.23.0-1
- Remove man page which duplicates what is in base Fedora.
- Rebase to 1.23.0 to match Fedora.
- +BR mingw32-dlfcn.

* Fri Feb 20 2009 Erik van Pienbroek <info@nntpgrab.nl> - 1.22.1-6
- Added -static subpackage

* Fri Feb 20 2009 Richard W.M. Jones <rjones@redhat.com> - 1.22.1-5
- Rebuild for mingw32-gcc 4.4

* Fri Jan 30 2009 Richard W.M. Jones <rjones@redhat.com> - 1.22.1-4
- Requires pkgconfig.

* Tue Jan 27 2009 Levente Farkas <lfarkas@lfarkas.org> - 1.22.1-3
- Include license file in documentation section.

* Fri Jan 23 2009 Richard W.M. Jones <rjones@redhat.com> - 1.22.1-2
- Disable static libraries.
- Use _smp_mflags.

* Fri Oct 24 2008 Richard W.M. Jones <rjones@redhat.com> - 1.22.1-1
- New upstream version 1.22.1.
- BR cairo >= 1.8.0 because of important fixes.

* Wed Sep 24 2008 Richard W.M. Jones <rjones@redhat.com> - 1.21.6-6
- Rename mingw -> mingw32.

* Tue Sep 23 2008 Daniel P. Berrange <berrange@redhat.com> - 1.21.6-5
- Remove use of wine in %-post.

* Thu Sep 11 2008 Daniel P. Berrange <berrange@redhat.com> - 1.21.6-4
- Add dep on pkgconfig

* Thu Sep 11 2008 Richard W.M. Jones <rjones@redhat.com> - 1.21.6-3
- post/preun scripts to update the pango.modules list.

* Wed Sep 10 2008 Richard W.M. Jones <rjones@redhat.com> - 1.21.6-2
- Run the correct glib-mkenums.

* Tue Sep  9 2008 Daniel P. Berrange <berrange@redhat.com> - 1.21.6-1
- Initial RPM release