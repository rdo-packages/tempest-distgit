# Macros for py2/py3 compatibility
%if 0%{?fedora} || 0%{?rhel} > 7
%global pyver %{python3_pkgversion}
%else
%global pyver 2
%endif
%global pyver_bin python%{pyver}
%global pyver_sitelib %{expand:%{python%{pyver}_sitelib}}
%global pyver_install %{expand:%{py%{pyver}_install}}
%global pyver_build %{expand:%{py%{pyver}_build}}
# End of macros for py2/py3 compatibility
%global project tempest
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%global with_doc 1
# guard for Red Hat OpenStack Platform supported tempest
%global rhosp 0
%global common_desc \
This is a set of integration tests to be run against a live OpenStack cluster.\
Tempest has batteries of tests for OpenStack API validation, Scenarios, and \
other specific tests useful in validating an OpenStack deployment.

Name:           openstack-%{project}
Epoch:          1
Version:        24.0.0
Release:        1%{?dist}
Summary:        OpenStack Integration Test Suite (Tempest)
License:        ASL 2.0
Url:            https://launchpad.net/tempest
Source0:        http://tarballs.openstack.org/tempest/tempest-%{upstream_version}.tar.gz
BuildArch:      noarch

BuildRequires:  git
BuildRequires:  python%{pyver}-oslo-config
BuildRequires:  python%{pyver}-pbr
BuildRequires:  python%{pyver}-setuptools
BuildRequires:  python%{pyver}-devel
BuildRequires:  openstack-macros

Requires:       python%{pyver}-tempest = %{epoch}:%{version}-%{release}

%if 0%{?repo_bootstrap} == 0
Requires:       python%{pyver}-tempestconf
%endif

%description
%{common_desc}

%package -n    python%{pyver}-%{project}
Summary:       Tempest Python library

%{?python_provide:%python_provide python2-%{project}}

# Obsoletes python-tempest-lib to avoid breakage
# during upgrade from Newton onwards to till this
# release
Obsoletes:     python-tempest-lib

Requires:      python%{pyver}-cliff
Requires:      python%{pyver}-debtcollector
Requires:      python%{pyver}-fixtures
Requires:      python%{pyver}-jsonschema
Requires:      python%{pyver}-netaddr
Requires:      python%{pyver}-oslo-concurrency >= 3.26.0
Requires:      python%{pyver}-oslo-config >= 2:5.2.0
Requires:      python%{pyver}-oslo-log >= 3.36.0
Requires:      python%{pyver}-oslo-serialization >= 2.18.0
Requires:      python%{pyver}-oslo-utils >= 3.33.0
Requires:      python%{pyver}-os-testr >= 0.8.0
Requires:      python%{pyver}-paramiko
Requires:      python%{pyver}-pbr
Requires:      python%{pyver}-prettytable
Requires:      python%{pyver}-six
Requires:      python%{pyver}-stevedore
Requires:      python%{pyver}-stestr
Requires:      python%{pyver}-testtools
Requires:      python%{pyver}-urllib3
Requires:      python%{pyver}-subunit

# Handle python2 exception
%if %{pyver} == 2
Requires:      python-unittest2
Requires:      PyYAML
Requires:      python2-mock
Requires:      python-configparser
%else
Requires:      python%{pyver}-unittest2
Requires:      python%{pyver}-PyYAML
%endif

%description -n python%{pyver}-%{project}
%{common_desc}

This package contains the tempest python library.

%package -n     python%{pyver}-%{project}-tests
Summary:        Python Tempest tests
Requires:       python%{pyver}-tempest = %{epoch}:%{version}-%{release}
%{?python_provide:%python_provide python2-%{project}-tests}

BuildRequires:  python%{pyver}-mock
BuildRequires:  python%{pyver}-oslotest
BuildRequires:  python%{pyver}-subunit
BuildRequires:  python%{pyver}-oslo-log
BuildRequires:  python%{pyver}-jsonschema
BuildRequires:  python%{pyver}-urllib3
BuildRequires:  python%{pyver}-oslo-concurrency
BuildRequires:  python%{pyver}-paramiko
BuildRequires:  python%{pyver}-cliff
BuildRequires:  python%{pyver}-pycodestyle
BuildRequires:  python%{pyver}-os-testr
BuildRequires:  python%{pyver}-stestr
BuildRequires:  python%{pyver}-hacking

# Handle python2 exception
%if %{pyver} == 2
BuildRequires:  PyYAML
BuildRequires:  python2-mock
BuildRequires:  python-configparser
%else
BuildRequires:  python%{pyver}-PyYAML
%endif


Requires:       python%{pyver}-mock
Requires:       python%{pyver}-oslotest

%description -n python%{pyver}-%{project}-tests
%{common_desc}

This package contains tests for the tempest python library.

%if 0%{?repo_bootstrap} == 0
%package -n    %{name}-all
Summary:       All OpenStack Tempest Plugins

Requires:      %{name} = %{epoch}:%{version}-%{release}

Requires:       python%{pyver}-cinder-tests-tempest
Requires:       python%{pyver}-designate-tests-tempest
Requires:       python%{pyver}-heat-tests-tempest
Requires:       python%{pyver}-horizon-tests-tempest
Requires:       python%{pyver}-ironic-tests-tempest
Requires:       python%{pyver}-keystone-tests-tempest
Requires:       python%{pyver}-mistral-tests-tempest
Requires:       python%{pyver}-neutron-tests-tempest
Requires:       python%{pyver}-zaqar-tests-tempest
Requires:       python%{pyver}-manila-tests-tempest
Requires:       python%{pyver}-telemetry-tests-tempest
Requires:       python%{pyver}-octavia-tests-tempest
Requires:       python%{pyver}-networking-l2gw-tests-tempest
Requires:       python%{pyver}-patrole-tests-tempest
Requires:       python%{pyver}-novajoin-tests-tempest
Requires:       python%{pyver}-kuryr-tests-tempest
Requires:       python%{pyver}-barbican-tests-tempest

%if 0%{?rhosp} == 0
Requires:       python%{pyver}-congress-tests-tempest
Requires:       python%{pyver}-magnum-tests-tempest
Requires:       python%{pyver}-murano-tests-tempest
Requires:       python%{pyver}-sahara-tests-tempest
Requires:       python%{pyver}-trove-tests-tempest
Requires:       python%{pyver}-vitrage-tests-tempest
Requires:       python%{pyver}-watcher-tests-tempest
%endif

%description -n %{name}-all
%{common_desc}

This package contains all the tempest plugins.
%endif

%if 0%{?with_doc}
%package -n %{name}-doc
Summary:        %{name} documentation

BuildRequires:  python%{pyver}-sphinx
BuildRequires:  python%{pyver}-openstackdocstheme
BuildRequires:  python%{pyver}-sphinxcontrib-rsvgconverter

%description -n %{name}-doc
%{common_desc}

It contains the documentation for Tempest.
%endif

%prep
%autosetup -n tempest-%{upstream_version} -S git
# have dependencies being handled by rpms, rather than requirement files
%py_req_cleanup

# Adjust use of 'stestr' binary in tests
sed -i "s/'stestr'/'stestr-%{pyver}'/" tempest/tests/cmd/test_run.py tempest/tests/test_list_tests.py

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
%{pyver_build}

%if 0%{?with_doc}
# Disable Build the plugin registry step as it uses git to clone
# projects and then generate tempest plugin projects list.
# It is also time taking.
export PYTHONPATH=.
export GENERATE_TEMPEST_PLUGIN_LIST='False'
sphinx-build-%{pyver} -b html doc/source doc/build/html
# remove the sphinx-build-%{pyver} leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}
%endif

# workaround for handling py2 and py3 mock issue
%if %{pyver} == 2
find ./tempest/tests -type f -exec sed -i -e 's/from unittest import mock/import mock/g' {} \;
find ./tempest/tests -type f -exec sed -i -e 's/from unittest.mock import patch/from mock import patch/g' {} \;
find ./tempest/cmd -type f -exec sed -i -e 's/from urllib import parse as urlparse/import urlparse/g' {} \;
# revert of https://review.opendev.org/#/c/732960/
sed -i -e 's/import six/from __future__ import absolute_import\n\nimport six/g' tempest/lib/common/thread.py
sed -i -e 's/import os/from __future__ import print_function\n\nimport os/g' tempest/config.py
%endif

%install
%{pyver_install}
rm -rf %{buildroot}/usr/bin/verify-tempest-config
rm -rf %{buildroot}/usr/bin/tempest-account-generator

# Generate tempest config
mkdir -p %{buildroot}%{_sysconfdir}/%{project}/
oslo-config-generator-%{pyver} --config-file tempest/cmd/config-generator.tempest.conf \
    --output-file %{buildroot}%{_sysconfdir}/%{project}/tempest.conf

mkdir -p %{buildroot}/etc/tempest
mv %{buildroot}/usr/etc/tempest/* %{buildroot}/etc/tempest

%check
export OS_TEST_PATH='./tempest/tests'
export PATH=$PATH:$RPM_BUILD_ROOT/usr/bin
export PYTHONPATH=$PWD
PYTHON=%{pyver_bin} stestr-%{pyver} --test-path $OS_TEST_PATH run

%files
%license LICENSE
%doc README.rst
%{_bindir}/tempest
%{_bindir}/check-uuid
%{_bindir}/skip-tracker
%{_bindir}/subunit-describe-calls
%{_sysconfdir}/%{project}/*sample
%{_sysconfdir}/%{project}/*yaml
%config(noreplace) %{_sysconfdir}/%{project}/*.conf

%files -n python%{pyver}-%{project}
%license LICENSE
%{pyver_sitelib}/%{project}
%{pyver_sitelib}/%{project}*.egg-info
%exclude %{pyver_sitelib}/tempest/tests

%files -n python%{pyver}-%{project}-tests
%license LICENSE
%{pyver_sitelib}/tempest/tests

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
* Mon Jun 15 2020 RDO <dev@lists.rdoproject.org> 1:24.0.0-1
- Update to 24.0.0

* Wed Feb 05 2020 RDO <dev@lists.rdoproject.org> 1:23.0.0-1
- Update to 23.0.0

* Wed Oct 16 2019 RDO <dev@lists.rdoproject.org> 1:22.1.0-1
- Update to 22.1.0

* Mon Oct 07 2019 RDO <dev@lists.rdoproject.org> 1:22.0.0-1
- Update to 22.0.0

