%define	name	xrestop
%define	version	0.4
%define	release	%mkrel 3

Summary:	X Resource Monitor
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Monitoring
URL:		http://www.freedesktop.org/Software/xrestop
Source0:	%{name}-%{version}.tar.bz2
BuildRequires:	libx11-devel
BuildRequires:  libxext-devel
BuildRequires:  libxres-devel
BuildRequires:  ncurses-devel

%description
A utility to monitor the usage of resources within the X Server, and
display them in a manner similar to top.

%prep
%setup -q

%build
%configure
%make SUBDIRS=

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std SUBDIRS=
%makeinstall_std -C doc SUBDIRS=

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}
%{_mandir}/man1/%{name}*
%doc README AUTHORS ChangeLog NEWS


