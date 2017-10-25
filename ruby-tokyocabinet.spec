Summary:	Ruby binding for Tokyo Cabinet
Summary(pl.UTF-8):	Wiązania języka Ruby do biblioteki Tokyo Cabinet
Name:		ruby-tokyocabinet
Version:	1.31
Release:	2
License:	LGPL v2.1+
Source0:	http://fallabs.com/tokyocabinet/rubypkg/tokyocabinet-ruby-%{version}.tar.gz
# Source0-md5:	8e71f49c5ae2cb8c46f5c2e5f43c182c
Patch0:		%{name}-gemspec.patch
Group:		Development/Languages
URL:		http://fallabs.com/tokyocabinet/
BuildRequires:	bzip2-devel
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.665
BuildRequires:	ruby-devel
BuildRequires:	tokyocabinet-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tokyo Cabinet is a library of routines for managing a database. The
database is a simple data file containing records, each is a pair of a
key and a value. Every key and value is serial bytes with variable
length. Both binary data and character string can be used as a key and
a value. There is neither concept of data tables nor data types.
Records are organized in hash table, B+ tree, or fixed-length array.

This package contains Ruby binding for the library.

%description -l pl.UTF-8
Tokyo Cabinet to biblioteka procedur do zarządzania bazą danych. Baza
danych to prosty plik danych zawierający pary klucz-wartość. Każdy
klucz oraz wartość to szereg bajtów o zmiennej długości. Jako kluczy
oraz wartości można używać zarówno danych binarnych, jak i łańcuchów
znaków. Nie ma konceptu tabel danych ani typów danych. Rekordy są
zorganizowane w tablicy haszującej, B+ drzewie lub tablicy o stałej
długości.

Ten pakiet zawiera wiązania języka Ruby do biblioteki.

%prep
%setup -q -n tokyocabinet-ruby-%{version}
%patch0 -p1

%build
ruby extconf.rb --vendor

%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} %{rpmcppflags} -fPIC -I." \
	ldflags="%{rpmldflags}"

%{__sed} -e '/^if \$0/,$d' tokyocabinet.gemspec > tokyocabinet-%{version}.gemspec

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{ruby_specdir}
cp -p tokyocabinet-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

%{__rm} doc/created.rid

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*
%attr(755,root,root) %{ruby_vendorarchdir}/tokyocabinet.so
%{ruby_specdir}/tokyocabinet-%{version}.gemspec
