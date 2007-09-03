%include	/usr/lib/rpm/macros.php
%define		_class		Structures
%define		_subclass	DataGrid_Renderer_Flexy
%define		_status		alpha
%define		_pearname	Structures_DataGrid_Renderer_Flexy
Summary:	%{_pearname} - renderer driver using Flexy
Summary(pl.UTF-8):	%{_pearname} - sterownik renderera wykorzystujący Flexy
Name:		php-pear-%{_pearname}
Version:	0.1.3
Release:	1
License:	PHP License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	dabe6e44be276e6a9091dea03bc8aec5
URL:		http://pear.php.net/package/Structures_DataGrid_Renderer_Flexy/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Requires:	php-pear-PEAR >= 1.4.9
Requires:	php-pear-Structures_DataGrid >= 0.7.1
Requires:	php-pear-Structures_DataGrid_Renderer_Pager >= 0.1.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a Renderer driver for Structures_DataGrid using
HTML_Template_Flexy. It adds a couple of variables to a Flexy instance
and adds paging functionality. This renderer also enables customised
result messages, customised column labels and a column label
formatter.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Ten pakiet dostarcza sterownik renderara dla Structures_DataGrid
korzystający z HTML_Template_Flexy. Dodaje kilka dodatkowych zmiennych
do instancji Flexy oraz możliwość podziału na strony. Renderer pozwala
takze na kofnigurowanie wyników, etykiet oraz formatowaina kolumn.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log docs/Structures_DataGrid_Renderer_Flexy/examples/
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Structures/DataGrid/Renderer/Flexy.php
