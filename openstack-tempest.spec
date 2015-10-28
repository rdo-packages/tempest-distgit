%global project tempest
%global release_name liberty
%global         timestamp 20151020

Name:           openstack-%{project}
Epoch:          1
Version:        %{release_name}
Release:        %{timestamp}.2%{?dist}
Summary:        OpenStack Integration Test Suite (Tempest)
License:        ASL 2.0
Url:            https://github.com/redhat-openstack/tempest
Source0:        https://github.com/redhat-openstack/tempest/archive/openstack-tempest-%{version}-%{timestamp}.tar.gz
BuildArch:      noarch

BuildRequires:  fdupes
BuildRequires:  git
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
Requires:       python-oslo-config >= 2:2.3.0
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
%autosetup -n tempest-%{name}-%{version}-%{timestamp} -S git
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
mkdir -p %{buildroot}%{_datarootdir}/%{name}-%{release_name}
cp --preserve=mode -r . %{buildroot}%{_datarootdir}/%{name}-%{release_name}
rm -rf %{buildroot}%{_datarootdir}/%{name}-%{release_name}/.git*
rm -rf %{buildroot}%{_datarootdir}/%{name}-%{release_name}/build
rm -f  %{buildroot}%{_datarootdir}/%{name}-%{release_name}/doc/source/_static/.keep
%{__python} setup.py install --skip-build --root %{buildroot}
mkdir -p %{buildroot}/etc/tempest
mv %{buildroot}/usr/etc/tempest/* %{buildroot}/etc/tempest

%build
%{__python} setup.py build

%files
%license LICENSE
%defattr(-,root,root)
%{_datarootdir}/%{name}-%{release_name}
%exclude %{_datarootdir}/%{name}-%{release_name}/.mailmap
%exclude %{_datarootdir}/%{name}-%{release_name}/.coveragerc
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
* Wed Oct 28 2015 Steve Linabery <slinaber@redhat.com> - 1:liberty-20151020.2
- fix version Requires for python-oslo-config to add Epoch
- fix date on previous changelog entry

* Fri Oct 23 2015 Steve Linabery <slinaber@redhat.com> - 1:liberty-20151020.1
- Rebase to new midstream tag on liberty branch

* Wed Jul 08 2015 Steve Linabery <slinaber@redhat.com> - kilo-20150708.2
- Update Requires based on requirements.txt

* Wed Jul 08 2015 Steve Linabery <slinaber@redhat.com> - kilo-20150708.1
- Rebase to new midstream tag on kilo branch

* Wed Jul 01 2015 Steve Linabery <slinaber@redhat.com> - kilo-20150507.3
- Update Requires on python-tempest-lib to 0.5.0

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:kilo-20150507.2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu May 07 2015 Steve Linabery <slinaber@redhat.com> - kilo-20150507.2
- Remove shebangs from specific .py files with patch file

* Thu May 07 2015 Steve Linabery <slinaber@redhat.com> - kilo-20150507.1
- Rebase to new midstream tag on kilo branch

* Wed May 06 2015 Steve Linabery <slinaber@redhat.com> - kilo-20150506.1
- Rebase to new midstream tag on kilo branch
- remove Requires on subunit-filters

* Mon May 04 2015 Steve Linabery <slinaber@redhat.com> - kilo-20150413.3
- Add provides/obsoletes

* Thu Apr 16 2015 Steve Linabery <slinaber@redhat.com> - kilo-20150413.2
- Add Requires for subunit-filters

* Mon Apr 13 2015 Steve Linabery <slinaber@redhat.com> - kilo-20150413.1
- rebase to latest tag
- Add Requires on python-tempest-lib

* Tue Mar 24 2015 Steve Linabery <slinaber@redhat.com> - 20150319-1
- new kilo RPM from latest tag

* Mon Dec 01 2014 Steve Linabery <slinaber@redhat.com> - 20141201-1
- rebase to latest tag

* Thu Nov 06 2014 Steve Linabery <slinaber@redhat.com> - 20141105-3
- fix perms on  tools/configure-tempest-directory

* Thu Nov 06 2014 Steve Linabery <slinaber@redhat.com> - 20141105-2
- sync w/juno branch, patch tools/configure-tempest-directory

* Wed Nov 05 2014 Steve Linabery <slinaber@redhat.com> - 20141105-1
- rebase to latest tag
- add juno subpackage

* Mon Sep 15 2014 Steve Linabery <slinaber@redhat.com> - 20140915-2
- add runtime dep on package which

* Mon Sep 15 2014 Steve Linabery <slinaber@redhat.com> - 20140915-1
- rebase to latest upstream tag

* Wed Aug 06 2014 Steve Linabery <slinaber@redhat.com> - 20140805-1
- rebase to latest tag
- use relative path to LICENSE

* Tue Aug 05 2014 Steve Linabery <slinaber@redhat.com> - 20140703-4
- keep .testr.conf

* Mon Aug 04 2014 Steve Linabery <slinaber@redhat.com> - 20140703-3
- Move Requires into subpackage openstack-tempest-icehouse

* Thu Jul 03 2014 Steve Linabery <slinaber@redhat.com> - 20140703-2
- relax python version requirement for el6

* Thu Jul 03 2014 Steve Linabery <slinaber@redhat.com> - 20140703-1
- rebase to latest tag

* Wed Jun 25 2014 Steve Linabery <slinaber@redhat.com> - 20140625-1
- Initial package.
