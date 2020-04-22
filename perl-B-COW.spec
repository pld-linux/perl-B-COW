#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	B
%define		pnam	COW
Summary:	B::COW - additional B helpers to check COW status
Summary(pl.UTF-8):	B::COW - dodatkowe funkcje pomocnicze B do sprawdzania stanu COW
Name:		perl-B-COW
Version:	0.003
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/B/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7993aed7be7b894c4883e3ac54769b1d
URL:		https://metacpan.org/release/B-COW
%if %{with tests}
BuildRequires:	perl-Test-Simple
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
B::COW provides some naive additional B helpers to check the COW
(Copy On Write) status of one SvPV. COWed SvPV is sharing its string
(the PV) with other SvPVs. It's a (kind of) Read Only C string, that
would be Copied On Write (COW).

%description -l pl.UTF-8
B::COW udostępnia kilka prostych, dodatkowych funkcji pomocniczych B
do sprawdzania stanu COW (Copy On Write). Kopiowany przy zapisie SvPV
współdzieli swój łańcuch znaków (PV) z innymi SvPV. Jest to rodzaj
łańucha znaków C tylko do odczytu, który zostałby skopiowany przy
zapisie (Copied On Write).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes 
%{perl_vendorarch}/B/COW.pm
%dir %{perl_vendorarch}/auto/B/COW
%attr(755,root,root) %{perl_vendorarch}/auto/B/COW/COW.so
%{_mandir}/man3/B::COW.3pm*
