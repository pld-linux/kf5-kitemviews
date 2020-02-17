%define		kdeframever	5.67
%define		qtver		5.9.0
%define		kfname		kitemviews

Summary:	Set of item views extending the Qt model-view framework
Name:		kf5-%{kfname}
Version:	5.67.0
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/frameworks/%{kdeframever}/%{kfname}-%{version}.tar.xz
# Source0-md5:	76990691b3c57e9c02c5da55144764a4
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= %{qtver}
BuildRequires:	Qt5Test-devel >= %{qtver}
BuildRequires:	Qt5Widgets-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	kf5-extra-cmake-modules >= 1.4.0
BuildRequires:	ninja
BuildRequires:	qt5-linguist >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	kf5-dirs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt5dir		%{_libdir}/qt5

%description
KItemViews includes a set of views, which can be used with item
models. It includes views for categorizing lists and to add search
filters to flat and hierarchical lists.

%package devel
Summary:	Header files for %{kfname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kfname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	Qt5Widgets-devel >= %{qtver}
Requires:	cmake >= 2.6.0

%description devel
Header files for %{kfname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kfname}.

%prep
%setup -q -n %{kfname}-%{version}

%build
install -d build
cd build
%cmake -G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	../
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kfname}5_qt --with-qm --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{kfname}5_qt.lang
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %ghost %{_libdir}/libKF5ItemViews.so.5
%attr(755,root,root) %{_libdir}/libKF5ItemViews.so.*.*
%attr(755,root,root) %{_libdir}/qt5/plugins/designer/kitemviews5widgets.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF5/KItemViews
%{_includedir}/KF5/kitemviews_version.h
%{_libdir}/cmake/KF5ItemViews
%attr(755,root,root) %{_libdir}/libKF5ItemViews.so
%{qt5dir}/mkspecs/modules/qt_KItemViews.pri
