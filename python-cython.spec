%define tarname Cython
%define name 	python-cython
%define version 0.10.3
%define release %mkrel 2

Summary:	Language for writing C extensions to Python
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{tarname}-%{version}.tar.lzma
License:	Apache License
Group:		Development/Python
Url:		http://www.cython.org
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:	dos2unix, emacs
%py_requires -d

%description
Cython is a language that facilitates the writing of C extensions for
the Python language. It is based on Pyrex, but provides more cutting
edge functionality and optimizations.

%prep
%setup -q -n %{tarname}-%{version}

%install
%__rm -rf %{buildroot}
find -name .*DS_Store* | xargs rm -rf

%__python setup.py install --root=%{buildroot} --record=FILELIST
pushd Tools
dos2unix cython-mode.el
emacs -batch -f batch-byte-compile cython-mode.el
%__install -m 755 -d %{buildroot}%{_sysconfdir}/emacs/site-start.d
%__install -m 644 *.el* %{buildroot}%{_sysconfdir}/emacs/site-start.d
popd

# Uncomment when all checks work properly:
#%check
#cd Demos
#PYTHONPATH=`pwd`/../build/lib make test clean

%clean
%__rm -rf %{buildroot}

%files -f FILELIST
%defattr(-,root,root)
%doc *.txt Demos Doc
%{_sysconfdir}/emacs/site-start.d/*.el*
