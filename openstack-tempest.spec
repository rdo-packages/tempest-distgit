%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0x5d2d1e4fb8d38e6af76c50d53d4fec30cf5ce3da
%global project tempest
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%global with_doc 1
# guard for Red Hat OpenStack Platform supported tempest
%global rhosp 0
# enable bootstrap mode
%global repo_bootstrap 0
%global common_desc \
This is a set of integration tests to be run against a live OpenStack cluster.\
Tempest has batteries of tests for OpenStack API validation, Scenarios, and \
other specific tests useful in validating an OpenStack deployment.

Name:           openstack-%{project}
Epoch:          1
Version:        26.0.0
Release:        1%{?dist}
Summary:        OpenStack Integration Test Suite (Tempest)
License:        ASL 2.0
Url:            https://launchpad.net/tempest
Source0:        http://tarballs.openstack.org/tempest/tempest-%{upstream_version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        http://tarballs.openstack.org/tempest/tempest-%{upstream_version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif
# This reverts removal of an old tempest/manager.py in order to provide
# compatibility with neutron-tempest-plugin which has switched to the
# new manager location at very latest and the change hasn't been included in
# a tag nor a release. We revert the removal in tempest so that we can package
# tempest 26.1.0 and ship it in Victoria. Tempest 26.1.0 contains apart from
# the fixes also a significant argument deprecation.
Patch 0001: 0001-Revert-Remove-tempest-manager.py-after-4-year-deprec.patch
BuildArch:      noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
%endif

BuildRequires:  git
BuildRequires:  python3-oslo-config
BuildRequires:  python3-pbr
BuildRequires:  python3-setuptools
BuildRequires:  python3-devel
BuildRequires:  openstack-macros

Requires:       python3-tempest = %{epoch}:%{version}-%{release}

%if 0%{?repo_bootstrap} == 0
Requires:       python3-tempestconf
%endif

%description
%{common_desc}

%package -n    python3-%{project}
Summary:       Tempest Python library

%{?python_provide:%python_provide python2-%{project}}

# Obsoletes python-tempest-lib to avoid breakage
# during upgrade from Newton onwards to till this
# release
Obsoletes:     python-tempest-lib

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
Requires:      python3-subunit

Requires:      python3-unittest2
Requires:      python3-PyYAML

%description -n python3-%{project}
%{common_desc}

This package contains the tempest python library.

%package -n     python3-%{project}-tests
Summary:        Python Tempest tests
Requires:       python3-tempest = %{epoch}:%{version}-%{release}
%{?python_provide:%python_provide python2-%{project}-tests}

BuildRequires:  python3-mock
BuildRequires:  python3-oslotest
BuildRequires:  python3-subunit
BuildRequires:  python3-oslo-log
BuildRequires:  python3-jsonschema
BuildRequires:  python3-urllib3
BuildRequires:  python3-oslo-concurrency
BuildRequires:  python3-paramiko
BuildRequires:  python3-cliff
BuildRequires:  python3-pycodestyle
BuildRequires:  python3-os-testr
BuildRequires:  python3-stestr

BuildRequires:  python3-PyYAML


Requires:       python3-mock
Requires:       python3-oslotest

%description -n python3-%{project}-tests
%{common_desc}

This package contains tests for the tempest python library.

%if 0%{?repo_bootstrap} == 0
%package -n    %{name}-all
Summary:       All OpenStack Tempest Plugins

Requires:      %{name} = %{epoch}:%{version}-%{release}

Requires:       python3-cinder-tests-tempest
Requires:       python3-designate-tests-tempest
Requires:       python3-heat-tests-tempest
Requires:       python3-horizon-tests-tempest
Requires:       python3-ironic-tests-tempest
Requires:       python3-keystone-tests-tempest
Requires:       python3-mistral-tests-tempest
Requires:       python3-neutron-tests-tempest
Requires:       python3-zaqar-tests-tempest
Requires:       python3-manila-tests-tempest
Requires:       python3-telemetry-tests-tempest
# octavia-tests-tempest missing due to https://bugs.centos.org/view.php?id=17139
%if 0%{?dlrn} != 0
Requires:       python3-octavia-tests-tempest
%endif
Requires:       python3-networking-l2gw-tests-tempest
Requires:       python3-patrole-tests-tempest
Requires:       python3-novajoin-tests-tempest
Requires:       python3-kuryr-tests-tempest
Requires:       python3-barbican-tests-tempest

%if 0%{?rhosp} == 0
Requires:       python3-magnum-tests-tempest
Requires:       python3-murano-tests-tempest
Requires:       python3-sahara-tests-tempest
Requires:       python3-trove-tests-tempest
Requires:       python3-vitrage-tests-tempest
Requires:       python3-watcher-tests-tempest
%endif

%description -n %{name}-all
%{common_desc}

This package contains all the tempest plugins.
%endif

%if 0%{?with_doc}
%package -n %{name}-doc
Summary:        %{name} documentation

BuildRequires:  python3-sphinx
BuildRequires:  python3-openstackdocstheme
BuildRequires:  python3-sphinxcontrib-rsvgconverter

%description -n %{name}-doc
%{common_desc}

It contains the documentation for Tempest.
%endif

%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
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
%{py3_build}

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
%{py3_install}

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
rm -f $OS_TEST_PATH/test_hacking.py
PYTHON=%{__python3} stestr --test-path $OS_TEST_PATH run

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

%files -n python3-%{project}
%license LICENSE
%{python3_sitelib}/%{project}
%{python3_sitelib}/%{project}*.egg-info
%exclude %{python3_sitelib}/tempest/tests

%files -n python3-%{project}-tests
%license LICENSE
%{python3_sitelib}/tempest/tests

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
* Tue Dec 22 2020 RDO <dev@lists.rdoproject.org> 1:26.0.0-1
- Update to 26.0.0

* Tue Oct 20 2020 Joel Capitao <jcapitao@redhat.com> 1:25.0.0-3
- Enable sources tarball validation using GPG signature.

* Wed Oct 7 2020 Bhagyashri Shewale <bshewale@redhat.com> - 1:25.0.0-2
- Disable repo_bootstrap and include openstack-tempest-all package
- Exclude octavia-tests-tempest for non dlrn builds

* Thu Sep 24 2020 RDO <dev@lists.rdoproject.org> 1:25.0.0-1
- Update to 25.0.0

# REMOVEME: error caused by commit https://opendev.org/openstack/tempest/commit/f9d31f2c46204abbbef53d3c0ae0f80125878fc9
