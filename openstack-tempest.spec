%global project tempest
%global upstream_release liberty

Name:           openstack-%{project}
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
Requires:       python-cliff
Requires:       python-fixtures
Requires:       python-glanceclient
Requires:       python-heatclient
Requires:       python-ironicclient
Requires:       python-iso8601
Requires:       python-junitxml
Requires:       python-keyring
Requires:       python-keystoneclient
Requires:       python-lxml
Requires:       python-netaddr >= 0.7.12
Requires:       python-neutronclient
Requires:       python-nose
Requires:       python-novaclient
Requires:       python-oslo-concurrency >= 2.3.0
Requires:       python-oslo-config >= 2.3.0
Requires:       python-oslo-i18n >= 1.5.0
Requires:       python-oslo-log >= 1.8.0
Requires:       python-oslo-serialization >= 1.4.0
Requires:       python-oslo-utils >= 2.0.0
Requires:       python-pbr
Requires:       python-saharaclient
Requires:       python-six >= 1.9.0
Requires:       python-swiftclient
Requires:       python-stevedore
Requires:       python-testrepository
Requires:       python-testresources
Requires:       python-testscenarios
Requires:       python-testtools
Requires:       PyYAML
Requires:       which
Requires:       python-tempest-lib >= 0.6.1
Requires:       subunit-filters

Provides:       openstack-tempest-liberty
Obsoletes:      openstack-tempest-kilo
Obsoletes:      openstack-tempest-juno < 20150319
Obsoletes:      openstack-tempest-icehouse < 20150319

%description
This is a set of integration tests to be run against a live OpenStack cluster.
Tempest has batteries of tests for OpenStack API validation, Scenarios, and
other specific tests useful in validating an OpenStack deployment.


%prep
%setup -q -n tempest-%{upstream_version}
# remove shebangs and fix permissions
RPMLINT_OFFENDERS="tempest/cmd/cleanup_service.py tempest/stress/cleanup.py"
sed -i '1{/^#!/d}' $RPMLINT_OFFENDERS
chmod u=rw,go=r $RPMLINT_OFFENDERS

%install
mkdir -p %{buildroot}%{_datarootdir}/%{name}-%{upstream_release}
cp --preserve=mode -r . %{buildroot}%{_datarootdir}/%{name}-%{upstream_release}
%{__python} setup.py install --skip-build --root %{buildroot}
mkdir -p %{buildroot}/etc/tempest
mv %{buildroot}/usr/etc/tempest/* %{buildroot}/etc/tempest

%build
%{__python} setup.py build

%files
%license LICENSE
%defattr(-,root,root)
%{_datarootdir}/%{name}-%{upstream_release}
%exclude %{_datarootdir}/%{name}-%{upstream_release}/.mailmap
%exclude %{_datarootdir}/%{name}-%{upstream_release}/.coveragerc
%{_bindir}/tempest
%{_bindir}/javelin2
%{_bindir}/run-tempest-stress
%{_bindir}/tempest-account-generator
%{_bindir}/tempest-cleanup
%{_bindir}/verify-tempest-config
%{python2_sitelib}/%{project}
%{python2_sitelib}/%{project}*.egg-info
%{_sysconfdir}/%{project}/*sample
%{_sysconfdir}/%{project}/*yaml
%{_sysconfdir}/%{project}/*.conf

%changelog
