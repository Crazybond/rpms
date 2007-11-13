# $Id$
# Authority: dag
# Upstream: Marc Lehmann <pcg$goof,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name JSON-XS

Summary: Perl module that implements JSON serialising/deserialising
Name: perl-JSON-XS
Version: 1.52
Release: 1
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/JSON-XS/

Source: http://www.cpan.org/authors/id/M/ML/MLEHMANN/JSON-XS-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
perl-JSON-XS is a Perl module that implements JSON serialising/deserialising,
done correctly and fast.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

### Clean up docs
find eg/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING Changes MANIFEST META.yml README eg/
%doc %{_mandir}/man3/JSON::XS.3pm*
%doc %{_mandir}/man3/JSON::XS::Boolean.3pm*
%dir %{perl_vendorarch}/auto/JSON/
%{perl_vendorarch}/auto/JSON/XS/
%dir %{perl_vendorarch}/JSON/
%{perl_vendorarch}/JSON/XS.pm
%{perl_vendorarch}/JSON/XS/

%changelog
* Tue Nov 13 2007 Dag Wieers <dag@wieers.com> - 1.52-1
- Updated to release 1.52.

* Tue Aug 07 2007 Dag Wieers <dag@wieers.com> - 1.43-2
- Disabled auto-requires for eg/.

* Sat Aug 04 2007 Dag Wieers <dag@wieers.com> - 1.43-1
- Initial package. (using DAR)
