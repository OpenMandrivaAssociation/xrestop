Summary:	X Resource Monitor
Name:		xrestop
Version:	0.4
Release:	%mkrel 4
License:	GPL
Group:		Monitoring
URL:		http://xorg.freedesktop.org
# Note local xrestop-0.4@mandriva suggested on upstream
# Tag at git checkout 08c9daab3a0b3ef37723c007858fa949cb91bbd8
########################################################################
# git clone git://git.mandriva.com/people/pcpa/xorg/app/xrestop xorg/app/xrestop
# cd xorg/app/xrestop
# git-archive --format=tar --prefix=xrestop-0.4/ xrestop-0.4@mandriva | bzip2 -9 > xrestop-0.4.tar.bz2
########################################################################
Source0:	%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires:	libx11-devel	>= 1.1.3
BuildRequires:  libxres-devel	>= 1.0.3
BuildRequires:  ncurses-devel
BuildRequires:  libxext-devel	>= 1.0.3

%description
A utility to monitor the usage of resources within the X Server, and
display them in a manner similar to top.

%prep
%setup -q

%build
autoreconf -ifs
%configure
%make SUBDIRS=

%install
rm -rf %{buildroot}
%makeinstall_std SUBDIRS=
%makeinstall_std -C doc SUBDIRS=

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}
%{_mandir}/man1/%{name}*
%doc README AUTHORS NEWS
