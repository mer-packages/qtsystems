Name:       qt5-qtsystems
Summary:    Qt System modules
Version:    0.0git682.701442a
Release:    1%{?dist}
Group:      System/Libraries
License:    LGPLv2.1 with exception or GPLv3
URL:        http://qt.nokia.com
Source0:    %{name}-%{version}.tar.bz2
BuildRequires:  qt5-qtcore-devel
BuildRequires:  qt5-qtgui-devel
BuildRequires:  qt5-qtnetwork-devel
BuildRequires:  qt5-qtsql-devel
BuildRequires:  qt5-qtdbus-devel
BuildRequires:  qt5-qtxml-devel
BuildRequires:  qt5-qttest-devel
BuildRequires:  qt5-qtopengl-devel
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:  qt5-qtdeclarative-qtquick-devel
BuildRequires:  qt5-qmake
BuildRequires:  fdupes
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(bluez)

%description
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.
.
This package contains the Qt system modules


%package -n qt5-qtsysteminfo
Summary:    Qt system info
Group:      System/Libraries
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig

%description -n qt5-qtsysteminfo
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.
.
This package contains the Qt SystemInfo module


%package -n qt5-qtsysteminfo-devel
Summary:    Qt system info - development files
Group:      Development/Libraries
Requires:   qt5-qtsysteminfo = %{version}-%{release}

%description -n qt5-qtsysteminfo-devel
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.
.
This package contains the Qt SystemInfo development files


%package -n qt5-qtdeclarative-systeminfo
Summary:    Qt system info import for QtDeclarative
Group:      System/Libraries
Requires:   qt5-qtdeclarative

%description -n qt5-qtdeclarative-systeminfo
This package contains the system info import for QtDeclarative


%package -n qt5-qtserviceframework
Summary:    Qt Service Framework
Group:      System/Libraries
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig

%description -n qt5-qtserviceframework
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.
.
This package contains the Qt Service Framework module

%package -n qt5-qtserviceframework-devel
Summary:    Qt Service Framework - development files
Group:      Development/Libraries
Requires:   qt5-qtserviceframework = %{version}-%{release}

%description -n qt5-qtserviceframework-devel
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.
.
This package contains the Qt Service Framework development files


%package -n qt5-qtdeclarative-serviceframework
Summary:    Qt Service Framework import for QtDeclarative
Group:      System/Libraries
Requires:   qt5-qtdeclarative

%description -n qt5-qtdeclarative-serviceframework
This package contains the Service Framework import for QtDeclarative



%package -n qt5-qtpublishsubscribe
Summary:    Qt PublishSubscribe module
Group:      System/Libraries
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig

%description -n qt5-qtpublishsubscribe
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.
.
This package contains the Qt PublishSubscribe module

%package -n qt5-qtpublishsubscribe-devel
Summary:    Qt PublishSubscribe - development files
Group:      Development/Libraries
Requires:   qt5-qtpublishsubscribe = %{version}-%{release}

%description -n qt5-qtpublishsubscribe-devel
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.
.
This package contains the Qt PublishSubscribe development files


%package -n qt5-qtdeclarative-publishsubscribe
Summary:    Qt PublishSubscribe import for QtDeclarative
Group:      System/Libraries
Requires:   qt5-qtdeclarative

%description -n qt5-qtdeclarative-publishsubscribe
This package contains the PublishSuvbscribe import for QtDeclarative




#### Build section

%prep
%setup -q -n %{name}-%{version}/qtsystems

%build
export QTDIR=/usr/share/qt5
touch .git
qmake -qt=5 CONFIG+=ofono CONFIG+=nox11option CONFIG+=upower
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%qmake5_install
# Remove unneeded .la files
rm -f %{buildroot}/%{_libdir}/*.la

# We don't need qt5/Qt/
rm -rf %{buildroot}/%{_includedir}/qt5/Qt

# Fix wrong path in pkgconfig files
find %{buildroot}%{_libdir}/pkgconfig -type f -name '*.pc' \
-exec perl -pi -e "s, -L%{_builddir}/?\S+,,g" {} \;
# Fix wrong path in prl files
find %{buildroot}%{_libdir} -type f -name '*.prl' \
-exec sed -i -e "/^QMAKE_PRL_BUILD_DIR/d;s/\(QMAKE_PRL_LIBS =\).*/\1/" {} \;


%fdupes %{buildroot}/%{_includedir}




#### Pre/Post section

%post -n qt5-qtsysteminfo
/sbin/ldconfig
%postun -n qt5-qtsysteminfo
/sbin/ldconfig

%post -n qt5-qtserviceframework
/sbin/ldconfig
%postun -n qt5-qtserviceframework
/sbin/ldconfig

%post -n qt5-qtpublishsubscribe
/sbin/ldconfig
%postun -n qt5-qtpublishsubscribe
/sbin/ldconfig



#### File section


%files -n qt5-qtsysteminfo
%defattr(-,root,root,-)
%{_libdir}/libQt5SystemInfo.so.5
%{_libdir}/libQt5SystemInfo.so.5.*
%{_qt5_bindir}/*

%files -n qt5-qtsysteminfo-devel
%defattr(-,root,root,-)
%{_libdir}/libQt5SystemInfo.so
%{_libdir}/libQt5SystemInfo.prl
%{_libdir}/pkgconfig/Qt5SystemInfo.pc
%{_includedir}/qt5/QtSystemInfo/
%{_datadir}/qt5/mkspecs/modules/qt_lib_systeminfo.pri
%{_libdir}/cmake/Qt5SystemInfo/

%files -n qt5-qtdeclarative-systeminfo
%defattr(-,root,root,-)
%{_libdir}/qt5/qml/QtSystemInfo/

%files -n qt5-qtserviceframework
%defattr(-,root,root,-)
%{_qt5_bindir}/servicefw
%{_libdir}/libQt5ServiceFramework.so.5
%{_libdir}/libQt5ServiceFramework.so.5.*

%files -n qt5-qtserviceframework-devel
%defattr(-,root,root,-)
%{_libdir}/libQt5ServiceFramework.so
%{_libdir}/libQt5ServiceFramework.prl
%{_libdir}/pkgconfig/Qt5ServiceFramework.pc
%{_includedir}/qt5/QtServiceFramework/
%{_datadir}/qt5/mkspecs/modules/qt_lib_serviceframework.pri
%{_libdir}/cmake/Qt5ServiceFramework/

%files -n qt5-qtdeclarative-serviceframework
%defattr(-,root,root,-)
%{_libdir}/qt5/qml/QtServiceFramework/




%files -n qt5-qtpublishsubscribe
%defattr(-,root,root,-)
%{_libdir}/libQt5PublishSubscribe.so.5
%{_libdir}/libQt5PublishSubscribe.so.5.*

%files -n qt5-qtpublishsubscribe-devel
%defattr(-,root,root,-)
%{_libdir}/libQt5PublishSubscribe.so
%{_libdir}/libQt5PublishSubscribe.prl
%{_libdir}/pkgconfig/Qt5PublishSubscribe.pc
%{_includedir}/qt5/QtPublishSubscribe/
%{_datadir}/qt5/mkspecs/modules/qt_lib_publishsubscribe.pri
%{_libdir}/cmake/Qt5PublishSubscribe/

%files -n qt5-qtdeclarative-publishsubscribe
%defattr(-,root,root,-)
%{_libdir}/qt5/qml/QtPublishSubscribe/


#### No changelog section, separate $pkg.changes contains the history
