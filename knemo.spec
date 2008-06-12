%define	name	knemo
%define	version	0.4.8
%define	release	%mkrel 1
%define	Summary	The KDE Network Monitor

Summary:	%{Summary}
Name:		%{name}
Version:	%{version}
Release:	%{release}

License:	GPL
Group:		Graphical desktop/KDE
Source0:	%{name}-%{version}.tar.bz2
URL:		http://kde-apps.org/content/show.php?content=12956

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	kdelibs-devel
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

%prep
%setup -q

%build
%configure2_5x	--disable-rpath \
		--enable-final

%make

%install
rm -rf %{buildroot}
%makeinstall

%find_lang %{name} %{name} kcm_knemo knemod

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%{update_menus}
%update_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%clean_icon_cache hicolor
%endif

%files -f %{name}.lang
%defattr(-,root,root)
%{_libdir}/kde3/kcm_knemo.la
%{_libdir}/kde3/kcm_knemo.so
%{_libdir}/kde3/kded_knemod.la
%{_libdir}/kde3/kded_knemod.so
%{_datadir}/applications/kde/kcm_knemo.desktop
%{_datadir}/services/kded/knemod.desktop
%{_datadir}/icons/*/*/*/*.png
%{_datadir}/apps/knemo
