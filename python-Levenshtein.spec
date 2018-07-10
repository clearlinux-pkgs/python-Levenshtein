#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-Levenshtein
Version  : 0.12.0
Release  : 17
URL      : http://pypi.debian.net/python-Levenshtein/python-Levenshtein-0.12.0.tar.gz
Source0  : http://pypi.debian.net/python-Levenshtein/python-Levenshtein-0.12.0.tar.gz
Summary  : Python extension for computing string edit distances and similarities.
Group    : Development/Tools
License  : GPL-2.0
Requires: python-Levenshtein-python3
Requires: python-Levenshtein-python
Requires: setuptools
BuildRequires : pbr
BuildRequires : pip

BuildRequires : python3-dev
BuildRequires : setuptools

%description
Introduction
        ------------
        
        The Levenshtein Python C extension module contains functions for fast
        computation of
        
        * Levenshtein (edit) distance, and edit operations
        
        * string similarity
        
        * approximate median strings, and generally string averaging
        
        * string sequence and set similarity
        
        It supports both normal and Unicode strings.
        
        Python 2.2 or newer is required; Python 3 is supported.
        
        StringMatcher.py is an example SequenceMatcher-like class built on the top of
        Levenshtein.  It misses some SequenceMatcher's functionality, and has some
        extra OTOH.
        
        Levenshtein.c can be used as a pure C library, too.  You only have to define
        NO_PYTHON preprocessor symbol (-DNO_PYTHON) when compiling it.  The
        functionality is similar to that of the Python extension.  No separate docs

%package python
Summary: python components for the python-Levenshtein package.
Group: Default
Requires: python-Levenshtein-python3
Provides: python-levenshtein-python

%description python
python components for the python-Levenshtein package.


%package python3
Summary: python3 components for the python-Levenshtein package.
Group: Default
Requires: python3-core

%description python3
python3 components for the python-Levenshtein package.


%prep
%setup -q -n python-Levenshtein-0.12.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1526149302
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
