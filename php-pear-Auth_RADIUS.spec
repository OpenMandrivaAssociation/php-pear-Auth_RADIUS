%define		_class		Auth
%define		_subclass	RADIUS
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

%define		_requires_exceptions pear(Crypt_CHAP/CHAP.php)

Summary:	%{_pearname} - Wrapper Classes for the RADIUS PECL
Name:		php-pear-%{_pearname}
Version:	1.0.5
Release:	%mkrel 2
License:	PHP License
Group:		Development/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tar.bz2
URL:		http://pear.php.net/package/Auth_RADIUS/
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
Requires:	php-radius
BuildArch:	noarch
BuildRequires:	dos2unix
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This package provides wrapper-classes for the RADIUS PECL. There are
different Classes for the different authentication methods. If you are
using CHAP-MD5 or MS-CHAP you need also the Crypt_CHAP package. If you
are using MS-CHAP you need also the mhash extension.

In PEAR status of this package is: %{_status}.

%prep

%setup -q -c

find . -type d -perm 0700 -exec chmod 755 {} \;
find . -type f -perm 0555 -exec chmod 755 {} \;
find . -type f -perm 0444 -exec chmod 644 {} \;

for i in `find . -type d -name CVS` `find . -type f -name .cvs\*` `find . -type f -name .#\*`; do
    if [ -e "$i" ]; then rm -rf $i; fi >&/dev/null
done

# strip away annoying ^M
find -type f | grep -v ".gif" | grep -v ".png" | grep -v ".jpg" | xargs dos2unix -U

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_datadir}/pear/%{_class}/

install %{_pearname}-%{version}/*.php %{buildroot}%{_datadir}/pear/%{_class}

install -d %{buildroot}%{_datadir}/pear/packages
install -m0644 package.xml %{buildroot}%{_datadir}/pear/packages/%{_pearname}.xml

%post
if [ "$1" = "1" ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear install --nodeps -r %{_datadir}/pear/packages/%{_pearname}.xml
	fi
fi
if [ "$1" = "2" ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear upgrade -f --nodeps -r %{_datadir}/pear/packages/%{_pearname}.xml
	fi
fi

%preun
if [ "$1" = 0 ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear uninstall --nodeps -r %{_pearname}
	fi
fi

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/examples/*
%{_datadir}/pear/%{_class}/*.php
%{_datadir}/pear/packages/%{_pearname}.xml


