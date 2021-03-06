# $Id$
# Authority: shuff
# Upstream: Max Kanat-Alexander <mkanat$cpan,org>
# ExcludeDist: el3 el4

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Math-Random-Secure

Summary: Cryptographically secure, cross-platform replacement for rand()
Name: perl-Math-Random-Secure
Version: 0.05
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Math-Random-Secure/

Source: http://search.cpan.org/CPAN/authors/id/M/MK/MKANAT/Math-Random-Secure-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Any::Moose)
BuildRequires: perl(Crypt::Random::Source) >= 0.07
BuildRequires: perl(ExtUtils::MakeMaker) >= 6.30
BuildRequires: perl(List::MoreUtils)
BuildRequires: perl(Math::Random::ISAAC) >= 1.0.1
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::Warn)
BuildRequires: rpm-macros-rpmforge
Requires: perl
Requires: perl(Any::Moose)
Requires: perl(Crypt::Random::Source) >= 0.07
Requires: perl(Math::Random::ISAAC) >= 1.0.1

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
This module is intended to provide a cryptographically-secure replacement for
Perl's built-in rand function. "Crytographically secure", in this case, means:

* No matter how many numbers you see generated by the random number generator,
  you cannot guess the future numbers, and you cannot guess the seed.
* There are so many possible seeds that it would take decades, centuries, or
  millenia for an attacker to try them all.
* The seed comes from a source that generates relatively strong random data on
  your platform, so the seed itself will be as random as possible. 

%prep
%setup -n %{real_name}-%{version}

# damn it Dist::Zilla
%{?el5:%{__perl} -pi -e '/.*ExtUtils::MakeMaker.*6\.31.*/ && s/6\.3\d/6.30/' Makefile.PL}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install
#%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes LICENSE META.json README
%doc %{_mandir}/man?/*
%{perl_vendorlib}/Math/Random/Secure.pm
%{perl_vendorlib}/Math/Random/Secure/*
#%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/*/.packlist

%changelog
* Mon Jan 24 2011 Steve Huff <shuff@vecna.org> - 0.05-1
- Initial package.
