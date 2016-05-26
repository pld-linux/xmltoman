Summary:	Scripts for converting XML to roff or HTML
Name:		xmltoman
Version:	0.4
Release:	1
License:	GPL v2+
Group:		Applications/Publishing
URL:		http://sourceforge.net/projects/xmltoman/
Source0:	http://downloads.sourceforge.net/xmltoman/%{name}-%{version}.tar.gz
# Source0-md5:	99be944b9fce40b3fe397049bf14a097
Patch0:		%{name}-0.3-timestamps.patch
BuildRequires:	perl-XML-Parser
BuildArch:	noarch

%description
This package provides xmltoman and xmlmantohtml scripts, to compile
the xml representation of manual page to either roff source, or HTML
(while providing the CSS stylesheet for eye-candy look). XSL
stylesheet for doing rougly the same job is provided.

%prep
%setup -q
%patch0 -p1 -b .timestamps

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
%attr(755,root,root) %{_bindir}/xmltoman
%attr(755,root,root) %{_bindir}/xmlmantohtml
%{_datadir}/xmltoman
%{_mandir}/man1/*.1*
