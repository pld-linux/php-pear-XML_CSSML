%include	/usr/lib/rpm/macros.php
%define		_class		XML
%define		_subclass	CSSML
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - methods for creating cascading style sheets (CSS)
Summary(pl.UTF-8):	%{_pearname} - metody do tworzenia stylów kaskadowych (CSS)
Name:		php-pear-%{_pearname}
Version:	1.1.1
Release:	4
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	30913ea7139ed4242c17b69737f074f0
Patch0:		%{name}-path_fix.patch
URL:		http://pear.php.net/package/XML_CSSML/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-common < 3:5.0.0
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The best way to describe this library is to classify it as a template
system for generating cascading style sheets (CSS). It is ideal for
storing all of the CSS in a single location and allowing it to be
parsed as needed at runtime (or from cache) using both general and
browser filters specified in the attribute for the style tags. It can
be driven with either the libxslt pear extenstion (part of xmldom) or
the xslt extension (part of the sablotron libraries). You may see an
example usage of this class at the follow url:
<http://mojave.mojavelinux.com/forum/viewtopic.php?p=22#22>

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Najlepszym sposobem na opisanie tej biblioteki jest sklasyfikowanie
jej jako system szablonów do generowania arkuszy CSS. Jest idealny do
przechowywania wszystkich CSS w jednym miejscu i pozwalania na
analizowanie ich w miarę potrzeby przy użyciu filtrów, zarówno
ogólnego, jak i dla przeglądarek - podanych w atrybucie znaczników
stylu. Biblioteka może polegać na rozszerzeniu PEAR-a libxslt
(będącego częścią xmldom) lub rozszerzeniu xslt (będącego częścią
bibliotek sablotron). Przykład użycia klasy można obejrzeć pod
adresem: <http://mojave.mojavelinux.com/forum/viewtopic.php?p=22#22>

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

install -d docs/%{_pearname}
mv ./%{php_pear_dir}/%{_class}/docs/* docs/%{_pearname}

# we do backward compat with symlink.
rm -rf ./%{php_pear_dir}/%{_pearname}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install
ln -s %{_class} $RPM_BUILD_ROOT%{php_pear_dir}/%{_pearname}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}
# BC for bug #5574
%{php_pear_dir}/%{_pearname}
