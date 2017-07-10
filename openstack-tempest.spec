%global project tempest
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%global with_doc 1
%global common_desc \
This is a set of integration tests to be run against a live OpenStack cluster.\
Tempest has batteries of tests for OpenStack API validation, Scenarios, and \
other specific tests useful in validating an OpenStack deployment.

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
BuildRequires:  openstack-macros

Requires:       python-tempest = %{epoch}:%{version}-%{release}

%if 0%{?repo_bootstrap} == 0
Requires:     python-tempestconf
%endif


# FIXME remove openstack-tempest-liberty obsoletes by Pike release.
Obsoletes:      openstack-tempest-liberty

%description
%{common_desc}

%package -n    python-tempest
Summary:       Tempest Python library

Requires:      python-cliff
Requires:      python-debtcollector
Requires:      python-fixtures
Requires:      python-jsonschema
Requires:      python-netaddr
Requires:      python-oslo-concurrency >= 3.8.0
Requires:      python-oslo-config >= 2:3.14.0
Requires:      python-oslo-log >= 3.11.0
Requires:      python-oslo-serialization >= 1.10.0
Requires:      python-oslo-utils >= 3.18.0
Requires:      python-os-testr >= 0.8.0
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
%{common_desc}

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
%{common_desc}

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
Requires:       python-keystone-tests-tempest
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
Requires:       python-panko-tests
Requires:       python-congress-tests
Requires:       python-vitrage-tests
Requires:       python-octavia-tests
Requires:       python-ec2-api-tests

%description -n %{name}-all
%{common_desc}

This package contains all the tempest plugins.
%endif

%if 0%{?with_doc}
%package -n %{name}-doc
Summary:        %{name} documentation

BuildRequires:  python-sphinx
BuildRequires:  python-openstackdocstheme

%description -n %{name}-doc
%{common_desc}

It contains the documentation for Tempest.
%endif

%prep
%autosetup -n tempest-%{upstream_version} -S git
# have dependencies being handled by rpms, rather than requirement files
%py_req_cleanup

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

# Disable Build the plugin registry step as it uses git to clone
# projects and then generate tempest plugin projects list.
# It is also time taking.
sed -i '/def setup(app):/d' doc/source/conf.py
sed -i "/\s*app.connect('builder-inited', build_plugin_registry)/d" doc/source/conf.py

%build
%{__python2} setup.py build

%if 0%{?with_doc}
%{__python2} setup.py build_sphinx -b html
%endif

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

%if 0%{?with_doc}
%files -n %{name}-doc
%doc doc/build/html
%license LICENSE
%endif

%changelog
