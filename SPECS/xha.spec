%global package_speccommit f7bea5d97a5d59bee0a3ca6483a7efa0c7115842
%global package_srccommit v10.3.1
Summary: xha - XenServer proprietary HA daemon
Name:    xha
Version: 10.3.1
Release: 3%{?xsrel}%{?dist}
License: GPLv2
URL:     https://github.com/xenserver/xha
Source0: xha-10.3.1.tar.gz

BuildRequires: libxml2-devel
BuildRequires: xen-devel
%{?_cov_buildrequires}

Requires: portreserve

%description
This package contains the HA heartbeating daemon used for XenServer's HA feature

%prep
%autosetup -p1
%{?_cov_prepare}

%build
%{?_cov_wrap} make

%install
DESTDIR=$RPM_BUILD_ROOT make install
%{?_cov_install}

%files
%{_sysconfdir}/logrotate.d/xha
%{_sysconfdir}/portreserve/xhad
%{_libexecdir}/xapi/cluster-stack/xhad/calldaemon
%{_libexecdir}/xapi/cluster-stack/xhad/cleanupwatchdog
%{_libexecdir}/xapi/cluster-stack/xhad/dumpstatefile
%{_libexecdir}/xapi/cluster-stack/xhad/ha_clear_excluded
%{_libexecdir}/xapi/cluster-stack/xhad/ha_disarm_fencing
%{_libexecdir}/xapi/cluster-stack/xhad/ha_errnorc
%{_libexecdir}/xapi/cluster-stack/xhad/ha_null
%{_libexecdir}/xapi/cluster-stack/xhad/ha_propose_master
%{_libexecdir}/xapi/cluster-stack/xhad/ha_query_liveset
%{_libexecdir}/xapi/cluster-stack/xhad/ha_rc
%{_libexecdir}/xapi/cluster-stack/xhad/ha_set_excluded
%{_libexecdir}/xapi/cluster-stack/xhad/ha_set_host_weight
%{_libexecdir}/xapi/cluster-stack/xhad/ha_set_pool_state
%{_libexecdir}/xapi/cluster-stack/xhad/ha_start_daemon
%{_libexecdir}/xapi/cluster-stack/xhad/ha_stop_daemon
%{_libexecdir}/xapi/cluster-stack/xhad/weightctl
%{_libexecdir}/xapi/cluster-stack/xhad/writestatefile
%{_libexecdir}/xapi/cluster-stack/xhad/xhad

%{?_cov_results_package}

%changelog
* Mon Dec 16 2024 Christian Lindig <christian.lindig@citrix.com> - 10.3.1-3
- Bump release and rebuild

* Fri Dec 13 2024 Christian Lindig <christian.lindig@cloud.com> - 10.3.1-2
- Bump release and rebuild

* Fri Dec 13 2024 Christian Lindig <christian.lindig@cloud.com> - 10.3.1-1
- lib: ensure the correct maximum amount of hosts
- CA-403139: Set scheduler policy and priority thread
- CA-403683: Configurable syslog printing

* Thu Dec 12 2024 Christian Lindig <christian.lindig@cloud.com> - 10.3.0-2
- Bump release and rebuild

* Thu Jul 22 2021 Rachel Yan <Rachel.Yan@citrix.com> - 10.3.0-1
- CA-322009: Fixed warning from set scheduler

* Tue Feb 16 2021 Rob Hoes <rob.hoes@citrix.com> - 10.2.0-1
- CA-351513: fix gcc's -fanalyzer warnings
- maintenance: ignore generated files

* Fri Feb 21 2020 Steven Woods <steven.woods@citrix.com> - 10.1.0-2
- CP33120: Add Coverity build macros

* Mon Jul 01 2019 Christian Lindig <christian.lindig@citrix.com> - 10.1.0-1
- XSI-301: Print errno when watchdog hypercall fails.
- XSI-301: remove duplicated unlock_pages lines
- CA-315962 cleanupwatchdog: Use hypercall's errno
- CA-315962 cleanupwatchdog: exit when encountering errors on hypercalls
- CA-315962 cleanupwatchdog: restrict hypercalls to disable watchdogs
- CA-315962 cleanupwatchdog: simplify hypercall call handling
- CA-315962 cleanupwatchdog: Allow resetting watchdog slots without an HA file
- CA-315962: Flush watchdog slots on HA startup

* Tue Nov 8 2016 Euan Harris <euan.harris@citrix.com> - 10.0.1-1
- Include Git commit metadata in source archive

* Tue Oct 18 2016 Euan Harris <euan.harris@citrix.com> - 10.0.0-1
- Build from GitHub sources

* Mon Oct 17 2016 Vivek Kumar Chaubey <vivekkumar.chaubey@citrix.com> - 7.0.91-248
- Build using transformer
