
#
# todo:
# - use external rxp
# - make documentation from rml file instead of downloading it
#   (need for spec for http://www.reportlab.org/rl_toolkit.html)
#

%define		_snap	20071106
%define		module	pyRXP

Summary:	A Python wrapper for the RXP parser
Summary(pl.UTF-8):	Pythonowy interfejs do analizatora XML RXP
Name:		python-%{module}
Version:	1.12
Release:	1
License:	GPL v2
Group:		Libraries/Python
Source0:	http://www.reportlab.org/daily/%{module}-%{version}-daily-unix.tgz
# Source0-md5:	614ec61a1f65231e8018897b5f5e2f5f
Source1:	http://www.reportlab.com/docs/PyRXP_Documentation.pdf
# Source1-md5:	984096b03131336f4eb53de829782576
URL:		http://www.reportlab.org/pyrxp.html
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pyRXP is a Python wrapper for RXP, a validating namespace-aware
XML parser in C.

%description -l pl.UTF-8
pyRXP to pythonowy interfejs do RXP - kontrolującego poprawność
analizatora XML-a z obsługą przestrzeni nazw, napisanego w C.

%package doc
Summary:	Documentation for Python pyRXP module
Summary(pl.UTF-8):	Dokumentacja do modułu Pythona pyRXP
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description doc
This package contains documentation files for Python pyRXP module.

%description doc -l pl.UTF-8
Pakiet zawierający dokumentację dla modułu Pythona pyRXP.

%package examples
Summary:	Example programs for Python pyRXP module
Summary(pl.UTF-8):	Programy przykładowe do modułu Pythona pyRXP
Group:		Development/Languages/Python
Requires:	%{name} = %{version}-%{release}

%description examples
This package contains example programs for Python pyRXP module.

%description examples -l pl.UTF-8
Pakiet zawierający programy przykładowe dla modułu Pythona pyRXP.

%prep
%setup -q -n pyRXP-%{version}-%{_snap}

%build
cd pyRXP
%py_build

cp -a %{SOURCE1} docs

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{py_sitedir},%{_examplesdir}/%{name}-%{version}}

cd pyRXP
%py_install

cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc pyRXP/README
%{py_sitedir}/pyRXP-%{version}-py*.egg-info
%attr(755,root,root) %{py_sitedir}/*.so

%files doc
%defattr(644,root,root,755)
%doc pyRXP/docs/PyRXP_Documentation.pdf

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
