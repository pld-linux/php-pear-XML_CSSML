%include	/usr/lib/rpm/macros.php
%define         _class          XML
%define         _subclass       CSSML
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_class}_%{_subclass} - methods for creating cascading style sheets (CSS)
Summary(pl):	%{_class}_%{_subclass} - metody do tworzenia styl�w kaskadowych (CSS)
Name:		php-pear-%{_pearname}
Version:	1.1
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov
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
http://mojave.mojavelinux.com/forum/viewtopic.php?p=22#22

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}_%{_subclass}/%{_subclass}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}_%{_subclass}
install %{_pearname}-%{version}/%{_subclass}/* $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}_%{_subclass}/%{_subclass}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/docs/*
%dir %{php_pear_dir}/%{_class}_%{_subclass}
%dir %{php_pear_dir}/%{_class}_%{_subclass}/%{_subclass}
%{php_pear_dir}/%{_class}_%{_subclass}/*.php
%{php_pear_dir}/%{_class}_%{_subclass}/%{_subclass}/*
