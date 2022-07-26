
Summary:	X Resource Monitor
Name:		xrestop
Version:	0.5
Release:	1
License:	GPL
Group:		Monitoring
URL:		http://www.freedesktop.org/Software/xrestop
Source0:		https://xorg.freedesktop.org/archive/individual/app/xrestop-%{version}.tar.bz2
BuildRequires:	pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xres)
BuildRequires:	ncurses-devel

%description
A utility to monitor the usage of resources within the X Server, and
display them in a manner similar to top.

%prep
%setup -q

%build
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


%changelog
* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 0.4-11mdv2011.0
+ Revision: 615734
- the mass rebuild of 2010.1 packages

* Mon Apr 19 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 0.4-10mdv2010.1
+ Revision: 536774
- rebuild

* Wed Sep 09 2009 Thierry Vignaud <tv@mandriva.org> 0.4-9mdv2010.0
+ Revision: 435271
- rebuild

* Mon Aug 04 2008 Thierry Vignaud <tv@mandriva.org> 0.4-8mdv2009.0
+ Revision: 262702
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.4-7mdv2009.0
+ Revision: 257690
- rebuild

* Tue Feb 12 2008 Paulo Andrade <pcpa@mandriva.com.br> 0.4-5mdv2008.1
+ Revision: 166801
- Revert to use upstream tarball, build requires and remove non mandatory local patches.

* Thu Jan 17 2008 Paulo Andrade <pcpa@mandriva.com.br> 0.4-4mdv2008.1
+ Revision: 154353
- Modified to use git-archive to generate tarball.
  Missing Changelog file can be rebuilt with something like git-log | git-shortlog
  This is also an interesting package, as it is licensed under GPL but
  in the X Org tree / repository......

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.4-3mdv2008.1
+ Revision: 136618
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Feb 09 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 0.4-3mdv2007.0
+ Revision: 118533
- Removed menu entries. This is a command line utility. (#28187)
- Import xrestop

* Tue Sep 05 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.4-2mdv2007.0
- XDG

* Mon Mar 13 2006 Lenny Cartier <lenny@mandriva.com> 0.4-1mdk
- 0.4

* Fri Oct 29 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 0.3-1mdk
- 0.3

* Thu Feb 26 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.2-5mdk
- fix typo in longtitle
- fix group
- cleanups 
- added docs

* Thu Feb 26 2004 Emmanuel Blindauer <manu@agat.net> 0.2-4mdk
- Rebuild

