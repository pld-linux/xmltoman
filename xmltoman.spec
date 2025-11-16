Summary:	Scripts for converting XML to roff or HTML
Summary(pl.UTF-8):	Skrypty do konwersji XML-a do formatu roff lub HTML
Name:		xmltoman
Version:	0.4
Release:	2
License:	GPL v2+
Group:		Applications/Publishing
Source0:	http://downloads.sourceforge.net/xmltoman/%{name}-%{version}.tar.gz
# Source0-md5:	99be944b9fce40b3fe397049bf14a097
Patch0:		%{name}-0.3-timestamps.patch
URL:		http://sourceforge.net/projects/xmltoman/
BuildRequires:	perl-XML-Parser
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides xmltoman and xmlmantohtml scripts, to compile
the XML representation of manual page to either roff source, or HTML
(while providing the CSS stylesheet for eye-candy look). XSL
stylesheet for doing rougly the same job is provided.

%description -l pl,UTF-8
Ten pakiet zawiera skrypty xmltoman oraz xmlmantohtml służące do
kompilacji reprezentacji XML stron podręcznika do postaci źródłowej
roff lub HTML-a (z dostarczeniem arkusza CSS dla ładnego wyglądu).
Załączony jest także arkusz XSL do wykonywania analogicznych zadań.

%prep
%setup -q
%patch -P0 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man1

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix}

cp -p *.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/xmlmantohtml
%attr(755,root,root) %{_bindir}/xmltoman
%{_datadir}/xmltoman
%{_mandir}/man1/xmlmantohtml.1*
%{_mandir}/man1/xmltoman.1*
