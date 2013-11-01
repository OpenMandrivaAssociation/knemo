Summary:	The KDE Network Monitor
Name:		knemo
Version:	0.7.6
Release:	2
License:	GPL
Group:		Graphical desktop/KDE
Source0:	http://kde-apps.org/CONTENT/content-files/12956-%{name}-%{version}.tar.bz2
URL:		http://kde-apps.org/content/show.php?content=12956
BuildRequires:	kdelibs4-devel
BuildRequires:	libiw-devel
BuildRequires:	pkgconfig(libnl-3.0)
BuildRequires:	kdebase4-workspace-devel
Requires:	wireless-tools
Requires:	qt4-database-plugin-sqlite

%description
KNemo offers a network monitor similar to the one found in Windows. 
For every network interface it displays an icon in the systray.

Features:
* support for ethernet (including wireless) and ppp connections
* the icon shows incoming/outgoing traffic
* hiding of icon when the interface is not available
* automatic detection of wireless extensions for ethernet interfaces
* left-clicking on an icon displays a status dialog with information
  about the selected interface (2nd click hides dialog)
* configuration via context menu or control center module
  (Internet & Network/Network Monitor)
* customizable tooltip for quick access to often needed information
* you can activate 2 custom entries for the context menu. They can
  have custom text and a command to run when selected. You can even
  select if the commands need root permissions or not.
* automatic detection of available interfaces (click on 'Default' in
  the configuration dialog and KNemo will look under /proc/net/dev for
  interfaces)
* KNemo uses more standard icon names which allows support from other
  icon themes.

Please make sure that in the settings the paths for 'ifconfig' and 'iwconfig'
are correct and that both programs are installed.

IMPORTANT: KNemo is not an executable but an KDED service. Therefore
it has to be started using Control Center/KDE Components/Service Manager.

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%find_lang %{name} kcm_knemo knemod %{name}.lang

%files -f %{name}.lang
%{_kde_bindir}/knemo
%{_kde_libdir}/kde4/kcm_knemo.so
%{_kde_applicationsdir}/knemo.desktop
%{_kde_appsdir}/knemo
%{_kde_appsdir}/kconf_update/*
%{_kde_datadir}/autostart/knemo.desktop
%{_kde_iconsdir}/hicolor/*/*/*
%{_kde_services}/kcm_knemo.desktop
