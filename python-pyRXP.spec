
#
# todo:
# - use external rxp
#

%include	/usr/lib/rpm/macros.python

%define module pyRXP

Summary:	A Python wrapper for the RXP parser 
Summary(pl):	Pythonowy interfejs do parsera XML RXP
Name:		python-%{module}
Version:	0.9
Release:	0.4
License:	GPL v2
Group:		Libraries/Python
Source0:	http://www.reportlab.com/ftp/%{module}-0-9.tgz
# Source0-md5:	7d69870d3884f9e40f111a62525e0d77
URL:		http://www.reportlab.com/xml/pyrxp.html
BuildRequires:	python-devel >= 2.2.1
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pyRXP is a Python wrapper for RXP, a validating namespace-aware
XML parser in C.

%description -l pl
pyRXP to pythonowy interfejs do RXP - kontroluj±cego poprawno¶æ
analizatora XML z obs³ug± przestrzeni nazw napisanego w C.

%prep
%setup -q -c %{module}-%{version}

%build
CFLAGS="%{rpmcflags}"
export CFLAGS
python setup.py build 

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--root=$RPM_BUILD_ROOT --optimize=2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{py_sitedir}/*.so
