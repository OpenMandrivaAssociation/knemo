%define	name	knemo
%define	version	0.5.1
%define	release	%mkrel 1
%define	Summary	The KDE Network Monitor

Summary:	%{Summary}
Name:		%{name}
Version:	%{version}
Release:	%{release}

License:	GPL
Group:		Graphical desktop/KDE
Source0:	%{name}-%{version}.tar.gz
URL:		http://kde-apps.org/content/show.php?content=12956

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	kdelibs4-devel
BuildRequires:  libiw-devel
Requires:	wireless-tools

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

%files -f %{name}.lang
%defattr(-,root,root)
%_kde_bindir/knemo
%_kde_libdir/kde4/kcm_knemo.so
%_kde_datadir/applications/kde4/knemo.desktop
%_kde_appsdir/knemo
%_kde_datadir/autostart/knemo.desktop
%_kde_iconsdir/hicolor/*/apps/*
%_kde_datadir/kde4/services/kcm_knemo.desktop

#--------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
rm -rf %{buildroot}
%makeinstall_std -C build

%find_lang %{name} %{name} kcm_knemo knemod

%clean
rm -rf %{buildroot}
