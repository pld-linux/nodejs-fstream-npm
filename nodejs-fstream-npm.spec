%define		pkg	fstream-npm
Summary:	An fstream class for creating npm packages
Name:		nodejs-%{pkg}
Version:	0.1.7
Release:	1
License:	MIT
Group:		Development/Libraries
Source0:	http://registry.npmjs.org/PACKAGE_NAME/-/%{pkg}-%{version}.tgz
# Source0-md5:	ee92c5c502f898fe19587e5d3d0ed18e
URL:		https://github.com/isaacs/fstream-npm
BuildRequires:	rpmbuild(macros) >= 1.634
Requires:	nodejs
Requires:	nodejs-fstream-ignore < 0.1.0
Requires:	nodejs-fstream-ignore >= 0.0.0
Requires:	nodejs-inherits < 3
Requires:	nodejs-inherits >= 2
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
cp -p %{pkg}.js package.json $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a example/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%{nodejs_libdir}/%{pkg}
%{_examplesdir}/%{name}-%{version}
