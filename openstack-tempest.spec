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
%global repo_bootstrap 1
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
BuildRequires:  python2-oslo-config
BuildRequires:  python2-pbr
BuildRequires:  python2-setuptools
BuildRequires:  python2-devel
BuildRequires:  openstack-macros

%if 0%{?with_python3}
Requires:       python3-tempest = %{epoch}:%{version}-%{release}
%else
Requires:       python2-tempest = %{epoch}:%{version}-%{release}
%endif

%if 0%{?repo_bootstrap} == 0
Requires:     python2-tempestconf
%endif

%description
%{common_desc}

%package -n    python2-%{project}
Summary:       Tempest Python library

%{?python_provide:%python_provide python2-%{project}}

# Obsoletes python-tempest-lib to avoid breakage
# during upgrade from Newton onwards to till this
# release
Obsoletes:     python-tempest-lib

Requires:      python2-cliff
Requires:      python2-debtcollector
Requires:      python2-fixtures
Requires:      python2-jsonschema
Requires:      python2-netaddr
Requires:      python2-oslo-concurrency >= 3.26.0
Requires:      python2-oslo-config >= 2:5.2.0
Requires:      python2-oslo-log >= 3.36.0
Requires:      python2-oslo-serialization >= 2.18.0
Requires:      python2-oslo-utils >= 3.33.0
Requires:      python2-os-testr >= 0.8.0
Requires:      python2-paramiko
Requires:      python2-pbr
Requires:      python2-prettytable
Requires:      python2-six
Requires:      python2-stevedore
Requires:      python2-stestr
Requires:      python2-testtools
Requires:      python2-urllib3
Requires:      python2-subunit
%if 0%{?fedora} > 0
Requires:      python2-unittest2
Requires:      python2-pyyaml
%else
Requires:      python-unittest2
Requires:      PyYAML
%endif
%description -n python2-%{project}
%{common_desc}

This package contains the tempest python library.

%package -n     python2-%{project}-tests
Summary:        Python Tempest tests
Requires:       python2-tempest = %{epoch}:%{version}-%{release}
%{?python_provide:%python_provide python2-%{project}-tests}

BuildRequires:  python2-mock
BuildRequires:  python2-oslotest
BuildRequires:  python2-subunit
BuildRequires:  python2-oslo-log
BuildRequires:  python2-jsonschema
BuildRequires:  python2-urllib3
BuildRequires:  PyYAML
BuildRequires:  python2-oslo-concurrency
BuildRequires:  python2-paramiko
BuildRequires:  python2-cliff
%if 0%{?fedora} > 0
BuildRequires:  python2-pep8
%else
BuildRequires:  python-pep8
%endif
BuildRequires:  python2-os-testr
BuildRequires:  python2-stestr

Requires:       python2-mock
Requires:       python2-oslotest

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
Requires:      python3-oslo-concurrency >= 3.26.0
Requires:      python3-oslo-config >= 2:5.2.0
Requires:      python3-oslo-log >= 3.36.0
Requires:      python3-oslo-serialization >= 2.18.0
Requires:      python3-oslo-utils >= 3.33.0
Requires:      python3-os-testr >= 0.8.0
Requires:      python3-paramiko
Requires:      python3-pbr
Requires:      python3-prettytable
Requires:      python3-six
Requires:      python3-stevedore
Requires:      python3-stestr
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

Requires:       python-cinder-tests-tempest
Requires:       python-designate-tests-tempest
Requires:       python-heat-tests-tempest
Requires:       python-horizon-tests-tempest
Requires:       python-ironic-tests-tempest
Requires:       python-keystone-tests-tempest
Requires:       python-mistral-tests-tempest
Requires:       python-neutron-tests-tempest
Requires:       python-sahara-tests-tempest
Requires:       python-zaqar-tests-tempest
Requires:       python-manila-tests-tempest
Requires:       python-telemetry-tests-tempest
Requires:       python-octavia-tests-tempest
Requires:       python-ec2api-tests-tempest
Requires:       python-networking-l2gw-tests-tempest
Requires:       python-patrole-tests-tempest
Requires:       python-tripleo-common-tests-tempest
Requires:       python-novajoin-tests-tempest
Requires:       python-kuryr-tests-tempest
Requires:       python-barbican-tests-tempest

%if 0%{?rhosp} == 0
Requires:       python-congress-tests-tempest
Requires:       python-magnum-tests-tempest
Requires:       python-murano-tests-tempest
Requires:       python-trove-tests-tempest
Requires:       python-vitrage-tests-tempest
Requires:       python-watcher-tests-tempest
%endif

%description -n %{name}-all
%{common_desc}

This package contains all the tempest plugins.
%endif

%if 0%{?with_doc}
%package -n %{name}-doc
Summary:        %{name} documentation

BuildRequires:  python2-sphinx
BuildRequires:  python2-openstackdocstheme

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
export PYTHONPATH=.
export GENERATE_TEMPEST_PLUGIN_LIST='False'
sphinx-build -b html doc/source doc/build/html
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}
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
# REMOVEME: error caused by commit http://git.openstack.org/cgit/openstack/tempest/commit/?id=9c71dcfa7c24a1fea350c07f4008964d857957ad
