%define module Array-Window

Summary:	Array-Window Perl module: calculate windows/subsets/pages of arrays
Name:		perl-%{module}
Version:	1.02
Release: %mkrel 2
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/Array/%{module}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Params::Util)
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Many applications require that a large set of results be broken down
into a smaller set of 'windows', or 'pages' in web language.
Array::Window implements an algorithm specifically for dealing with
these windows. It is very flexible and permissive, making adjustments to
the window as needed.

%prep
%setup -q -n %{module}-%{version} 

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




