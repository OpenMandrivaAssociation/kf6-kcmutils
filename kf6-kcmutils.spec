%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)

%define libname %mklibname KF6KCMUtils
%define devname %mklibname KF6KCMUtils -d
#define git 20231103

Name: kf6-kcmutils
Version: 5.246.0
Release: %{?git:0.%{git}.}1
%if 0%{?git:1}
Source0: https://invent.kde.org/frameworks/kcmutils/-/archive/master/kcmutils-master.tar.bz2#/kcmutils-%{git}.tar.bz2
%else
Source0: https://download.kde.org/%{stable}/frameworks/%{version}/kcmutils-%{version}.tar.xz
%endif
Summary: Utilities for interacting with KCModules
URL: https://invent.kde.org/frameworks/kcmutils
License: CC0-1.0 LGPL-2.0+ LGPL-2.1 LGPL-3.0
Group: System/Libraries
BuildRequires: cmake
BuildRequires: cmake(ECM)
BuildRequires: python
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6QmlTools)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6GuiTools)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: doxygen
BuildRequires: cmake(Qt6ToolsTools)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6QuickWidgets)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(KF6Activities)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(KF6Package)
BuildRequires: cmake(KF6KIO)
# Just to make sure the KDE 5 version isn't pulled in
BuildRequires: plasma6-xdg-desktop-portal-kde
Requires: %{libname} = %{EVRD}

%description
Utilities for interacting with KCModules

%package -n %{libname}
Summary: Utilities for interacting with KCModules
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
Utilities for interacting with KCModules

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

Utilities for interacting with KCModules

%prep
%autosetup -p1 -n kcmutils-%{?git:master}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%find_lang %{name} --all-name --with-qt --with-html

%files -f %{name}.lang
%{_datadir}/qlogging-categories6/kcmutils.*
%{_bindir}/kcmshell6

%files -n %{devname}
%{_includedir}/KF6/KCMUtils
%{_includedir}/KF6/KCMUtilsCore
%{_includedir}/KF6/KCMUtilsQuick
%{_libdir}/cmake/KF6KCMUtils
%{_qtdir}/doc/KF6KCMUtils.*

%files -n %{libname}
%{_libdir}/libKF6KCMUtils.so*
%{_libdir}/libKF6KCMUtilsCore.so*
%{_libdir}/libKF6KCMUtilsQuick.so*
%{_libdir}/libexec/kf6/kcmdesktopfilegenerator
%{_libdir}/qt6/qml/org/kde/kcmutils
