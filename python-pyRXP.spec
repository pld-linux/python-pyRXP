
#
# todo:
# - use external rxp
# - make documentation from rml file instead of downloading it
#   (need for spec for http://www.reportlab.org/rl_toolkit.html)
#

%include	/usr/lib/rpm/macros.python

%define	module	pyRXP

Summary:	A Python wrapper for the RXP parser
Summary(pl):	Pythonowy interfejs do analizatora XML RXP
Name:		python-%{module}
Version:	0.9
Release:	2
License:	GPL v2
Group:		Libraries/Python
Source0:	http://www.reportlab.org/ftp/%{module}-0-9.tgz
# Source0-md5:	7d69870d3884f9e40f111a62525e0d77
Source1:	http://www.reportlab.com/docs/PyRXP_Documentation.pdf
# Source1-md5:	3ae69ba61f1facea5b76e91dbee8718e
URL:		http://www.reportlab.org/pyrxp.html
BuildRequires:	python-devel >= 2.2.1
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pyRXP is a Python wrapper for RXP, a validating namespace-aware
XML parser in C.

%description -l pl
pyRXP to pythonowy interfejs do RXP - kontroluj±cego poprawno¶æ
analizatora XML-a z obs³ug± przestrzeni nazw, napisanego w C.

%package doc
Summary:	Documentation for Python pyRXP module
Summary(pl):	Dokumentacja do modu³u Pythona pyRXP
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description doc
This package contains documentation files for Python pyRXP module.

%description doc -l pl
Pakiet zawieraj±cy dokumentacjê dla modu³u Pythona pyRXP.

%package examples
Summary:	Example programs for Python pyRXP module
Summary(pl):	Programy przyk³adowe do modu³u Pythona pyRXP
Group:		Development/Languages/Python
Requires:	%{name} = %{version}-%{release}

%description examples
This package contains example programs for Python pyRXP module.

%description examples -l pl
Pakiet zawieraj±cy programy przyk³adowe dla modu³u Pythona pyRXP.

%prep
%setup -q -c %{module}-%{version}

%build
CFLAGS="%{rpmcflags}"
export CFLAGS
python setup.py build

cp -a %{SOURCE1} docs

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{py_sitedir},%{_examplesdir}/%{name}-%{version}}

python setup.py install \
	--root=$RPM_BUILD_ROOT --optimize=2

cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{py_sitedir}/*.so

%files doc
%defattr(644,root,root,755)
%doc docs/PyRXP_Documentation.pdf

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
