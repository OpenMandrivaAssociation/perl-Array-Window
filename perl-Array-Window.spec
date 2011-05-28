%define upstream_name    Array-Window
%define upstream_version 1.02

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:	Array-Window Perl module: calculate windows/subsets/pages of arrays
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Array/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(Params::Util)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
Many applications require that a large set of results be broken down
into a smaller set of 'windows', or 'pages' in web language.
Array::Window implements an algorithm specifically for dealing with
these windows. It is very flexible and permissive, making adjustments to
the window as needed.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Array
%{_mandir}/*/*
