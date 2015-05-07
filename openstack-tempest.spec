%global         timestamp 20150507

Name:           openstack-tempest
Epoch:          1
Version:        kilo
Release:        %{timestamp}.2%{?dist}
Summary:        OpenStack Integration Test Suite (Tempest)
License:        ASL 2.0
Url:            https://github.com/redhat-openstack/tempest
Source0:        https://github.com/redhat-openstack/tempest/archive/openstack-tempest-%{version}-%{timestamp}.tar.gz
BuildArch:      noarch

Patch0001: 0001-Remove-some-shebangs.patch

BuildRequires:  fdupes
BuildRequires:  python-sphinx
BuildRequires:  python-d2to1
BuildRequires:  python-distribute
BuildRequires:  python-pbr
BuildRequires:  python2-devel

Requires:       python
Requires:       python-anyjson
Requires:       python-boto
Requires:       python-cinderclient
Requires:       python-fixtures
Requires:       python-glanceclient
Requires:       python-heatclient
Requires:       python-ironicclient
Requires:       python-iso8601
Requires:       python-junitxml
Requires:       python-keyring
Requires:       python-keystoneclient
Requires:       python-lxml
Requires:       python-netaddr
Requires:       python-neutronclient
Requires:       python-nose
Requires:       python-novaclient
Requires:       python-oslo-config
Requires:       python-paramiko
Requires:       python-pbr
Requires:       python-saharaclient
Requires:       python-swiftclient
Requires:       python-testrepository
Requires:       python-testresources
Requires:       python-testscenarios
Requires:       python-testtools
Requires:       which
Requires:       python-tempest-lib >= 0.4.0
Requires:       subunit-filters

Provides:       openstack-tempest-kilo
Obsoletes:      openstack-tempest-juno < 20150319
Obsoletes:      openstack-tempest-icehouse < 20150319

%description
This is a set of integration tests to be run against a live OpenStack cluster.
Tempest has batteries of tests for OpenStack API validation, Scenarios, and
other specific tests useful in validating an OpenStack deployment.


%prep
%setup -q -n tempest-%{name}-%{version}-%{timestamp}
%patch0001 -p1

%install
mkdir -p %{buildroot}%{_datarootdir}/%{name}-%{version}
cp --preserve=mode -r . %{buildroot}%{_datarootdir}/%{name}-%{version}

%build

%files
%doc LICENSE
%defattr(-,root,root)
%{_datarootdir}/%{name}-%{version}
%exclude %{_datarootdir}/%{name}-%{version}/.gitignore
%exclude %{_datarootdir}/%{name}-%{version}/.gitreview
%exclude %{_datarootdir}/%{name}-%{version}/.mailmap
%exclude %{_datarootdir}/%{name}-%{version}/.coveragerc

%changelog
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
