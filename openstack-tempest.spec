Name:           openstack-tempest
Epoch:          1
Version:        XXX
Release:        XXX
Summary:        OpenStack Integration Test Suite (Tempest)
License:        ASL 2.0
Url:            https://github.com/redhat-openstack/tempest
Source0:        https://github.com/redhat-openstack/tempest/archive/master.tar.gz
BuildArch:      noarch

BuildRequires:  fdupes
BuildRequires:  python-sphinx
BuildRequires:  python-d2to1
BuildRequires:  python-distribute
BuildRequires:  python-pbr
BuildRequires:  python2-devel

Requires:       python
Requires:       python-anyjson
Requires:       python-boto
Requires:       python-cinderclient
Requires:       python-fixtures
Requires:       python-glanceclient
Requires:       python-heatclient
Requires:       python-ironicclient
Requires:       python-iso8601
Requires:       python-junitxml
Requires:       python-keyring
Requires:       python-keystoneclient
Requires:       python-lxml
Requires:       python-netaddr
Requires:       python-neutronclient
Requires:       python-nose
Requires:       python-novaclient
Requires:       python-oslo-config
Requires:       python-paramiko
Requires:       python-pbr
Requires:       python-saharaclient
Requires:       python-swiftclient
Requires:       python-testrepository
Requires:       python-testresources
Requires:       python-testscenarios
Requires:       python-testtools
Requires:       which
Requires:       python-tempest-lib >= 0.4.0
Requires:       subunit-filters

Provides:       openstack-tempest-kilo
Obsoletes:      openstack-tempest-juno < 20150319
Obsoletes:      openstack-tempest-icehouse < 20150319

%description
This is a set of integration tests to be run against a live OpenStack cluster.
Tempest has batteries of tests for OpenStack API validation, Scenarios, and
other specific tests useful in validating an OpenStack deployment.


%prep
%setup -q -n tempest-%{upstream_version}
# remove shebangs and fix permissions
find -type f -a \( -name '*.py' -o -name 'py.*' \) \
   -exec sed -i '1{/^#!/d}' {} \; \
   -exec chmod u=rw,go=r {} \;

%install
mkdir -p %{buildroot}%{_datarootdir}/%{name}-%{version}
cp --preserve=mode -r . %{buildroot}%{_datarootdir}/%{name}-%{version}

%build

%files
%doc LICENSE
%defattr(-,root,root)
%{_datarootdir}/%{name}-%{version}
%exclude %{_datarootdir}/%{name}-%{version}/.gitignore
%exclude %{_datarootdir}/%{name}-%{version}/.gitreview
%exclude %{_datarootdir}/%{name}-%{version}/.mailmap
%exclude %{_datarootdir}/%{name}-%{version}/.coveragerc

%changelog
