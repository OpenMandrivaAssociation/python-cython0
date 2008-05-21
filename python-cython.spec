%define tarname Cython
%define name 	python-cython
%define version 0.9.6.14
%define release %mkrel 2

Summary: Language for writing C extensions to Python
Name: 	 %{name}
Version: %{version}
Release: %{release}
Source0: %{tarname}-%{version}.tar.lzma
License: Python
Group: 	 Development/Python
Url: 	 http://www.cython.org
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires: python-devel
BuildRequires: python-numeric-devel
BuildArch: noarch

%description
Cython is a language that facilitates the writing of C extensions for
the Python language. It is based on Pyrex, but provides more cutting
edge functionality and optimizations.

%prep
%setup -q -n %{tarname}-%{version}

%install
%__rm -rf %{buildroot}
%__python setup.py install --root=%{buildroot} --record=INSTALLED_FILES.txt

# Uncomment when all checks work properly:
#%check
#cd Demos
#PYTHONPATH=`pwd`/../build/lib make test clean

%clean
%__rm -rf %{buildroot}

%files -f INSTALLED_FILES.txt
%defattr(-,root,root)
%doc *.txt Demos Doc

