Summary:	An fstream class for creating npm packages
Name:		nodejs-fstream-npm
Version:	0.1.3
Release:	1
License:	MIT
Group:		Development/Libraries
URL:		https://github.com/isaacs/fstream-npm
Source0:	http://registry.npmjs.org/fstream-npm/-/fstream-npm-%{version}.tgz
# Source0-md5:	2267e408a544355f10c3f00d070a92d3
BuildRequires:	rpmbuild(macros) >= 1.634
Requires:	nodejs
Requires:	nodejs-fstream-ignore >= 0.0.5
Requires:	nodejs-fstream-ignore < 0.1.0
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
