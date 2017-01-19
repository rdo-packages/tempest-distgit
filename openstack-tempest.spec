%global project tempest

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:           openstack-%{project}
Epoch:          1
Version:        XXX
Release:        XXX
Summary:        OpenStack Integration Test Suite (Tempest)
License:        ASL 2.0
Url:            https://launchpad.net/tempest
Source0:        http://tarballs.openstack.org/tempest/tempest-%{upstream_version}.tar.gz
BuildArch:      noarch

BuildRequires:  git
BuildRequires:  python-oslo-config
BuildRequires:  python-pbr
BuildRequires:  python-setuptools
BuildRequires:  python2-devel

Requires:       python-tempest = %{epoch}:%{version}-%{release}

# FIXME Once python-tempestconf is available
# Requires:     python-tempestconf



# FIXME remove openstack-tempest-liberty obsoletes by Pike release.
Obsoletes:      openstack-tempest-liberty
Obsoletes:      openstack-tempest < 1:14.0.0

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
Requires:      python-oslo-serialization
Requires:      python-oslo-utils
Requires:      python-os-testr
Requires:      python-paramiko
Requires:      python-pbr
Requires:      python-prettytable
Requires:      python-six
Requires:      python-stevedore
Requires:      python-testrepository
Requires:      python-testtools
Requires:      python-urllib3
Requires:      PyYAML
Requires:      python-subunit

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
BuildRequires:  python-oslo-log
BuildRequires:  python-jsonschema
BuildRequires:  python-urllib3
BuildRequires:  PyYAML
BuildRequires:  python-oslo-concurrency
BuildRequires:  python-paramiko
BuildRequires:  python-cliff
BuildRequires:  python-pep8
BuildRequires:  python-os-testr

Requires:       python-coverage
Requires:       python-mock
Requires:       python-oslotest

%description -n python-tempest-tests
This is a set of integration tests to be run against a live OpenStack cluster.
Tempest has batteries of tests for OpenStack API validation, Scenarios, and
other specific tests useful in validating an OpenStack deployment.

This package contains tests for the tempest python library.

%if 0%{?repo_bootstrap} == 0
%package -n    %{name}-all
Summary:       All OpenStack Tempest Plugins

Requires:      %{name} = %{epoch}:%{version}-%{release}

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

%description -n %{name}-all
This is a set of integration tests to be run against a live OpenStack cluster.
Tempest has batteries of tests for OpenStack API validation, Scenarios, and
other specific tests useful in validating an OpenStack deployment.

This package contains all the tempest plugins.
%endif

%prep
%autosetup -n tempest-%{upstream_version} -S git
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
%{__python2} setup.py install --skip-build --root %{buildroot}

# Generate tempest config
mkdir -p %{buildroot}%{_sysconfdir}/%{project}/
oslo-config-generator --config-file tempest/cmd/config-generator.tempest.conf \
    --output-file %{buildroot}%{_sysconfdir}/%{project}/tempest.conf

mkdir -p %{buildroot}/etc/tempest
mv %{buildroot}/usr/etc/tempest/* %{buildroot}/etc/tempest

%check
export OS_TEST_PATH='./tempest/tests'
export PATH=$PATH:$RPM_BUILD_ROOT/usr/bin
export PYTHONPATH=$PWD
%{__python2} setup.py testr

%files
%license LICENSE
%doc README.rst
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
