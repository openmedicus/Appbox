%global debug_package %{nil}

%define ver 4.6.1

Name:           darwinx-mono
Version:        %{ver}.3
Release:        1%{?dist}
Summary:        A .NET runtime environment

Group:          Development/Languages
License:        MIT
URL:            http://www.mono-project.com/Main_Page
Source0:        http://download.mono-project.com/sources/mono/mono-%{version}.tar.bz2
Source1:        monodir.c
# This key was generated by Tom "spot" Callaway <tcallawa@redhat.com> on Dec 1, 2009
# by running the following command:
# sn -k mono.snk
# You should not regenerate this unless you have a really, really, really good reason.
Source2:        mono.snk
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch

BuildRequires:  darwinx-filesystem-base >= 18

Requires:  	darwinx-filesystem >= 18

%description
The Mono runtime implements a JIT engine for the ECMA CLI
virtual machine (as well as a byte code interpreter, the
class loader, the garbage collector, threading system and
metadata access libraries.

%define monodir /usr/darwinx/usr/lib/mono
%define gac_dll(dll)  %{monodir}/gac/%{1} \
  %{monodir}/?.?/%{1}.dll \
  %{nil}
%define mono_bin(bin) %{_darwinx_bindir}/%{1} \
  %{monodir}/?.?/%{1}.exe \
  %{monodir}/?.?/%{1}.exe.* \
  %{nil}

%prep
%setup -q -n mono-%{ver}

sed -i '' 's!$mono_libdir/!!g' data/config.in

# Remove prebuilt binaries
rm -rf mcs/class/lib/monolite/*

%build
gcc -o monodir %{SOURCE1} -DMONODIR=\"%{_darwinx_prefix}/lib/mono\"

%{_darwinx_configure} --enable-parallel-mark --disable-nls

%{_darwinx_make} %{?_smp_mflags} 

%install
%{__rm} -rf %{buildroot}
make DESTDIR=%{buildroot} install program_transform_name="" 
install monodir %{buildroot}%{_darwinx_bindir}

# copy the mono.snk key into /etc/pki/mono
mkdir -p %{buildroot}%{_darwinx_sysconfdir}/pki/mono
install -p -m0644 %{SOURCE2} %{buildroot}%{_darwinx_sysconfdir}/pki/mono/

%{__rm} %{buildroot}%{_darwinx_libdir}/*.la
%{__rm} %{buildroot}%{_darwinx_libdir}/*.a

# We put these inside rpm
%{__rm} %{buildroot}%{_darwinx_bindir}/mono-find-provides
%{__rm} %{buildroot}%{_darwinx_bindir}/mono-find-requires

# No more 2.0 and 3.5
%{__rm} -rf %{buildroot}%{monodir}/2.0
%{__rm} -rf %{buildroot}%{monodir}/2.0-api
%{__rm} -rf %{buildroot}%{monodir}/3.5
%{__rm} -rf %{buildroot}%{monodir}/3.5-api

# This was removed upstream:
%{__rm} -rf %{buildroot}%{monodir}/gac/Mono.Security.Win32
%{__rm} -rf %{buildroot}%{monodir}/4.0/Mono.Security.Win32.dll
%{__rm} -rf %{buildroot}%{monodir}/4.5/Mono.Security.Win32.dll
%{__rm} %{buildroot}%{_darwinx_datadir}/libgc-mono/README*
%{__rm} %{buildroot}%{_darwinx_datadir}/libgc-mono/barrett_diagram
%{__rm} %{buildroot}%{_darwinx_datadir}/libgc-mono/*.html
%{__rm} %{buildroot}%{_darwinx_datadir}/libgc-mono/gc.man
%{__rm} -f %{buildroot}%{monodir}/4.5/mcs.exe.so
%{__rm} -rf %{buildroot}%{monodir}/xbuild/Microsoft
%{__rm} -f %{buildroot}%{monodir}/4.0/mscorlib.dll.dylib
%{__rm} -f %{buildroot}%{monodir}/4.0/dmcs.exe.so
%{__rm} -rf %{buildroot}%{monodir}/4.0/Mono.Security.Win32
%{__rm} -f %{buildroot}%{monodir}/4.5/mscorlib.dll.dylib
%{__rm} -rf %{buildroot}%{_darwinx_bindir}/mono-configuration-crypto
%{__rm} -rf %{buildroot}%{_darwinx_mandir}/man?/mono-configuration-crypto*

# Remove Npgsql
%{__rm} -rf %{buildroot}%{monodir}/4.0/Npgsql.dll

%clean
#%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_darwinx_bindir}/mono
%{_darwinx_bindir}/mono-sgen
%{_darwinx_bindir}/mono-boehm
%{_darwinx_bindir}/monodir
%{_darwinx_bindir}/mono-test-install
%{_darwinx_bindir}/mono-gdb.py
%{_darwinx_bindir}/mono-symbolicate
%mono_bin mcs
%mono_bin cccheck
%mono_bin ccrewrite
%mono_bin gacutil
%mono_bin chktrust
%mono_bin csharp
%mono_bin lc
%mono_bin mozroots
%mono_bin pdb2mdb
%mono_bin setreg
%mono_bin sn
%{_darwinx_bindir}/gacutil2
%{_darwinx_bindir}/dmcs
%{_darwinx_bindir}/mono-heapviz
%{_darwinx_bindir}/mprof-report
%{_darwinx_mandir}/man1/certmgr.1
%{_darwinx_mandir}/man1/chktrust.1
%{_darwinx_mandir}/man1/gacutil.1
%{_darwinx_mandir}/man1/mcs.1
%{_darwinx_mandir}/man1/mono.1
%{_darwinx_mandir}/man1/mozroots.1
%{_darwinx_mandir}/man1/setreg.1
%{_darwinx_mandir}/man1/sn.1
%{_darwinx_mandir}/man5/mono-config.5
%{_darwinx_mandir}/man1/csharp.1
%{_darwinx_mandir}/man1/pdb2mdb.1
%{_darwinx_mandir}/man1/lc.1
%{_darwinx_mandir}/man1/mprof-report.1
%{_darwinx_mandir}/man1/cccheck.1
%{_darwinx_libdir}/libMonoPosixHelper.dylib
%dir %{monodir}
%dir %{monodir}/4.0
%dir %{monodir}/4.5
%dir %{monodir}/gac
%gac_dll Commons.Xml.Relaxng
%gac_dll ICSharpCode.SharpZipLib
%gac_dll Mono.Debugger.Soft

%gac_dll cscompmgd
%gac_dll Microsoft.VisualC
%gac_dll Mono.Cairo
%gac_dll Mono.CompilerServices.SymbolWriter
%gac_dll Mono.CSharp
%gac_dll Mono.Parallel
%gac_dll System.Drawing
%gac_dll Mono.Management
%gac_dll Mono.Posix
%gac_dll Mono.Security
%gac_dll Mono.Security.Providers.DotNet
%gac_dll Mono.Security.Providers.NewSystemSource
%gac_dll Mono.Security.Providers.NewTls
%gac_dll Mono.Security.Providers.OldTls
%gac_dll Mono.Simd
%gac_dll System
%gac_dll System.Configuration
%gac_dll System.Core
%gac_dll System.Security
%gac_dll System.Xml
%gac_dll System.Xml.Serialization
%gac_dll Mono.Tasklets
%gac_dll System.Net
%gac_dll System.Net.Http
%gac_dll System.Net.Http.Formatting
%gac_dll System.Net.Http.WebRequest
%gac_dll System.Xml.Linq
%gac_dll System.Json
%gac_dll System.Json.Microsoft
%gac_dll System.Threading.Tasks.Dataflow
%dir %{_darwinx_sysconfdir}/mono
%dir %{_darwinx_sysconfdir}/mono/2.0
%dir %{_darwinx_sysconfdir}/mono/mconfig
%config (noreplace) %{_darwinx_sysconfdir}/mono/config
%config (noreplace) %{_darwinx_sysconfdir}/mono/2.0/machine.config
%config (noreplace) %{_darwinx_sysconfdir}/mono/2.0/settings.map
%config (noreplace) %{_darwinx_sysconfdir}/mono/4.0/Browsers/Compat.browser
%config (noreplace) %{_darwinx_sysconfdir}/mono/4.5/machine.config
%config (noreplace) %{_darwinx_sysconfdir}/mono/4.5/settings.map
%config (noreplace) %{_darwinx_sysconfdir}/mono/4.5/Browsers/Compat.browser
%{_darwinx_prefix}/lib/mono-source-libs/
%{_darwinx_libdir}/libmono*-2.0*.dylib
%{_darwinx_libdir}/libmono-profiler-*.dylib
%config (noreplace) %{_darwinx_sysconfdir}/mono/4.0/*.config
%config (noreplace) %{_darwinx_sysconfdir}/mono/4.0/settings.map
%config (noreplace) %{_darwinx_sysconfdir}/mono/4.0/DefaultWsdlHelpGenerator.aspx
%dir %{_darwinx_sysconfdir}/mono/4.0
%{monodir}/4.0/mscorlib.dll
%{monodir}/4.5/mscorlib.dll
%{monodir}/4.5/mscorlib.dll.mdb
%{monodir}/4.0-api/
%{monodir}/4.5-api/
%gac_dll Microsoft.CSharp
%gac_dll System.Dynamic
%gac_dll System.Runtime.InteropServices.RuntimeInformation
%gac_dll System.Reflection.Context
%gac_dll System.ComponentModel.Composition
%gac_dll System.EnterpriseServices
%gac_dll System.Data
%gac_dll System.Numerics
%gac_dll System.Numerics.Vectors
%gac_dll System.Runtime.Caching
%gac_dll System.Runtime.DurableInstancing
%gac_dll System.Transactions
%gac_dll System.Xaml
%gac_dll WebMatrix.Data
%gac_dll Mono.CodeContracts
%{_darwinx_mandir}/man1/ccrewrite.1
%gac_dll CustomMarshalers
%gac_dll I18N.West
%gac_dll I18N
%gac_dll System.Reactive.Core
%gac_dll System.Reactive.Debugger
%gac_dll System.Reactive.Experimental
%gac_dll System.Reactive.Interfaces
%gac_dll System.Reactive.Linq
%gac_dll System.Reactive.PlatformServices
%gac_dll System.Reactive.Providers
%gac_dll System.Reactive.Runtime.Remoting
%gac_dll System.Reactive.Windows.Threading
%gac_dll System.Reactive.Observable.Aliases
%gac_dll System.IO.Compression.FileSystem
%gac_dll System.IO.Compression
%gac_dll System.Windows
%{_darwinx_prefix}/lib/mono/4.5/Facades
%{_darwinx_prefix}/lib/mono/gac/Mono.Cecil/*/Mono.Cecil.dll*

### files devel
%{_darwinx_sysconfdir}/pki/mono/
%{_darwinx_bindir}/mono-api-info
%mono_bin xbuild
%mono_bin genxs
%{monodir}/?.?/culevel*
%mono_bin al
%mono_bin caspol
%mono_bin cert2spc
%mono_bin certmgr
%mono_bin crlupdate
%mono_bin dtd2rng
%mono_bin dtd2xsd
%mono_bin installvst
%mono_bin macpack
%mono_bin makecert
%mono_bin mono-cil-strip
%{_darwinx_bindir}/mono-sgen-gdb.py
%mono_bin mono-shlib-cop
%mono_bin mono-xmltool
%mono_bin permview
%mono_bin secutil
%mono_bin sgen
%mono_bin signcode
%{_darwinx_bindir}/al2
%mono_bin ilasm
%mono_bin mkbundle
%mono_bin cert-sync
%{_darwinx_bindir}/monodis
%mono_bin monolinker
%mono_bin monop
%mono_bin mono-api-html
%{_darwinx_bindir}/monop2
%{_darwinx_bindir}/peverify
%{_darwinx_bindir}/prj2make
%mono_bin resgen
%{_darwinx_bindir}/resgen2
%{_darwinx_bindir}/pedump
%{_darwinx_bindir}/mdbrebase
%{_darwinx_bindir}/ikdasm
%{_darwinx_prefix}/lib/mono/4.5/mono-symbolicate.exe
%{_darwinx_prefix}/lib/mono/4.5/mono-symbolicate.exe.mdb
%{_darwinx_prefix}/lib/mono/4.5/linkeranalyzer.exe
%{_darwinx_prefix}/lib/mono/4.5/linkeranalyzer.exe.mdb
%{_darwinx_mandir}/man1/resgen.1
%{_darwinx_mandir}/man1/al.1
%{_darwinx_mandir}/man1/cert2spc.1
%{_darwinx_mandir}/man1/cilc.1
%{_darwinx_mandir}/man1/dtd2xsd.1
%{_darwinx_mandir}/man1/genxs.1
%{_darwinx_mandir}/man1/ilasm.1
%{_darwinx_mandir}/man1/macpack.1
%{_darwinx_mandir}/man1/makecert.1
%{_darwinx_mandir}/man1/mkbundle.1
%{_darwinx_mandir}/man1/mono-cil-strip.1
%{_darwinx_mandir}/man1/monodis.1
%{_darwinx_mandir}/man1/monolinker.1
%{_darwinx_mandir}/man1/mono-shlib-cop.1
%{_darwinx_mandir}/man1/mono-xmltool.1
%{_darwinx_mandir}/man1/monop.1
%{_darwinx_mandir}/man1/permview.1
%{_darwinx_mandir}/man1/prj2make.1
%{_darwinx_mandir}/man1/secutil.1
%{_darwinx_mandir}/man1/sgen.1
%{_darwinx_mandir}/man1/signcode.1
%{_darwinx_mandir}/man1/xbuild.1
%{_darwinx_mandir}/man1/mono-api-info.1
#{_darwinx_mandir}/man1/mono-configuration-crypto.1
%{_darwinx_mandir}/man1/crlupdate.1
%{_darwinx_mandir}/man1/mono-symbolicate.1
%gac_dll PEAPI
%gac_dll Microsoft.Build
%gac_dll Microsoft.Build.Engine
%gac_dll Microsoft.Build.Framework
%gac_dll Microsoft.Build.Tasks.v4.0
%gac_dll Microsoft.Build.Utilities.v4.0
%gac_dll Mono.XBuild.Tasks
%gac_dll System.Deployment
%{monodir}/4.5/xbuild.rsp
%{monodir}/4.5/MSBuild/Microsoft.Build.CommonTypes.xsd
%{monodir}/4.5/MSBuild/Microsoft.Build.Core.xsd
%{monodir}/4.5/Microsoft.Build.xsd
%{monodir}/4.5/Microsoft.CSharp.targets
%{monodir}/4.5/Microsoft.Common.targets
%{monodir}/4.5/Microsoft.Common.tasks
%{monodir}/4.5/Microsoft.VisualBasic.targets
%{monodir}/mono-configuration-crypto/4.5/Mono.Configuration.Crypto.dll
%{monodir}/mono-configuration-crypto/4.5/Mono.Configuration.Crypto.dll.mdb
%{monodir}/mono-configuration-crypto/4.5/mono-configuration-crypto.exe
%{monodir}/mono-configuration-crypto/4.5/mono-configuration-crypto.exe.mdb
%{_darwinx_libdir}/libMonoSupportW.dylib
%{_darwinx_libdir}/libikvm-native.dylib
%{_darwinx_libdir}/pkgconfig/dotnet.pc
%{_darwinx_libdir}/pkgconfig/mono-cairo.pc
%{_darwinx_libdir}/pkgconfig/mono.pc
%{_darwinx_libdir}/pkgconfig/cecil.pc
%{_darwinx_libdir}/pkgconfig/dotnet35.pc
%{_darwinx_libdir}/pkgconfig/mono-lineeditor.pc
%{_darwinx_libdir}/pkgconfig/mono-options.pc
%{_darwinx_libdir}/pkgconfig/wcf.pc
%{_darwinx_libdir}/pkgconfig/mono-2.pc
%{_darwinx_libdir}/pkgconfig/monosgen-2.pc
%{_darwinx_libdir}/pkgconfig/xbuild12.pc
%{monodir}/xbuild
%{_darwinx_includedir}/mono-2.0/mono/jit/jit.h
%{_darwinx_includedir}/mono-2.0/mono/metadata/*.h
%{_darwinx_includedir}/mono-2.0/mono/utils/*.h
%{_darwinx_includedir}/mono-2.0/mono/cil/opcode.def
%{monodir}/xbuild-frameworks
%{monodir}/4.5/browsercaps-updater.exe
%{monodir}/4.5/browsercaps-updater.exe.mdb
%{monodir}/4.5/ictool.exe
%{monodir}/4.5/ictool.exe.mdb
%{monodir}/4.5/installutil.exe
%{monodir}/4.5/installutil.exe.mdb
%{monodir}/4.5/mod.exe
%{monodir}/4.5/mod.exe.mdb
%{monodir}/4.5/mono-api-info.exe*
%{_darwinx_libdir}/pkgconfig/reactive.pc
%{_darwinx_prefix}/lib/mono/4.5/mdbrebase.exe
%{_darwinx_prefix}/lib/mono/4.5/mdbrebase.exe.mdb
%{_darwinx_prefix}/lib/mono/4.5/ikdasm.exe
%{_darwinx_prefix}/lib/mono/4.5/ikdasm.exe.mdb
%{_darwinx_prefix}/lib/mono/gac/Microsoft.Build.Tasks.Core
%{_darwinx_prefix}/lib/mono/gac/Microsoft.Build.Tasks.v12.0
%{_darwinx_prefix}/lib/mono/gac/Microsoft.Build.Utilities.Core
%{_darwinx_prefix}/lib/mono/gac/Microsoft.Build.Utilities.v12.0
%{_darwinx_libdir}/mono/lldb/mono.py
%{_darwinx_prefix}/lib/mono/4.5/SMDiagnostics.dll
%{_darwinx_prefix}/lib/mono/gac/SMDiagnostics
%{_darwinx_datadir}/mono-2.0/mono/cil/cil-opcodes.xml
%{_darwinx_datadir}/mono-2.0/mono/profiler/mono-profiler-log.suppression

### files nunit
%mono_bin nunit-console
%{_darwinx_bindir}/nunit-console2
%{_darwinx_bindir}/nunit-console4
%gac_dll nunit.core
%gac_dll nunit.framework
%gac_dll nunit.util
%gac_dll nunit.mocks
%gac_dll nunit-console-runner
%gac_dll nunit.core.extensions
%gac_dll nunit.core.interfaces
%gac_dll nunit.framework.extensions

### %files nunit-devel
%{_darwinx_libdir}/pkgconfig/mono-nunit.pc

### files locale-extras
%gac_dll I18N.MidEast
%gac_dll I18N.Rare
%gac_dll I18N.CJK
%gac_dll I18N.Other

### files extras
%{_darwinx_bindir}/mono-service2
%mono_bin mono-service
%{monodir}/gac/mono-service
%gac_dll System.Configuration.Install
%gac_dll System.Management
%gac_dll System.Messaging
%gac_dll System.ServiceProcess
%gac_dll Mono.Messaging.RabbitMQ
%gac_dll Mono.Messaging
%gac_dll RabbitMQ.Client
%{monodir}/?.?/RabbitMQ.Client.Apigen*
%{_darwinx_mandir}/man1/mono-service.1

### files wcf
%gac_dll System.IdentityModel
%gac_dll System.IdentityModel.Selectors
%gac_dll System.ServiceModel
%gac_dll System.ServiceModel.Web
%gac_dll System.ServiceModel.Discovery
%gac_dll System.ServiceModel.Routing
%gac_dll System.ServiceModel.Activation
%gac_dll System.ServiceModel.Internals
%gac_dll System.Workflow.Activities
%gac_dll System.Workflow.ComponentModel
%gac_dll System.Workflow.Runtime


### files web
%mono_bin wsdl
%mono_bin soapsuds
%mono_bin svcutil
%mono_bin httpcfg
%mono_bin mconfig
%{_darwinx_bindir}/wsdl2
%mono_bin xsd
%mono_bin disco
%gac_dll Mono.Http
%gac_dll System.ComponentModel.DataAnnotations
%gac_dll System.Runtime.Remoting
%gac_dll System.Runtime.Serialization.Formatters.Soap
%gac_dll System.Web
%gac_dll System.Web.Abstractions
%gac_dll System.Web.DynamicData
%gac_dll System.Web.Routing
%gac_dll System.Web.Services
%gac_dll System.Web.ApplicationServices
%gac_dll Microsoft.Web.Infrastructure
%gac_dll System.Web.Http
%gac_dll System.Web.Http.SelfHost
%gac_dll System.Web.Razor
%gac_dll System.Web.WebPages.Deployment
%gac_dll System.Web.WebPages.Razor
%gac_dll System.Web.WebPages
%gac_dll System.Web.Http.WebHost
%gac_dll System.Web.Mobile
%gac_dll System.Web.RegularExpressions
%{_darwinx_mandir}/man1/disco.1
%{_darwinx_mandir}/man1/httpcfg.1
%{_darwinx_mandir}/man1/mconfig.1
%{_darwinx_mandir}/man1/soapsuds.1
%{_darwinx_mandir}/man1/wsdl.1
%{_darwinx_mandir}/man1/xsd.1
%config (noreplace) %{_darwinx_sysconfdir}/mono/browscap.ini
%config (noreplace) %{_darwinx_sysconfdir}/mono/2.0/Browsers/Compat.browser
%config (noreplace) %{_darwinx_sysconfdir}/mono/2.0/DefaultWsdlHelpGenerator.aspx
%config (noreplace) %{_darwinx_sysconfdir}/mono/mconfig/config.xml
%config (noreplace) %{_darwinx_sysconfdir}/mono/2.0/web.config
%config (noreplace) %{_darwinx_sysconfdir}/mono/4.5/DefaultWsdlHelpGenerator.aspx
%config (noreplace) %{_darwinx_sysconfdir}/mono/4.5/web.config

### files web-devel
%{_darwinx_libdir}/pkgconfig/aspnetwebstack.pc
%{_darwinx_libdir}/pkgconfig/system.web.mvc3.pc

### files winforms
%gac_dll Accessibility
%gac_dll Mono.WebBrowser
%gac_dll System.Design
%gac_dll System.Drawing.Design
%gac_dll System.Windows.Forms
%gac_dll System.Windows.Forms.DataVisualization
%gac_dll System.Reactive.Windows.Forms

### files mvc
%gac_dll System.Web.Extensions
%gac_dll System.Web.Extensions.Design
%gac_dll System.Web.Mvc

### files mvc-devel
%{_darwinx_libdir}/pkgconfig/system.web.extensions.design_1.0.pc
%{_darwinx_libdir}/pkgconfig/system.web.extensions_1.0.pc
%{_darwinx_libdir}/pkgconfig/system.web.mvc.pc
%{_darwinx_libdir}/pkgconfig/system.web.mvc2.pc

### files winfx
%gac_dll WindowsBase

### files data
%mono_bin sqlmetal
%mono_bin sqlsharp
%gac_dll System.Data.Entity
%gac_dll System.Data.DataSetExtensions
%gac_dll System.Data.Linq
%gac_dll System.Data.Services
%gac_dll System.Data.Services.Client
%gac_dll System.DirectoryServices
%gac_dll System.DirectoryServices.Protocols
%gac_dll System.Runtime.Serialization
%gac_dll Mono.Data.Tds
%gac_dll Novell.Directory.Ldap
%{_darwinx_mandir}/man1/sqlsharp.1

### files data-sqlite
%gac_dll Mono.Data.Sqlite

### files data-oracle
%gac_dll System.Data.OracleClient

### files -n ibm-data-db2
%gac_dll IBM.Data.DB2

### files -n monodoc
%mono_bin mdoc
%{monodir}/gac/monodoc
%{_darwinx_prefix}/lib/monodoc/*
%{monodir}/monodoc/monodoc.dll
%{_darwinx_bindir}/mod
%{_darwinx_bindir}/mdoc-*
%{_darwinx_bindir}/mdass*
%{_darwinx_bindir}/mdval*
%{_darwinx_bindir}/monodoc*
%{_darwinx_mandir}/man1/md*
%{_darwinx_mandir}/man1/monodoc*
%{_darwinx_mandir}/man5/mdoc*

### files -n monodoc-devel
%{_darwinx_libdir}/pkgconfig/monodoc.pc


%changelog
* Tue Jan 5 2016 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 4.2.2.10-1
- Update to 4.2.2.10

* Tue Mar 25 2014 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 3.2.8-1
- Initial version
