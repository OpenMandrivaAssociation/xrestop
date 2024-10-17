Summary:	X Resource Monitor
Name:		xrestop
Version:	0.6
Release:	1
License:	GPL
Group:		Monitoring
URL:		https://www.freedesktop.org/Software/xrestop
Source0:	https://xorg.freedesktop.org/archive/individual/app/xrestop-%{version}.tar.xz
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xres)
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	ncurses-devel

%description
A utility to monitor the usage of resources within the X Server, and
display them in a manner similar to top.

%prep
%autosetup -p1

%build
%configure
%make_build SUBDIRS=

%install
%make_install SUBDIRS=
%make_install -C doc SUBDIRS=

%files
%{_bindir}/%{name}
%doc %{_mandir}/man1/%{name}*
%doc README* AUTHORS NEWS
