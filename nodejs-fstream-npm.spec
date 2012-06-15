Summary:	An fstream class for creating npm packages
Name:		nodejs-fstream-npm
Version:	0.0.6
Release:	1
License:	MIT
Group:		Development/Libraries
URL:		https://github.com/isaacs/fstream-npm
Source0:	http://registry.npmjs.org/fstream-npm/-/fstream-npm-%{version}.tgz
# Source0-md5:	51ee77f6e92db2e3b2812db2ff20ca77
BuildRequires:	rpmbuild(macros) >= 1.634
Requires:	nodejs
Requires:	nodejs-fstream-ignore
Requires:	nodejs-inherits
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An fstream class for creating npm packages.

%prep
%setup -qc
mv package/* .

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{nodejs_libdir}/fstream-npm
cp -pr fstream-npm.js package.json $RPM_BUILD_ROOT%{nodejs_libdir}/fstream-npm

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a example/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%{nodejs_libdir}/fstream-npm
%{_examplesdir}/%{name}-%{version}
