#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Text-Levenshtein
Version  : 0.14
Release  : 14
URL      : https://cpan.metacpan.org/authors/id/N/NE/NEILB/Text-Levenshtein-0.14.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/N/NE/NEILB/Text-Levenshtein-0.14.tar.gz
Summary  : 'calculate the Levenshtein edit distance between two strings'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Text-Levenshtein-license = %{version}-%{release}
Requires: perl-Text-Levenshtein-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
Text::Levenshtein is an implementation of the Levenshtein edit distance in Perl.
If you're not familiar with this algorithm, a good place to start is
the wikipedia page:

%package dev
Summary: dev components for the perl-Text-Levenshtein package.
Group: Development
Provides: perl-Text-Levenshtein-devel = %{version}-%{release}
Requires: perl-Text-Levenshtein = %{version}-%{release}

%description dev
dev components for the perl-Text-Levenshtein package.


%package license
Summary: license components for the perl-Text-Levenshtein package.
Group: Default

%description license
license components for the perl-Text-Levenshtein package.


%package perl
Summary: perl components for the perl-Text-Levenshtein package.
Group: Default
Requires: perl-Text-Levenshtein = %{version}-%{release}

%description perl
perl components for the perl-Text-Levenshtein package.


%prep
%setup -q -n Text-Levenshtein-0.14
cd %{_builddir}/Text-Levenshtein-0.14

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Text-Levenshtein
cp %{_builddir}/Text-Levenshtein-0.14/LICENSE %{buildroot}/usr/share/package-licenses/perl-Text-Levenshtein/ac6003ce40240de25b30d7e17ee93cb8616443be
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Text::Levenshtein.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Text-Levenshtein/ac6003ce40240de25b30d7e17ee93cb8616443be

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.32.1/Text/Levenshtein.pm
