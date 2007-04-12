%define real_name Array-Window

Summary:	Array-Window Perl module: calculate windows/subsets/pages of arrays
Name:		perl-%{real_name}
Version:	0.4
Release: %mkrel 2
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Array/%{real_name}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Many applications require that a large set of results be broken down
into a smaller set of 'windows', or 'pages' in web language.
Array::Window implements an algorithm specifically for dealing with
these windows. It is very flexible and permissive, making adjustments to
the window as needed.

%prep
%setup -q -n %{real_name}-%{version} 

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
%{perl_vendorlib}/Array/Window.pm
%{_mandir}/*/*




