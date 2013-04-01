%define tarname Cython

Summary:	Language for writing C extensions to Python
Name:		python-cython
Version:	0.18
Release:	1
Source0:	http://www.cython.org/release/%{tarname}-%{version}.tar.gz
License:	Apache License
Group:		Development/Python
Url:		http://www.cython.org
BuildRequires:	python-devel
BuildRequires:	dos2unix

%description
Cython is a language that facilitates the writing of C extensions for
the Python language. It is based on Pyrex, but provides more cutting
edge functionality and optimizations.


%package -n python3-cython
Summary:    Language for writing C extensions to Python
Group:      Development/Python

BuildRequires:  python3-devel

%description -n python3-cython
Cython is a language that facilitates the writing of C extensions for
the Python language. It is based on Pyrex, but provides more cutting
edge functionality and optimizations.

%prep
%setup -q -n %{tarname}-%{version}


%build 
pushd python2
%{__python} setup.py build
popd
pushd python3
%{__python3} setup.py build
popd

%install

pushd python3
PYTHONDONTWRITEBYTECODE= %__python3 setup.py install --root %{buildroot}
mv %{buildroot}/usr/bin/cython %{buildroot}/usr/bin/cython3
mv %{buildroot}/usr/bin/cygdb %{buildroot}/usr/bin/cygdb3
popd

pushd python2
find -name .*DS_Store* | xargs rm -rf

PYTHONDONTWRITEBYTECODE= %__python setup.py install --root %{buildroot}
pushd Tools
dos2unix cython-mode.el
%__install -m 755 -d %{buildroot}%{_sysconfdir}/emacs/site-start.d
%__install -m 644 *.el* %{buildroot}%{_sysconfdir}/emacs/site-start.d
popd
popd

#%%check
#PYTHONPATH=`pwd`/../build/lib make test clean

%files 
%{_sysconfdir}/emacs/site-start.d/*.el*
%_bindir/cython
%_bindir/cygdb
%py_platsitedir/Cython*
%py_platsitedir/cython*
%py_platsitedir/pyximport*

%files -n python3-cython
%_bindir/cython3
%_bindir/cygdb3
%py3_platsitedir/__pycache__/*
%py3_platsitedir/Cython*
%py3_platsitedir/cython*
%py3_platsitedir/pyximport*


%changelog
* Sun Sep 02 2012 Lev Givon <lev@mandriva.org> 0.17-1
+ Revision: 816174
- Update to 0.17.

* Sun Apr 22 2012 Lev Givon <lev@mandriva.org> 0.16-1
+ Revision: 792653
- Update to 0.16.

* Tue Sep 20 2011 Lev Givon <lev@mandriva.org> 0.15.1-1
+ Revision: 700563
- Update to 0.15.1.

* Sun Aug 07 2011 Lev Givon <lev@mandriva.org> 0.15-1
+ Revision: 693551
- Update to 0.15.

* Thu May 05 2011 Funda Wang <fwang@mandriva.org> 0.14.1-2
+ Revision: 669119
- disable emacs compile

  + Oden Eriksson <oeriksson@mandriva.com>
    - mass rebuild

* Fri Feb 04 2011 Lev Givon <lev@mandriva.org> 0.14.1-1
+ Revision: 635836
- Update to 0.14.1.

* Tue Dec 14 2010 Lev Givon <lev@mandriva.org> 0.14-1mdv2011.0
+ Revision: 621815
- Update to 0.14.

* Sat Oct 30 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.13-2mdv2011.0
+ Revision: 590646
- rebuild for python-2.7
- drop obsolete %%py_requires macro and add BR python-devel
- disable checks for now as they fail (the numpy ones)

* Wed Aug 25 2010 Lev Givon <lev@mandriva.org> 0.13-1mdv2011.0
+ Revision: 573270
- Update to 0.13.

* Tue Feb 02 2010 Lev Givon <lev@mandriva.org> 0.12.1-1mdv2010.1
+ Revision: 499585
- Update to 0.12.1.

* Mon Nov 23 2009 Lev Givon <lev@mandriva.org> 0.12-1mdv2010.1
+ Revision: 469387
- Update to 0.12.

* Sun Sep 27 2009 Lev Givon <lev@mandriva.org> 0.11.3-1mdv2010.0
+ Revision: 449880
- Update to 0.11.3.

* Wed May 20 2009 Lev Givon <lev@mandriva.org> 0.11.2-1mdv2010.0
+ Revision: 378065
- Update to 0.11.2.

* Sun May 03 2009 Lev Givon <lev@mandriva.org> 0.11.1-1mdv2010.0
+ Revision: 371101
- Update to 0.11.1.

* Sun Mar 15 2009 Lev Givon <lev@mandriva.org> 0.11-1mdv2009.1
+ Revision: 355431
- Update to 0.11.

* Sun Dec 28 2008 Funda Wang <fwang@mandriva.org> 0.10.3-2mdv2009.1
+ Revision: 320161
- rebuild for new python

* Wed Dec 17 2008 Lev Givon <lev@mandriva.org> 0.10.3-1mdv2009.1
+ Revision: 315162
- Update to 0.10.3.

* Wed Nov 26 2008 Lev Givon <lev@mandriva.org> 0.10.2-1mdv2009.1
+ Revision: 307043
- Update to 0.10.2.

* Sun Nov 09 2008 Lev Givon <lev@mandriva.org> 0.10-1mdv2009.1
+ Revision: 301257
- Update to 0.10.

* Tue Sep 23 2008 Lev Givon <lev@mandriva.org> 0.9.8.1.1-2mdv2009.0
+ Revision: 287546
- Correct license.

* Wed Aug 20 2008 Lev Givon <lev@mandriva.org> 0.9.8.1.1-1mdv2009.0
+ Revision: 274335
- Update to 0.9.8.1.1.

* Tue Aug 19 2008 Lev Givon <lev@mandriva.org> 0.9.8.1-1mdv2009.0
+ Revision: 273536
- Update to 0.9.8.1.

* Sun Aug 03 2008 Lev Givon <lev@mandriva.org> 0.9.8-2mdv2009.0
+ Revision: 262540
- Install emacs mode.

* Fri Jun 13 2008 Lev Givon <lev@mandriva.org> 0.9.8-1mdv2009.0
+ Revision: 218786
- Update to 0.9.8.

* Wed May 21 2008 Lev Givon <lev@mandriva.org> 0.9.6.14-2mdv2009.0
+ Revision: 209885
- Make package noarch.

* Fri May 02 2008 Lev Givon <lev@mandriva.org> 0.9.6.14-1mdv2009.0
+ Revision: 200101
- Update to 0.9.6.14.

* Sun Apr 13 2008 Lev Givon <lev@mandriva.org> 0.9.6.13.1-1mdv2009.0
+ Revision: 192662
- Update to 0.9.6.13.1.

* Fri Mar 07 2008 Lev Givon <lev@mandriva.org> 0.9.6.12-1mdv2008.1
+ Revision: 181397
- import python-cython


* Wed Feb 13 2008 Lev Givon <lev@mandriva.org> 0.9.6.12-1mdv2008.0
- Update to 0.9.6.12.

* Mon Jan 07 2008 Lev Givon <lev@mandriva.org> 0.9.6.10b-1mdv2008.0
- Package for Mandriva.
