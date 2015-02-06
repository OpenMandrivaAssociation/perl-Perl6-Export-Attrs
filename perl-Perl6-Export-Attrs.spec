
%define realname   Perl6-Export-Attrs
%define version    0.0.3
%define release    5

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    The Perl 6 'is export(...)' trait as a Perl 5 attribute
Source:     http://www.cpan.org/modules/by-module/Perl6/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel


BuildArch: noarch

%description
Implements a Perl 5 native version of what the Perl 6 symbol export
mechanism will look like.

It's very straightforward:

* *

%prep
%setup -q -n %{realname}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*




%changelog
* Mon Apr 25 2011 Funda Wang <fwang@mandriva.org> 0.0.3-3mdv2011.0
+ Revision: 658873
- rebuild for updated spec-helper

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 0.0.3-2mdv2010.0
+ Revision: 440616
- rebuild

* Fri Feb 20 2009 Jérôme Quelin <jquelin@mandriva.org> 0.0.3-1mdv2009.1
+ Revision: 343331
- import perl-Perl6-Export-Attrs


* Fri Feb 20 2009 cpan2dist 0.0.3-1mdv
- initial mdv release, generated with cpan2dist

