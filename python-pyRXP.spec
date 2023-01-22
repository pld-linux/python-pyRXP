
#
# todo:
# - use external rxp
# - make documentation from rml file instead of downloading it
#   (need for spec for http://www.reportlab.org/rl_toolkit.html)
#

Summary:	A Python wrapper for the RXP parser
Summary(pl.UTF-8):	Pythonowy interfejs do analizatora XML RXP
Name:		python-pyRXP
Version:	1.16
Release:	1
License:	GPL v2
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pyRXP/
Source0:	https://www.reportlab.com/ftp/pyRXP-%{version}-daily-unix.tar.gz
# Source0-md5:	6c883cc6e9ac32585365dd2ae8867d81
URL:		https://pypi.org/project/pyRXP/
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.5
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
Group:		Documentation
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description doc
This package contains documentation files for Python pyRXP module.

%description doc -l pl.UTF-8
Pakiet zawierający dokumentację dla modułu Pythona pyRXP.

%package examples
Summary:	Example programs for Python pyRXP module
Summary(pl.UTF-8):	Programy przykładowe do modułu Pythona pyRXP
Group:		Development/Languages/Python
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description examples
This package contains example programs for Python pyRXP module.

%description examples -l pl.UTF-8
Pakiet zawierający programy przykładowe dla modułu Pythona pyRXP.

%prep
%setup -q -n pyRXP-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%py_install

cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rst
%attr(755,root,root) %{py_sitedir}/pyRXP.so
%attr(755,root,root) %{py_sitedir}/pyRXPU.so
%{py_sitedir}/pyRXP-%{version}-py*.egg-info

%files doc
%defattr(644,root,root,755)
%doc docs/*.{gif,html}

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
