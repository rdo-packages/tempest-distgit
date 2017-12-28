%global project tempest
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%global with_doc 1
# guard for Red Hat OpenStack Platform supported tempest
%global rhosp 0
%global common_desc \
This is a set of integration tests to be run against a live OpenStack cluster.\
Tempest has batteries of tests for OpenStack API validation, Scenarios, and \
other specific tests useful in validating an OpenStack deployment.

%if 0%{?fedora} >= 24
%global with_python3 1
%endif

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

%description
%{common_desc}

%package -n    python2-%{project}
Summary:       Tempest Python library

%{?python_provide:%python_provide python2-%{project}}

Requires:      python-cliff
Requires:      python-debtcollector
Requires:      python-fixtures
Requires:      python-jsonschema
Requires:      python-netaddr
Requires:      python-oslo-concurrency >= 3.8.0
Requires:      python-oslo-config >= 2:4.0.0
Requires:      python-oslo-log >= 3.22.0
Requires:      python-oslo-serialization >= 1.10.0
Requires:      python-oslo-utils >= 3.20.0
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
Requires:      python-unittest2

%description -n python2-%{project}
%{common_desc}

This package contains the tempest python library.

%package -n     python2-%{project}-tests
Summary:        Python Tempest tests
Requires:       python2-tempest = %{epoch}:%{version}-%{release}
%{?python_provide:%python_provide python2-%{project}-tests}

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
BuildRequires:  python-stestr

Requires:       python-mock
Requires:       python-oslotest

%description -n python2-%{project}-tests
%{common_desc}

This package contains tests for the tempest python library.

# Python3 package
%if 0%{?with_python3}
%package -n    python3-%{project}
Summary:       Tempest Python library

%{?python_provide:%python_provide python3-%{project}}
BuildRequires:  python3-oslo-config
BuildRequires:  python3-pbr
BuildRequires:  python3-setuptools
BuildRequires:  python3-devel

Requires:      python3-cliff
Requires:      python3-debtcollector
Requires:      python3-fixtures
Requires:      python3-jsonschema
Requires:      python3-netaddr
Requires:      python3-oslo-concurrency >= 3.8.0
Requires:      python3-oslo-config >= 2:4.0.0
Requires:      python3-oslo-log >= 3.22.0
Requires:      python3-oslo-serialization >= 1.10.0
Requires:      python3-oslo-utils >= 3.20.0
Requires:      python3-os-testr >= 0.8.0
Requires:      python3-paramiko
Requires:      python3-pbr
Requires:      python3-prettytable
Requires:      python3-six
Requires:      python3-stevedore
Requires:      python3-testrepository
Requires:      python3-testtools
Requires:      python3-urllib3
Requires:      python3-PyYAML
Requires:      python3-subunit
Requires:      python3-unittest2

%description -n python3-%{project}
%{common_desc}

This package contains the tempest python library.

%package -n     python3-%{project}-tests
Summary:        Python Tempest tests
%{?python_provide:%python_provide python3-%{project}-tests}

Requires:       python3-tempest = %{epoch}:%{version}-%{release}

BuildRequires:  python3-oslotest
BuildRequires:  python3-subunit
BuildRequires:  python3-oslo-log
BuildRequires:  python3-jsonschema
BuildRequires:  python3-urllib3
BuildRequires:  python3-PyYAML
BuildRequires:  python3-oslo-concurrency
BuildRequires:  python3-paramiko
BuildRequires:  python3-cliff
BuildRequires:  python3-pep8
BuildRequires:  python3-os-testr
BuildRequires:  python3-stestr

Requires:       python3-oslotest

%description -n python3-%{project}-tests
%{common_desc}

This package contains tests for the tempest python library.
%endif

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
Requires:       python-nova-tests
Requires:       python-sahara-tests-tempest
Requires:       python-swift-tests
Requires:       python-zaqar-tests
Requires:       python-manila-tests
Requires:       python-ironic-inspector-tests
Requires:       python-panko-tests
Requires:       python-octavia-tests
Requires:       python-ec2-api-tests

%if 0%{?rhosp} == 0
Requires:       python-congress-tests
Requires:       python-magnum-tests
Requires:       python-murano-tests
Requires:       python-neutron-vpnaas-tests
Requires:       python-trove-tests
Requires:       python-vitrage-tests
Requires:       python-watcher-tests-tempest
%endif

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

%build
%py2_build
%if 0%{?with_python3}
%py3_build
%endif

%if 0%{?with_doc}
# Disable Build the plugin registry step as it uses git to clone
# projects and then generate tempest plugin projects list.
# It is also time taking.
export GENERATE_TEMPEST_PLUGIN_LIST='False'
# TODO(ihrachys): remove when https://review.openstack.org/#/c/523235/ is
# released
sed -i 's/warning-is-error = 1/warning-is-error = 0/' setup.cfg
%{__python2} setup.py build_sphinx -b html
%endif

%install
%py2_install
%if 0%{?with_python3}
%py3_install
%endif

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
stestr --test-path $OS_TEST_PATH run
%if 0%{?with_python3}
rm -rf .stestr
stestr-3 --test-path $OS_TEST_PATH run
%endif

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

%files -n python2-%{project}
%license LICENSE
%{python2_sitelib}/%{project}
%{python2_sitelib}/%{project}*.egg-info
%exclude %{python2_sitelib}/tempest/tests

%files -n python2-%{project}-tests
%license LICENSE
%{python2_sitelib}/tempest/tests

%if 0%{?with_python3}
%files -n python3-%{project}
%license LICENSE
%{python3_sitelib}/%{project}
%{python3_sitelib}/%{project}*.egg-info
%exclude %{python3_sitelib}/tempest/tests

%files -n python3-%{project}-tests
%license LICENSE
%{python3_sitelib}/tempest/tests
%endif

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
# REMOVEME: error caused by commit http://git.openstack.org/cgit/openstack/tempest/commit/?id=ac6ce0005e2600833f5313ed18ed0684eb36b6fa
