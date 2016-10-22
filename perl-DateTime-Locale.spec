%{?scl:%scl_package perl-DateTime-Locale}

Name:           %{?scl_prefix}perl-DateTime-Locale
Version:        1.05
Release:        3%{?dist}
Summary:        Localization support for DateTime.pm
# package itself is 'same terms as Perl'
# modules under DateTime/Locale/ are generated from data provided by the CLDR project
# tools/t/test-data contains CLDR data files under MIT license
License:        (GPL+ or Artistic) and MIT
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/DateTime-Locale/
Source0:        http://www.cpan.org/authors/id/D/DR/DROLSKY/DateTime-Locale-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  %{?scl_prefix}perl
BuildRequires:  %{?scl_prefix}perl-generators
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  %{?scl_prefix}perl(strict)
BuildRequires:  %{?scl_prefix}perl(warnings)
# Runtime
BuildRequires:  %{?scl_prefix}perl(Carp)
# Dist::CheckConflicts 0.02 is optionaly used from Makefile.PL, but it has no
# meaning in minimal build root without useless Perl modules.
BuildRequires:  %{?scl_prefix}perl(Exporter)
BuildRequires:  %{?scl_prefix}perl(List::Util) >= 1.45
BuildRequires:  %{?scl_prefix}perl(Params::Validate)
# Tests only
BuildRequires:  %{?scl_prefix}perl(base)
BuildRequires:  %{?scl_prefix}perl(File::Spec)
BuildRequires:  %{?scl_prefix}perl(Test::Fatal)
BuildRequires:  %{?scl_prefix}perl(Test::More) >= 0.96
BuildRequires:  %{?scl_prefix}perl(Test::Requires)
BuildRequires:  %{?scl_prefix}perl(Test::Warnings)
BuildRequires:  %{?scl_prefix}perl(utf8)
# Optional tests:
BuildRequires:  %{?scl_prefix}perl(CPAN::Meta) >= 2.120900
BuildRequires:  %{?scl_prefix}perl(CPAN::Meta::Prereqs)
BuildRequires:  %{?scl_prefix}perl(Storable)
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%(%{?scl:scl enable %{scl} '}eval "$(perl -V:version)";echo $version%{?scl:'}))
Requires:       %{?scl_prefix}perl(Dist::CheckConflicts) >= 0.02
# perl-DateTime-Locale used to be bundled with perl-DateTime
# ideally, this would be resolved with
# Requires:     %{?scl_prefix}perl-DateTime >= 2:0.70-1
# but DateTime::Locale doesn't strictly require DateTime
# and this would introduce circular build dependencies
Conflicts:      %{?scl_prefix}perl-DateTime <= 1:0.7000-3.fc16

%if 0%{?rhel} < 7
# RPM 4.8 style
%{?filter_setup:
%filter_from_requires /^%{?scl_prefix}perl(Dist::CheckConflicts)$/d
%?perl_default_filter
}
%else
# RPM 4.9 style
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^%{?scl_prefix}perl\\(Dist::CheckConflicts\\)$
%endif

%description
DateTime::Locale is primarily a factory for the various locale sub-classes.
It also provides some functions for getting information on all the
available locales.

%prep
%setup -q -n DateTime-Locale-%{version}

%build
%{?scl:scl enable %{scl} '}perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 && make %{?_smp_mflags}%{?scl:'}

%install
%{?scl:scl enable %{scl} '}make pure_install DESTDIR=%{buildroot}%{?scl:'}
%{_fixperms} %{buildroot}/*

%check
%{?scl:scl enable %{scl} '}make test%{?scl:'}

%files
%doc LICENSE LICENSE.cldr
%doc Changes CONTRIBUTING.md README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed Jul 13 2016 Petr Pisar <ppisar@redhat.com> - 1.05-3
- SCL

* Wed Jul 13 2016 Petr Pisar <ppisar@redhat.com> - 1.05-2
- Simplify optional build-time dependencies

* Mon Jun 27 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.05-1
- 1.05 bump

* Mon Jun 20 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.04-1
- 1.04 bump

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.03-2
- Perl 5.24 rebuild

* Tue Mar 29 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.03-1
- 1.03 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.02-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Dec 11 2015 Petr Šabata <contyk@redhat.com> - 1.02-1
- 1.02 bump

* Tue Nov 10 2015 Petr Šabata <contyk@redhat.com> - 1.01-1
- 1.01 bump, lots of backwards incompatible changes

* Tue Sep 29 2015 Petr Šabata <contyk@redhat.com> - 0.92-1
- 0.92 bump, no changes (yet)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.46-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.46-2
- Perl 5.22 rebuild

* Wed May 27 2015 Petr Šabata <contyk@redhat.com> - 0.46-1
- 0.46 bump

* Tue Jan 13 2015 Petr Pisar <ppisar@redhat.com> - 0.45-11
- Modernize spec file

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.45-10
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.45-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.45-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jul 26 2013 Petr Pisar <ppisar@redhat.com> - 0.45-7
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.45-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Nov 13 2012 Marcela Mašláňová <mmaslano@redhat.com> - 0.45-5
- Add BR, fix whitespaces

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.45-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 19 2012 Petr Pisar <ppisar@redhat.com> - 0.45-3
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.45-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Aug 15 2011 Iain Arnell <iarnell@gmail.com> 0.45-1
- Specfile autogenerated by cpanspec 1.78.
