#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-Levenshtein
Version  : 0.12.0
Release  : 2
URL      : https://pypi.python.org/packages/42/a9/d1785c85ebf9b7dfacd08938dd028209c34a0ea3b1bcdb895208bd40a67d/python-Levenshtein-0.12.0.tar.gz
Source0  : https://pypi.python.org/packages/42/a9/d1785c85ebf9b7dfacd08938dd028209c34a0ea3b1bcdb895208bd40a67d/python-Levenshtein-0.12.0.tar.gz
Summary  : Python extension for computing string edit distances and similarities.
Group    : Development/Tools
License  : GPL-2.0
Requires: python-Levenshtein-python
Requires: setuptools
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
.. contents ::
Introduction
------------
The Levenshtein Python C extension module contains functions for fast
computation of

%package python
Summary: python components for the python-Levenshtein package.
Group: Default
Provides: python-levenshtein-python

%description python
python components for the python-Levenshtein package.


%prep
%setup -q -n python-Levenshtein-0.12.0

%build
export LANG=C
export SOURCE_DATE_EPOCH=1490546197
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1490546197
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python2*/*
/usr/lib/python3*/*
