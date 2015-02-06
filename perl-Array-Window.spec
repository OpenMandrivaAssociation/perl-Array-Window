%define upstream_name    Array-Window
%define upstream_version 1.02

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Array-Window Perl module: calculate windows/subsets/pages of arrays
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Array/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Params::Util)
BuildArch:	noarch

%description
Many applications require that a large set of results be broken down
into a smaller set of 'windows', or 'pages' in web language.
Array::Window implements an algorithm specifically for dealing with
these windows. It is very flexible and permissive, making adjustments to
the window as needed.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Array
%{_mandir}/*/*


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 1.20.0-2mdv2011.0
+ Revision: 680478
- mass rebuild

* Wed Jul 29 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.20.0-1mdv2011.0
+ Revision: 402981
- rebuild using %%perl_convert_version

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 1.02-2mdv2009.0
+ Revision: 268369
- rebuild early 2009.0 package (before pixel changes)

* Sat Jun 07 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.02-1mdv2009.0
+ Revision: 216627
- dont change source compression
- update to new version 1.02

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Jul 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.01-1mdv2008.0
+ Revision: 46312
- update to new version 1.01


* Fri Oct 27 2006 Nicolas LÃ©cureuil <neoclust@mandriva.org> 0.4-2mdv2007.0
+ Revision: 73298
- import perl-Array-Window-0.4-2mdk

* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.4-2mdk
- Fix SPEC Using perl Policies
	- Source URL
- use mkrel

* Thu Jul 14 2005 Oden Eriksson <oeriksson@mandriva.com> 0.4-1mdk
- initial Mandriva package

