%global commit ab030aba43cdd2412411f184763e2d7c905db31a
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global alphatag .%{shortcommit}git
%global project tempest

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%{?dlrn: %global tarsources %{project}-%{upstream_version}}
%{!?dlrn: %global tarsources %{project}-%{commit}}

Name:           openstack-%{project}
Epoch:          1
Version:        13.0.0
Release:        12%{alphatag}%{?dist}
Summary:        OpenStack Integration Test Suite (Tempest)
License:        ASL 2.0
# FIXME move to Upstream tempest
Url:            https://github.com/redhat-openstack/tempest
Source0:        https://github.com/redhat-openstack/tempest/archive/%{commit}.tar.gz#/%{project}-%{commit}.tar.gz
BuildArch:      noarch

BuildRequires:  fdupes
BuildRequires:  git
BuildRequires:  python-d2to1
BuildRequires:  python-oslo-config
BuildRequires:  python-pbr
BuildRequires:  python-setuptools
BuildRequires:  python2-devel

Requires:       python-tempest = %{epoch}:%{version}-%{release}

Requires:       python
Requires:       python-anyjson
Requires:       python-boto
Requires:       python-iso8601
Requires:       python-junitxml
Requires:       python-keyring
Requires:       python-lxml
Requires:       python-nose
Requires:       python-testresources
Requires:       subunit-filters
Requires:       which

Obsoletes:      openstack-tempest-icehouse < 20150319
Obsoletes:      openstack-tempest-juno < 20150319
Obsoletes:      openstack-tempest-liberty
Obsoletes:      openstack-tempest-kilo

%description
This is a set of integration tests to be run against a live OpenStack cluster.
Tempest has batteries of tests for OpenStack API validation, Scenarios, and
other specific tests useful in validating an OpenStack deployment.

%package -n    python-tempest
Summary:       Tempest Python library

Requires:      python-cliff
Requires:      python-debtcollector
Requires:      python-fixtures
Requires:      python-jsonschema
Requires:      python-netaddr
Requires:      python-oslo-concurrency
Requires:      python-oslo-config
Requires:      python-oslo-log
Requires:      python-oslo-i18n
Requires:      python-oslo-serialization
Requires:      python-oslo-utils
Requires:      python-os-testr
Requires:      python-paramiko
Requires:      python-pbr
Requires:      python-prettytable
Requires:      python-six
Requires:      python-stevedore
Requires:      python-testrepository
Requires:      python-testscenarios
Requires:      python-testtools
Requires:      python-urllib3
Requires:      PyYAML

%description -n python-tempest
This is a set of integration tests to be run against a live OpenStack cluster.
Tempest has batteries of tests for OpenStack API validation, Scenarios, and
other specific tests useful in validating an OpenStack deployment.

This package contains the tempest python library.

%package -n     python-tempest-tests
Summary:        Python Tempest tests
Requires:       python-tempest = %{epoch}:%{version}-%{release}

BuildRequires:  python-coverage
BuildRequires:  python-mock
BuildRequires:  python-oslotest
BuildRequires:  python-subunit

Requires:       python-coverage
Requires:       python-mock
Requires:       python-oslotest
Requires:       python-subunit

%description -n python-tempest-tests
This is a set of integration tests to be run against a live OpenStack cluster.
Tempest has batteries of tests for OpenStack API validation, Scenarios, and
other specific tests useful in validating an OpenStack deployment.

This package contains tests for the tempest python library.

%if 0%{?repo_bootstrap} == 0
%package -n    %{name}-all
Summary:       All OpenStack Tempest Plugins

Requires:      %{name} = %{epoch}:%{version}-%{release}

<<<<<<< HEAD   (3c53ce Fix config_tempest failing due to v3)
Requires:       python-aodh-tests
Requires:       python-ceilometer-tests
Requires:       python-cinder-tests
Requires:       python-designate-tests-tempest
Requires:       python-glance-tests
Requires:       python-gnocchi-tests
Requires:       python-heat-tests
Requires:       python-horizon-tests-tempest
Requires:       python-ironic-tests
Requires:       python-keystone-tests
Requires:       python-mistral-tests
Requires:       python-neutron-tests
Requires:       python-neutron-fwaas-tests
Requires:       python-neutron-lbaas-tests
Requires:       python-neutron-vpnaas-tests
Requires:       python-nova-tests
Requires:       python-sahara-tests-tempest
Requires:       python-swift-tests
Requires:       python-trove-tests
Requires:       python-zaqar-tests
Requires:       python-watcher-tests-tempest
Requires:       python-magnum-tests
Requires:       python-murano-tests
Requires:       python-manila-tests
Requires:       python-ironic-inspector-tests
=======
Requires:       python3-cinder-tests-tempest
Requires:       python3-designate-tests-tempest
Requires:       python3-heat-tests-tempest
Requires:       python3-ironic-tests-tempest
Requires:       python3-keystone-tests-tempest
Requires:       python3-neutron-tests-tempest
Requires:       python3-manila-tests-tempest
Requires:       python3-telemetry-tests-tempest
Requires:       python3-octavia-tests-tempest
Requires:       python3-networking-l2gw-tests-tempest
Requires:       python3-patrole-tests-tempest
Requires:       python3-novajoin-tests-tempest
Requires:       python3-barbican-tests-tempest

%if 0%{?rhosp} == 0
Requires:       python3-kuryr-tests-tempest
Requires:       python3-magnum-tests-tempest
Requires:       python3-mistral-tests-tempest
Requires:       python3-murano-tests-tempest
Requires:       python3-sahara-tests-tempest
Requires:       python3-trove-tests-tempest
Requires:       python3-vitrage-tests-tempest
Requires:       python3-watcher-tests-tempest
Requires:       python3-zaqar-tests-tempest
%endif
>>>>>>> CHANGE (d73655 move kuryr-tests-tempest to not rhosp block)

%description -n %{name}-all
This is a set of integration tests to be run against a live OpenStack cluster.
Tempest has batteries of tests for OpenStack API validation, Scenarios, and
other specific tests useful in validating an OpenStack deployment.

This package contains all the tempest plugins.
%endif

%prep
%autosetup -n %{tarsources} -S git
# have dependencies being handled by rpms, rather than requirement files
rm -rf {test-,}requirements.txt

# remove shebangs and fix permissions
RPMLINT_OFFENDERS="tempest/cmd/list_plugins.py \
tempest/cmd/cleanup.py \
tempest/cmd/cleanup_service.py \
tempest/cmd/verify_tempest_config.py \
tempest/cmd/account_generator.py \
tempest/lib/cmd/skip_tracker.py \
tempest/lib/cmd/check_uuid.py"
sed -i '1{/^#!/d}' $RPMLINT_OFFENDERS
chmod u=rw,go=r $RPMLINT_OFFENDERS

%build
%{__python2} setup.py build

%install
mkdir -p %{buildroot}%{_datarootdir}/%{name}-%{upstream_version}
cp -pr . %{buildroot}%{_datarootdir}/%{name}-%{upstream_version}
# Remove unnecessary files
rm -rf %{buildroot}%{_datarootdir}/%{name}-%{upstream_version}/.git*
rm -rf %{buildroot}%{_datarootdir}/%{name}-%{upstream_version}/build
rm -f  %{buildroot}%{_datarootdir}/%{name}-%{upstream_version}/doc/source/_static/.keep
rm -f  %{buildroot}%{_datarootdir}/%{name}-%{upstream_version}/.mailmap
rm -f  %{buildroot}%{_datarootdir}/%{name}-%{upstream_version}/.coveragerc

%{__python2} setup.py install --skip-build --root %{buildroot}

# Generate tempest config
mkdir -p %{buildroot}%{_sysconfdir}/%{project}/
oslo-config-generator --config-file tempest/cmd/config-generator.tempest.conf \
    --output-file %{buildroot}%{_sysconfdir}/%{project}/tempest.conf

mkdir -p %{buildroot}/etc/tempest
mv %{buildroot}/usr/etc/tempest/* %{buildroot}/etc/tempest

%files
%license LICENSE
%doc README.rst
%{_datarootdir}/%{name}-%{upstream_version}
%{_bindir}/tempest
%{_bindir}/check-uuid
%{_bindir}/skip-tracker
%{_bindir}/subunit-describe-calls
%{_bindir}/tempest-account-generator
%{_bindir}/verify-tempest-config
%{_sysconfdir}/%{project}/*sample
%{_sysconfdir}/%{project}/*yaml
%config(noreplace) %{_sysconfdir}/%{project}/*.conf

%files -n python-tempest
%license LICENSE
%{python2_sitelib}/%{project}
%{python2_sitelib}/%{project}*.egg-info
%exclude %{python2_sitelib}/tempest/tests

%files -n python-tempest-tests
%license LICENSE
%{python2_sitelib}/tempest/tests

%if 0%{?repo_bootstrap} == 0
%files -n %{name}-all
%license LICENSE
%endif

%changelog
* Thu Jun 15 2017 Martin Kopec <mkopec AT redhat.com> 1:13.0.0-12-ab030abagit
- Fix config_tempest failing due to v3
- Resolves rhbz#1460925
- Update to post 13.0.0 (ab030aba43cdd2412411f184763e2d7c905db31a)

* Fri May 26 2017 Chandan Kumar <chkumar AT redhat.com> 1:13.0.0-11-b13ba4cfgit
- Fixed waiters.py: raise BackupException defined in tempest/lib
- Resolves rhbz#1455928
- Update to post 13.0.0 (b13ba4cfd277c67097db4cc431ecd04d6ed49411)

* Thu Apr 27 2017 Chandan Kumar <chkumar AT redhat.com> 1:13.0.0-10-79cf31a3git
- Added remove option in config_tempest.py
- Resolves rhbz#1443397
- Update to post 13.0.0 (79cf31a3034f227c2ddfa3426a45615cd8ed6f63)

* Thu Mar 30 2017 Chandan Kumar <chkumar AT redhat.com> 1:13.0.0-9-e6587796git
- Fixed proper initialization of configuration values from tempest.conf for some plugins
- Resolves rhbz#1434849
- Update to post 13.0.0 (72c0cf156358858984186fee53b2bd2ae6587796)

* Mon Feb 20 2017 Chandan Kumar <chkumar AT redhat.com> 1:13.0.0-8.35fce174git
- Remove the Stress Framework
- Update to post 13.0.0 (35fce1741bab97398a586c47df22ea493074c49e)

* Fri Jan 27 2017 Chandan Kumar <chkumar AT redhat.com> 1:13.0.0-7.1e455fcgit
- Update to post 13.0.0 (fa4dc09118621a9a0f95988c88d998c961e455fc)
- Added manila service in tools/config_tempest.py

* Thu Nov 24 2016 Chandan Kumar <chkumar AT redhat.com> 1:13.0.0-6.a8d012a1git
- Update to post 13.0.0 (a8d012a1807916d065657cec2a3e20d636741b7f)
- Remove unused arguments from _error_checker() from negative_rest_client
- Install a package only if available backports

* Fri Nov 18 2016 Chandan Kumar <chkumar AT redhat.com> 1:13.0.0-5.d72c4b2agit
- Update to post 13.0.0 (d72c4b2ad0aceca4ae5a3bbb47c7d34fcfe49f9b)

* Fri Nov 11 2016 Chandan Kumar <chkumar AT redhat.com> 1:13.0.0-4.6425a9bagit
- Update to post 13.0.0 (6425a9bac6082278a26dcd4a067e270bba80b58d)

* Fri Nov 04 2016 Chandan Kumar <chkumar AT redhat.com> 1:13.0.0-3.296cca79git
- Update to post 13.0.0 (296cca79678463dd90ca2694245bb7b89f8405d8)

* Wed Oct 19 2016 Alfredo Moralejo <amoralej@redhat.com> 1:13.0.0-2.bafe630git
- Update to post 13.0.0  (bafe630508a1a85b649a7d0134bd8112afd0de84)

* Tue Oct 11 2016 Chandan Kumar <chkumar AT redhat.com> 1:13.0.0-1.0363596git
- Update to 13.0.0

* Fri Sep 23 2016 Alan Pevec <apevec AT redhat.com> 1:12.2.0-2.0f8baaegit
- Update to 12.2.0 redhat-openstack/tempest snapshot 0f8baae
