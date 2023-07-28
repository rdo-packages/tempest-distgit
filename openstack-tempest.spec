%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0x2426b928085a020d8a90d0d879ab7008d0896c8a
%global project tempest
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
# we are excluding some BRs from automatic generator
%global excluded_brs doc8 bandit pre-commit hacking flake8-import-order bashate pycodestyle
# Exclude sphinx from BRs if docs are disabled
%if ! 0%{?with_doc}
%global excluded_brs %{excluded_brs} sphinx openstackdocstheme
%endif
%global with_doc 0
# guard for Red Hat OpenStack Platform supported tempest
%global rhosp 0
%global common_desc \
This is a set of integration tests to be run against a live OpenStack cluster.\
Tempest has batteries of tests for OpenStack API validation, Scenarios, and \
other specific tests useful in validating an OpenStack deployment.

Name:           openstack-%{project}
Epoch:          1
Version:        XXX
Release:        XXX
Summary:        OpenStack Integration Test Suite (Tempest)
License:        Apache-2.0
Url:            https://launchpad.net/tempest
Source0:        http://tarballs.openstack.org/tempest/tempest-%{upstream_version}.tar.gz

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        http://tarballs.openstack.org/tempest/tempest-%{upstream_version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif
BuildArch:      noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
%endif

BuildRequires:  git-core
BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  openstack-macros

Requires:       python3-tempest = %{epoch}:%{version}-%{release}

%if 0%{?repo_bootstrap} == 0
Requires:       python3-tempestconf
%endif

%description
%{common_desc}

%package -n    python3-%{project}
Summary:       Tempest Python library


# Obsoletes python-tempest-lib to avoid breakage
# during upgrade from Newton onwards to till this
# release
Obsoletes:     python-tempest-lib

%description -n python3-%{project}
%{common_desc}

This package contains the tempest python library.

%package -n     python3-%{project}-tests
Summary:        Python Tempest tests
Requires:       python3-tempest = %{epoch}:%{version}-%{release}

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
Requires:       python3-ironic-tests-tempest
Requires:       python3-keystone-tests-tempest
Requires:       python3-neutron-tests-tempest
Requires:       python3-manila-tests-tempest
Requires:       python3-telemetry-tests-tempest
Requires:       python3-octavia-tests-tempest
Requires:       python3-networking-l2gw-tests-tempest
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

%description -n %{name}-all
%{common_desc}

This package contains all the tempest plugins.
%endif

%if 0%{?with_doc}
%package -n %{name}-doc
Summary:        %{name} documentation

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

sed -i /^[[:space:]]*-c{env:.*_CONSTRAINTS_FILE.*/d tox.ini
sed -i "s/^deps = -c{env:.*_CONSTRAINTS_FILE.*/deps =/" tox.ini
sed -i /^minversion.*/d tox.ini
sed -i /^requires.*virtualenv.*/d tox.ini

# Exclude some bad-known BRs
for pkg in %{excluded_brs}; do
  for reqfile in doc/requirements.txt test-requirements.txt; do
    if [ -f $reqfile ]; then
      sed -i /^${pkg}.*/d $reqfile
    fi
  done
done

# Automatic BR generation
%generate_buildrequires
%if 0%{?with_doc}
  %pyproject_buildrequires -t -e %{default_toxenv},docs
%else
  %pyproject_buildrequires -t -e %{default_toxenv}
%endif

%build
%pyproject_wheel

%if 0%{?with_doc}
# Disable Build the plugin registry step as it uses git to clone
# projects and then generate tempest plugin projects list.
# It is also time taking.
export GENERATE_TEMPEST_PLUGIN_LIST='False'
%tox -e docs
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}
%endif

%install
%pyproject_install

# Generate tempest config
mkdir -p %{buildroot}%{_sysconfdir}/%{project}/
PYTHONPATH="%{buildroot}/%{python3_sitelib}" oslo-config-generator --config-file tempest/cmd/config-generator.tempest.conf \
    --output-file %{buildroot}%{_sysconfdir}/%{project}/tempest.conf

mkdir -p %{buildroot}/etc/tempest
mv %{buildroot}/usr/etc/tempest/* %{buildroot}/etc/tempest

%check
export OS_TEST_PATH='./tempest/tests'
rm -f $OS_TEST_PATH/test_hacking.py
%tox -e %{default_toxenv}

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
%{python3_sitelib}/%{project}*.dist-info
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
