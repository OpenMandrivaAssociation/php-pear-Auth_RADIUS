%define		_class		Auth
%define		_subclass	RADIUS
%define		upstream_name	%{_class}_%{_subclass}

%define		_requires_exceptions pear(Crypt_CHAP/CHAP.php)

Name:		php-pear-%{upstream_name}
Version:	1.0.7
Release:	%mkrel 3
Summary:	Wrapper Classes for the RADIUS PECL
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/Auth_RADIUS/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tar.bz2
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
Requires:	php-radius
BuildRequires:	php-pear
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This package provides wrapper-classes for the RADIUS PECL. There are
different Classes for the different authentication methods. If you are
using CHAP-MD5 or MS-CHAP you need also the Crypt_CHAP package. If you
are using MS-CHAP you need also the mhash extension.

In PEAR status of this package is: %{_status}.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install
rm -rf %{buildroot}

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean
rm -rf %{buildroot}

%post
%if %mdkversion < 201000
pear install --nodeps --soft --force --register-only \
    %{_datadir}/pear/packages/%{upstream_name}.xml >/dev/null || :
%endif

%preun
%if %mdkversion < 201000
if [ "$1" -eq "0" ]; then
    pear uninstall --nodeps --ignore-errors --register-only \
        %{upstream_name} >/dev/null || :
fi
%endif

%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/examples
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml




%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.7-3mdv2012.0
+ Revision: 741825
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.7-2
+ Revision: 679264
- mass rebuild

* Sun Nov 07 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.7-1mdv2011.0
+ Revision: 594481
- update to new version 1.0.7

* Tue Nov 10 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.6-4mdv2010.1
+ Revision: 464359
- spec cleanup
- use rpm filetriggers to register starting from mandriva 2010.1

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 1.0.6-2mdv2009.1
+ Revision: 321898
- rebuild

* Tue Sep 02 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.6-1mdv2009.0
+ Revision: 278910
- update to new version 1.0.6

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0.5-2mdv2009.0
+ Revision: 236803
- rebuild

* Wed Jan 02 2008 Olivier Blin <blino@mandriva.org> 1.0.5-1mdv2008.1
+ Revision: 140729
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Apr 20 2007 Oden Eriksson <oeriksson@mandriva.com> 1.0.5-1mdv2008.0
+ Revision: 15639
- 1.0.5


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 1.0.4-7mdv2007.0
+ Revision: 81366
- Import php-pear-Auth_RADIUS

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 1.0.4-7mdk
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.4-6mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.4-5mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.4-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.4-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.4-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.4-1mdk
- initial Mandriva package (PLD import)

