%global project tempest

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

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
BuildRequires:  git
BuildRequires:  python-sphinx
BuildRequires:  python-d2to1
BuildRequires:  python-setuptools
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
Requires:       python-jsonschema
Requires:       python-junitxml
Requires:       python-keyring
Requires:       python-keystoneclient
Requires:       python-lxml
Requires:       python-netaddr >= 0.7.12
Requires:       python-neutronclient
Requires:       python-nose
Requires:       python-novaclient
Requires:       python-oslo-concurrency >= 2.3.0
Requires:       python-oslo-config >= 2:2.3.0
Requires:       python-oslo-i18n >= 1.5.0
Requires:       python-oslo-log >= 1.8.0
Requires:       python-oslo-serialization >= 1.4.0
Requires:       python-oslo-utils >= 2.0.0
Requires:       python-paramiko
Requires:       python-pbr
Requires:       python-prettytable
Requires:       python-saharaclient
Requires:       python-six >= 1.9.0
Requires:       python-swiftclient
Requires:       python-stevedore
Requires:       python-testrepository
Requires:       python-testresources
Requires:       python-testscenarios
Requires:       python-testtools
Requires:       python2-os-testr >= 0.4.1
Requires:       PyYAML
Requires:       which
Requires:       subunit-filters
Requires:       python-aodh-tests
Requires:       python-ceilometer-tests
Requires:       python-cinder-tests
Requires:       python-glance-tests
Requires:       python-gnocchi-tests
Requires:       python-heat-tests
Requires:       python-ironic-tests
Requires:       python-keystone-tests
Requires:       python-mistral-tests
Requires:       python-neutron-tests
Requires:       python-neutron-fwaas-tests
Requires:       python-neutron-lbaas-tests
Requires:       python-neutron-vpnaas-tests
Requires:       python-nova-tests
Requires:       python-sahara-tests
Requires:       python-swift-tests
Requires:       python-trove-tests

Obsoletes:      openstack-tempest-liberty
Obsoletes:      openstack-tempest-kilo
Obsoletes:      openstack-tempest-juno < 20150319
Obsoletes:      openstack-tempest-icehouse < 20150319

%description
This is a set of integration tests to be run against a live OpenStack cluster.
Tempest has batteries of tests for OpenStack API validation, Scenarios, and
other specific tests useful in validating an OpenStack deployment.


%prep
%autosetup -n tempest-%{upstream_version} -S git
# remove shebangs and fix permissions
RPMLINT_OFFENDERS="tempest/cmd/account_generator.py \
tempest/cmd/cleanup.py \
tempest/cmd/cleanup_service.py \
tempest/cmd/javelin.py \
tempest/cmd/run_stress.py \
tempest/cmd/verify_tempest_config.py \
tempest/common/api_discovery.py \
tempest/stress/cleanup.py \
tempest/tests/cmd/test_javelin.py"
sed -i '1{/^#!/d}' $RPMLINT_OFFENDERS
chmod u=rw,go=r $RPMLINT_OFFENDERS

%install
mkdir -p %{buildroot}%{_datarootdir}/%{name}-%{upstream_version}
cp --preserve=mode -r . %{buildroot}%{_datarootdir}/%{name}-%{upstream_version}
rm -rf %{buildroot}%{_datarootdir}/%{name}-%{upstream_version}/.git*
rm -rf %{buildroot}%{_datarootdir}/%{name}-%{upstream_version}/build
rm -f  %{buildroot}%{_datarootdir}/%{name}-%{upstream_version}/doc/source/_static/.keep
%{__python} setup.py install --skip-build --root %{buildroot}
mkdir -p %{buildroot}/etc/tempest
mv %{buildroot}/usr/etc/tempest/* %{buildroot}/etc/tempest

%build
%{__python} setup.py build

%files
%license LICENSE
%defattr(-,root,root)
%{_datarootdir}/%{name}-%{upstream_version}
%exclude %{_datarootdir}/%{name}-%{upstream_version}/.mailmap
%exclude %{_datarootdir}/%{name}-%{upstream_version}/.coveragerc
%{_bindir}/tempest
%{_bindir}/check-uuid
%{_bindir}/javelin2
%{_bindir}/run-tempest-stress
%{_bindir}/skip-tracker
%{_bindir}/tempest-account-generator
%{_bindir}/tempest-cleanup
%{_bindir}/verify-tempest-config
%{python2_sitelib}/%{project}
%{python2_sitelib}/%{project}*.egg-info
%{_sysconfdir}/%{project}/*sample
%{_sysconfdir}/%{project}/*yaml
%{_sysconfdir}/%{project}/*.conf

%changelog
