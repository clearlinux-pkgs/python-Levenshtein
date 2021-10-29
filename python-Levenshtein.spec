#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-Levenshtein
Version  : 0.12.2
Release  : 39
URL      : https://files.pythonhosted.org/packages/2a/dc/97f2b63ef0fa1fd78dcb7195aca577804f6b2b51e712516cc0e902a9a201/python-Levenshtein-0.12.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/2a/dc/97f2b63ef0fa1fd78dcb7195aca577804f6b2b51e712516cc0e902a9a201/python-Levenshtein-0.12.2.tar.gz
Summary  : Python extension for computing string edit distances and similarities.
Group    : Development/Tools
License  : GPL-2.0
Requires: python-Levenshtein-license = %{version}-%{release}
Requires: python-Levenshtein-python = %{version}-%{release}
Requires: python-Levenshtein-python3 = %{version}-%{release}
Requires: setuptools
BuildRequires : buildreq-distutils3
BuildRequires : python3-dev
BuildRequires : setuptools

%description
Maintainer wanted
        -----------------
        
        |MaintainerWanted|_

%package license
Summary: license components for the python-Levenshtein package.
Group: Default

%description license
license components for the python-Levenshtein package.


%package python
Summary: python components for the python-Levenshtein package.
Group: Default
Requires: python-Levenshtein-python3 = %{version}-%{release}
Provides: python-levenshtein-python

%description python
python components for the python-Levenshtein package.


%package python3
Summary: python3 components for the python-Levenshtein package.
Group: Default
Requires: python3-core
Provides: pypi(levenshtein)
Requires: pypi(setuptools)

%description python3
python3 components for the python-Levenshtein package.


%prep
%setup -q -n python-Levenshtein-0.12.2
cd %{_builddir}/python-Levenshtein-0.12.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1612199987
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/python-Levenshtein
cp %{_builddir}/python-Levenshtein-0.12.2/COPYING %{buildroot}/usr/share/package-licenses/python-Levenshtein/07102fa3ba93fed83e4cab3681f311908c1a7c93
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/python-Levenshtein/07102fa3ba93fed83e4cab3681f311908c1a7c93

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
